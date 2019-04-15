import React from 'react'
import classNames from 'classnames'

import classes from '../styles/button.module.sass'

const Button = ({ Component = 'button', children, onClick, variant = 'default', small }) => {
    const buttonClassNames = classNames(classes.root, {
        [classes.primary]: variant === 'primary',
        [classes.secondary]: variant === 'secondary',
        [classes.small]: !!small,
    })
    return (
        <Component className={buttonClassNames} onClick={onClick}>
            {children}
        </Component>
    )
}

export default Button
