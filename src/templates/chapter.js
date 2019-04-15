import React from 'react'
import { graphql } from 'gatsby'

import { renderAst } from '../markdown'
import Layout from '../components/layout'

const Template = ({ data, pageContext }) => {
    const { markdownRemark } = data
    const { frontmatter, htmlAst } = markdownRemark
    const { title } = frontmatter // TODO: prev, next
    const html = renderAst(htmlAst)

    return <Layout title={title}>{html}</Layout>
}

export default Template

export const pageQuery = graphql`
    query($slug: String!) {
        markdownRemark(fields: { slug: { eq: $slug } }) {
            htmlAst
            frontmatter {
                title
            }
        }
    }
`
