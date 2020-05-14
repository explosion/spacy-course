import React, { useContext } from 'react'
import classNames from 'classnames'

import { LocaleContext } from '../context'
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
    const { uiText } = useContext(LocaleContext)
    const buttonClassNames = classNames({
        [classes.completeInactive]: !completed,
        [classes.completeActive]: completed,
    })
    return (
        <Button small={small} onClick={toggleComplete} className={buttonClassNames}>
            {!completed ? (
                uiText.markAsCompleted
            ) : (
                <>
                    <IconCheck width={14} height={14} className={classes.completeIcon} />{' '}
                    <span className={classes.completeLabel}>{uiText.completed}</span>{' '}
                    <span className={classes.completeLabelHover}>{uiText.removeFromCompleted}</span>
                </>
            )}
        </Button>
    )
}
