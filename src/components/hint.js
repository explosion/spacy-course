import React, { useState, useCallback } from 'react'

import classes from '../styles/hint.module.sass'

const Hint = ({ expanded = false, children }) => {
    const [isExpanded, setIsExpanded] = useState(expanded)
    const handleExpand = useCallback(() => setIsExpanded(!isExpanded), [isExpanded])
    return (
        <aside className={classes.root}>
            <h4 onClick={handleExpand}>Show hint</h4>
            {isExpanded && children}
        </aside>
    )
}

export default Hint
