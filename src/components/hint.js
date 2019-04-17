import React, { useState, useCallback } from 'react'

import classes from '../styles/hint.module.sass'

export const Hint = ({ expanded = false, actions = [], children }) => {
    const [isExpanded, setIsExpanded] = useState(expanded)
    const handleExpand = useCallback(() => setIsExpanded(!isExpanded), [isExpanded])
    return (
        <aside className={classes.root}>
            {isExpanded && children && <div className={classes.content}>{children}</div>}
            <menu className={classes.actions}>
                {children && (
                    <button className={classes.label} onClick={handleExpand}>
                        {isExpanded ? 'Hide hints' : 'Show hints'}
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
