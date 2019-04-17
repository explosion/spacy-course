import React from 'react'
import { StaticQuery, graphql } from 'gatsby'
import Marked from 'reveal.js/plugin/markdown/marked.js'
import classNames from 'classnames'

import '../styles/reveal.css'
import classes from '../styles/slides.module.sass'

function getFiles({ allMarkdownRemark }) {
    return Object.assign(
        {},
        ...allMarkdownRemark.edges.map(({ node }) => ({
            [node.fields.slug.replace('/', '')]: node.rawMarkdownBody,
        }))
    )
}

function getSlideContent(data, source) {
    const files = getFiles(data)
    const file = files[source] || ''
    return file.split('\n---\n').map(f => f.trim())
}

class Slides extends React.Component {
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
                                            }
                                        }
                                    }
                                }
                            }
                        `}
                        render={data => {
                            const content = getSlideContent(data, source)
                            return (
                                <div className={slideClassNames}>
                                    {content.map((markdown, i) => (
                                        <section
                                            key={i}
                                            data-markdown=""
                                            data-separator-notes="^Notes:"
                                        >
                                            <textarea data-template defaultValue={markdown} />
                                        </section>
                                    ))}
                                </div>
                            )
                        }}
                    />
                </div>
            </div>
        )
    }
}

export default Slides
