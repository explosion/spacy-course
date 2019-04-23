import React from 'react'
import Helmet from 'react-helmet'
import { StaticQuery, graphql } from 'gatsby'

const SEO = ({ title, description }) => (
    <StaticQuery
        query={query}
        render={data => {
            const lang = 'en'
            const siteMetadata = data.site.siteMetadata
            const pageTitle = title
                ? `${title} · ${siteMetadata.title}`
                : `${siteMetadata.title} · ${siteMetadata.slogan}`
            const pageDesc = description || siteMetadata.description
            const image = `${siteMetadata.siteUrl}/social.jpg`
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
                    content: 'summary_large_image',
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

            return (
                <Helmet defer={false} htmlAttributes={{ lang }} title={pageTitle} meta={meta}>
                    {siteMetadata.fonts && (
                        <link
                            href={`https://fonts.googleapis.com/css?family=${siteMetadata.fonts}`}
                            rel="stylesheet"
                        />
                    )}
                </Helmet>
            )
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
                slogan
                siteUrl
                twitter
                fonts
            }
        }
    }
`
