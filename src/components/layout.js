import React from 'react'

import SEO from './seo'
import Link from './link'
import { H3 } from './typography'

import '../styles/index.sass'
import classes from '../styles/layout.module.sass'

const Layout = ({ pageTitle, title, description, children }) => {
    return (
        <>
            <SEO title={title} />
            <main className={classes.root}>
                {pageTitle && (
                    <nav className={classes.topbar}>
                        <h1 className={classes.pageTitle}>
                            <Link hidden to="/">
                                {pageTitle}
                            </Link>
                        </h1>
                    </nav>
                )}
                <div className={classes.content}>
                    <header className={classes.header}>
                        {title && <h1 className={classes.title}>{title}</h1>}
                        {description && <p className={classes.description}>{description}</p>}
                    </header>
                    {children}
                </div>

                <footer className={classes.footer}>
                    <div className={classes.footerContent}>
                        <H3>About this course</H3>
                        Footer content
                    </div>
                </footer>
            </main>
        </>
    )
}

export default Layout
