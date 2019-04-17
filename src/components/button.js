import React from 'react'
import classNames from 'classnames'

import IconCheck from '../../static/icon_check.svg'
import classes from '../styles/button.module.sass'

export const Button = ({ Component = 'button', children, onClick, variant, small, className }) => {
    const buttonClassNames = classNames(classes.root, className, {
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

export const CompleteButton = ({ completed, toggleComplete, small = true }) => {
    const buttonClassNames = classNames({
        [classes.completeInactive]: !completed,
        [classes.completeActive]: completed,
    })
    return (
        <Button small={small} onClick={toggleComplete} className={buttonClassNames}>
            {!completed ? (
                'Mark as completed'
            ) : (
                <>
                    <IconCheck width={14} height={14} className={classes.completeIcon} />{' '}
                    <span className={classes.completeLabel}>Completed</span>{' '}
                    <span className={classes.completeLabelHover}>Remove from completed</span>
                </>
            )}
        </Button>
    )
}
