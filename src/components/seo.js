import React from 'react'
import Helmet from 'react-helmet'
import { StaticQuery, graphql } from 'gatsby'

const SEO = ({ title, description, lang, localeData }) => (
    <StaticQuery
        query={query}
        render={data => {
            const { siteUrl, twitter, fonts } = data.site.siteMetadata
            const socialImage = localeData.socialImage || 'social.jpg'
            const pageTitle = title
                ? `${title} · ${localeData.title}`
                : `${localeData.title} · ${localeData.slogan}`
            const pageDesc = description || localeData.description
            const image = `${siteUrl}/${socialImage}`
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
                    content: localeData.title,
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
                    content: `@${twitter}`,
                },
                {
                    name: 'twitter:site',
                    content: `@${twitter}`,
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
                    {fonts && (
                        <link
                            href={`https://fonts.googleapis.com/css?family=${fonts}`}
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
                siteUrl
                twitter
                fonts
            }
        }
    }
`
