import React from 'react'

import SEO from './seo'

import classes from '../styles/layout.module.sass'

const Layout = ({ title, children }) => {
    return (
        <>
            <SEO title={title} />
            <main className={classes.root}>
                {title && <h1 className={classes.title}>{title}</h1>}
                {children}
            </main>
        </>
    )
}

export default Layout
