import React, { useState, useContext } from 'react'
import { graphql, navigate } from 'gatsby'
import useLocalStorage from '@illinois/react-use-local-storage'

import { renderAst } from '../markdown'
import { ChapterContext, UiTextContext } from '../context'
import Layout from '../components/layout'
import { Button } from '../components/button'

import classes from '../styles/chapter.module.sass'

const Pagination = ({ prev, next, lang }) => {
    const uiText = useContext(UiTextContext)
    const buttons = [
        { slug: prev, text: `« ${uiText.prevChapter}` },
        { slug: next, text: `${uiText.nextChapter} »` },
    ]

    return (
        <section className={classes.pagination}>
            {buttons.map(({ slug, text }) => (
                <div key={slug}>
                    {slug && (
                        <Button
                            variant="secondary"
                            small
                            onClick={() => navigate(`${lang}/${slug}`)}
                        >
                            {text}
                        </Button>
                    )}
                </div>
            ))}
        </section>
    )
}

const Template = ({ data }) => {
    const { markdownRemark } = data
    const { frontmatter, htmlAst, parent, fields } = markdownRemark
    const { title, description, prev, next, id } = frontmatter
    const { lang } = fields
    const [activeExc, setActiveExc] = useState(null)
    const [completed, setCompleted] = useLocalStorage(`spacy-course-completed-${id}`, [])
    const html = renderAst(htmlAst)

    return (
        <ChapterContext.Provider value={{ lang, activeExc, setActiveExc, completed, setCompleted }}>
            <Layout lang={lang} title={title} description={description} pageName={parent.name}>
                {html}

                <Pagination prev={prev} next={next} lang={lang} />
            </Layout>
        </ChapterContext.Provider>
    )
}

export default Template

export const pageQuery = graphql`
    query($slug: String!) {
        markdownRemark(fields: { slug: { eq: $slug } }) {
            htmlAst
            frontmatter {
                id
                title
                description
                next
                prev
            }
            fields {
                lang
            }
            parent {
                ... on File {
                    name
                }
            }
        }
    }
`
