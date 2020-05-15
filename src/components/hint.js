import React, { useState, useCallback, useContext } from 'react'

import { LocaleContext } from '../context'
import classes from '../styles/hint.module.sass'

export const Hint = ({ expanded = false, actions = [], children }) => {
    const { uiText } = useContext(LocaleContext)
    const [isExpanded, setIsExpanded] = useState(expanded)
    const handleExpand = useCallback(() => setIsExpanded(!isExpanded), [isExpanded])
    return (
        <aside className={classes.root}>
            {isExpanded && children && <div className={classes.content}>{children}</div>}
            <menu className={classes.actions}>
                {children && (
                    <button className={classes.label} onClick={handleExpand}>
                        {isExpanded ? uiText.hideHints : uiText.showHints}
                    </button>
                )}
                {actions.map(({ text, onClick }, i) => (
                    <button className={classes.label} key={i} onClick={onClick}>
                        {text}
                    </button>
                ))}
            </menu>
        </aside>
    )
}
