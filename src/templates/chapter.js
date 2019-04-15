import React, { useState } from 'react'
import { graphql } from 'gatsby'

import { renderAst } from '../markdown'
import { ChapterContext } from '../context'
import Layout from '../components/layout'

const Template = ({ data, pageContext }) => {
    const [activeExc, setActiveExc] = useState(null)
    const { markdownRemark, site } = data
    const { frontmatter, htmlAst } = markdownRemark
    const { title, description } = frontmatter // TODO: prev, next
    const html = renderAst(htmlAst)

    return (
        <ChapterContext.Provider value={{ activeExc, setActiveExc }}>
            <Layout pageTitle={site.siteMetadata.title} title={title} description={description}>
                {html}
            </Layout>
        </ChapterContext.Provider>
    )
}

export default Template

export const pageQuery = graphql`
    query($slug: String!) {
        site {
            siteMetadata {
                title
            }
        }
        markdownRemark(fields: { slug: { eq: $slug } }) {
            htmlAst
            frontmatter {
                title
                description
            }
        }
    }
`
