import React, { useState } from 'react'
import { graphql, navigate } from 'gatsby'
import useLocalStorage from '@illinois/react-use-local-storage'

import { renderAst } from '../markdown'
import { ChapterContext } from '../context'
import Layout from '../components/layout'
import Button from '../components/button'

import classes from '../styles/chapter.module.sass'

const Template = ({ data }) => {
    const { markdownRemark } = data
    const { frontmatter, htmlAst } = markdownRemark
    const { title, description, prev, next, id } = frontmatter
    const [activeExc, setActiveExc] = useState(null)
    const [completed, setCompleted] = useLocalStorage(`spacy-course-completed-${id}`, [])
    const html = renderAst(htmlAst)

    return (
        <ChapterContext.Provider value={{ activeExc, setActiveExc, completed, setCompleted }}>
            <Layout title={title} description={description}>
                {html}

                <section className={classes.pagination}>
                    <div>
                        {prev && (
                            <Button variant="secondary" small onClick={() => navigate(prev)}>
                                &laquo; Previous Chapter
                            </Button>
                        )}
                    </div>

                    <div>
                        {next && (
                            <Button variant="secondary" small onClick={() => navigate(next)}>
                                Next Chapter &raquo;
                            </Button>
                        )}
                    </div>
                </section>
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
        }
    }
`
