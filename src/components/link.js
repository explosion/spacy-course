import React from 'react'
import { Link as GatsbyLink } from 'gatsby'
import classNames from 'classnames'

import classes from '../styles/link.module.sass'

const Link = ({ children, to, href, onClick, hidden, className, ...other }) => {
    const dest = to || href
    const external = /(http(s?)):\/\//gi.test(dest)
    const linkClassNames = classNames(classes.root, className, {
        [classes.hidden]: hidden,
    })

    if (!external) {
        if ((dest && /^#/.test(dest)) || onClick) {
            return (
                <a href={dest} onClick={onClick} className={linkClassNames}>
                    {children}
                </a>
            )
        }
        return (
            <GatsbyLink to={dest} className={linkClassNames} {...other}>
                {children}
            </GatsbyLink>
        )
    }
    return (
        <a
            href={dest}
            className={linkClassNames}
            target="_blank"
            rel="noopener nofollow noreferrer"
            {...other}
        >
            {children}
        </a>
    )
}

export default Link
