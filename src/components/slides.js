import React, { useContext, useEffect, useRef, useState } from 'react'
import { StaticQuery, graphql } from 'gatsby'
import Marked from 'reveal.js/plugin/markdown/marked.js'
import Prism from 'prismjs'
import classNames from 'classnames'

import { ChapterContext, LocaleContext } from '../context'
import '../styles/reveal.css'
import '../styles/plyr.css'
import classes from '../styles/slides.module.sass'

const CODE_LANGS = ['python']

function getFiles({ allMarkdownRemark }, lang) {
    return Object.assign(
        {},
        ...allMarkdownRemark.edges
            .filter(({ node }) => node.fields.lang === lang)
            .map(({ node }) => ({
                [node.fields.slug.replace('/', '')]: node.rawMarkdownBody,
            }))
    )
}

function getSlideContent(data, source, lang) {
    const files = getFiles(data, lang)
    const key = `${lang}/slides/${source}`
    const file = files[key] || ''
    return file.split('\n---\n').map(f => f.trim())
}

function timestampToSeconds(ts) {
    if (ts === null) return ts
    const [mins, secs] = ts.split(':')
    const seconds =
        secs.length > 2 ? parseFloat(`${secs.slice(0, 2)}.${secs.slice(2)}`) : parseInt(secs)
    return parseInt(mins) * 60 + seconds
}

const Slides = ({ source, start = null, end = null }) => {
    const { slideType, setSlideType } = useContext(ChapterContext)
    const { video, uiText } = useContext(LocaleContext)
    const hasVideo = video && start !== null && end !== null
    return hasVideo ? (
        <>
            <menu className={classes.menu}>
                {['video', 'slides'].map(value => {
                    const isActive = slideType === value
                    const tabClassNames = classNames(classes.tab, {
                        [classes.tabActive]: isActive,
                    })
                    return (
                        <label key={value} htmlFor={value} className={tabClassNames}>
                            <input
                                className={classes.radio}
                                name="type"
                                id={value}
                                type="radio"
                                defaultChecked={isActive}
                                onChange={() => setSlideType(value)}
                            />
                            {uiText[value]}
                        </label>
                    )
                })}
            </menu>
            {slideType === 'video' ? (
                <Video id={video} start={timestampToSeconds(start)} end={timestampToSeconds(end)} />
            ) : (
                <SlideDeck source={source} />
            )}
        </>
    ) : (
        <SlideDeck source={source} />
    )
}

const Video = ({ id, start = 0, end = 0 }) => {
    const ref = useRef(null)
    const { lang } = useContext(ChapterContext)
    const { uiText } = useContext(LocaleContext)
    const [duration, setDuration] = useState(0)
    const url = `https://www.youtube.com/embed/${id}?start=${start}&end=${end}&version=3&color=white&hl=${lang}&modestbranding=1&rel=0`
    const options = {
        duration: end,
        tooltips: { seek: false },
        disableContextMenu: false,
    }

    useEffect(() => {
        let player = null
        import('plyr').then(({ default: Plyr }) => {
            player = new Plyr(ref.current, options)
            player.on('ready', () => {
                if (ref.current) {
                    const marker = document.createElement('span')
                    ref.current.querySelector('.plyr__progress').appendChild(marker)
                    marker.className = 'plyr__tooltip plyr__marker'
                    marker.textContent = uiText.start
                    marker.addEventListener('click', () => {
                        player.currentTime = start
                        player.play()
                    })
                }
                setDuration(player.duration)
                player.currentTime = start
            })
            player.on('timeupdate', () => {
                if (player.currentTime > end) {
                    player.pause()
                    player.currentTime = end
                }
            })
            player.on('play', () => {
                if (player.currentTime >= end) {
                    player.currentTime = start
                }
            })
        })
        return () => {
            if (player) player.destroy()
        }
    }, [end, options, start, uiText.start])

    return (
        <div style={{ '--plyr-marker': `${(100 / duration) * start}%` }}>
            <div ref={ref}>
                <iframe
                    title={id}
                    width="800"
                    height="450"
                    src={url}
                    frameBorder="0"
                    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                />
            </div>
        </div>
    )
}

class SlideDeck extends React.Component {
    componentDidMount() {
        import('reveal.js').then(({ default: Reveal }) => {
            window.Reveal = Reveal
            window.marked = Marked
            import('reveal.js/plugin/markdown/markdown.js').then(({ RevealMarkdown }) => {
                RevealMarkdown.init()
                Reveal.initialize({
                    center: false,
                    progress: false,
                    showNotes: true,
                    controls: true,
                    width: '100%',
                    height: 600,
                    minScale: 0.75,
                    maxScale: 1,
                })
            })
        })
        Promise.all(CODE_LANGS.map(lang => import(`prismjs/components/prism-${lang}`))).then(() =>
            setTimeout(() => {
                Prism.highlightAll()
            }, 1000)
        )
    }

    componentWillUnmount() {
        // Work around default reveal.js behaviour that doesn't allow
        // re-initialization and clashes with React
        delete window.Reveal
        delete window.marked
        delete require.cache[require.resolve('reveal.js')]
        delete require.cache[require.resolve('reveal.js/plugin/markdown/markdown.js')]
    }

    render() {
        const { source } = this.props
        const revealClassNames = classNames('reveal', 'show-notes', classes.reveal)
        const slideClassNames = classNames('slides', classes.slides)

        return (
            <div className={classes.root}>
                <div className={revealClassNames}>
                    <ChapterContext.Consumer>
                        {({ lang }) => (
                            <StaticQuery
                                query={graphql`
                                    {
                                        allMarkdownRemark(
                                            filter: { frontmatter: { type: { eq: "slides" } } }
                                        ) {
                                            edges {
                                                node {
                                                    rawMarkdownBody
                                                    fields {
                                                        slug
                                                        lang
                                                    }
                                                }
                                            }
                                        }
                                    }
                                `}
                                render={data => {
                                    const content = getSlideContent(data, source, lang)
                                    return (
                                        <div className={slideClassNames}>
                                            {content.map((markdown, i) => (
                                                <section
                                                    key={i}
                                                    data-markdown=""
                                                    data-separator-notes="^Notes:"
                                                >
                                                    <textarea
                                                        data-template
                                                        defaultValue={markdown}
                                                    />
                                                </section>
                                            ))}
                                        </div>
                                    )
                                }}
                            />
                        )}
                    </ChapterContext.Consumer>
                </div>
            </div>
        )
    }
}

export default Slides
