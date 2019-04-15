import React from 'react'
import Helmet from 'react-helmet'
import { StaticQuery, graphql } from 'gatsby'

const SEO = ({ title, description }) => (
    <StaticQuery
        query={query}
        render={data => {
            const lang = 'en'
            const siteMetadata = data.site.siteMetadata
            const pageTitle = title ? `${title} · ${siteMetadata.title}` : siteMetadata.title
            const pageDesc = description || siteMetadata.description
            const image = null // TODO: siteMetadata.siteUrl + socialImage
            const meta = [
                {
                    name: 'description',
                    content: pageDesc,
                },
                {
                    property: 'og:title',
                    content: pageTitle,
                },
                {
                    property: 'og:description',
                    content: pageDesc,
                },
                {
                    property: 'og:type',
                    content: `website`,
                },
                {
                    property: 'og:site_name',
                    content: siteMetadata.title,
                },
                {
                    property: 'og:image',
                    content: image,
                },
                {
                    name: 'twitter:card',
                    content: 'summary',
                },
                {
                    name: 'twitter:image',
                    content: image,
                },
                {
                    name: 'twitter:creator',
                    content: `@${siteMetadata.twitter}`,
                },
                {
                    name: 'twitter:site',
                    content: `@${siteMetadata.twitter}`,
                },
                {
                    name: 'twitter:title',
                    content: pageTitle,
                },
                {
                    name: 'twitter:description',
                    content: pageDesc,
                },
            ]

            return <Helmet htmlAttributes={{ lang }} title={pageTitle} meta={meta} />
        }}
    />
)

export default SEO

const query = graphql`
    query DefaultSEOQuery {
        site {
            siteMetadata {
                title
                description
                siteUrl
                twitter
            }
        }
    }
`
