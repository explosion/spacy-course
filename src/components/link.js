import React from 'react'
import PropTypes from 'prop-types'
import { Link as GatsbyLink } from 'gatsby'
import classNames from 'classnames'

import classes from '../styles/link.module.sass'

export const Link = ({ children, to, href, onClick, variant, hidden, className, ...other }) => {
    const dest = to || href
    const external = /(http(s?)):\/\//gi.test(dest)
    const linkClassNames = classNames(classes.root, className, {
        [classes.hidden]: hidden,
        [classes.secondary]: variant === 'secondary',
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

Link.propTypes = {
    children: PropTypes.node.isRequired,
    to: PropTypes.string,
    href: PropTypes.string,
    onClick: PropTypes.func,
    variant: PropTypes.oneOf(['secondary', null]),
    hidden: PropTypes.bool,
    className: PropTypes.string,
}
