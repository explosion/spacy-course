import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/layout'
import Link from '../components/link'

import classes from '../styles/index.module.sass'

export default ({ data }) => {
    const chapters = data.allMarkdownRemark.edges.map(({ node }) => ({
        slug: node.fields.slug,
        title: node.frontmatter.title,
        description: node.frontmatter.description,
    }))
    return (
        <Layout>
            {chapters.map(({ slug, title, description }) => (
                <section key={slug} className={classes.chapter}>
                    <h2 className={classes.chapterTitle}>
                        <Link hidden to={slug}>
                            {title}
                        </Link>
                    </h2>
                    <p className={classes.chapterDesc}>{description}</p>
                </section>
            ))}
        </Layout>
    )
}

export const pageQuery = graphql`
    {
        allMarkdownRemark(filter: { frontmatter: { type: { eq: "chapter" } } }) {
            edges {
                node {
                    fields {
                        slug
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
