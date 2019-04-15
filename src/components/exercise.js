import React, { useState, useCallback } from 'react'

import classes from '../styles/exercise.module.sass'

const Exercise = ({ id, title, type, expanded = true, children }) => {
    const [isExpanded, setIsExpanded] = useState(expanded)
    const handleExpand = useCallback(() => setIsExpanded(!isExpanded), [isExpanded])
    return (
        <section id={id} className={classes.root}>
            <h2 className={classes.title} onClick={handleExpand}>
                {title}
            </h2>
            {isExpanded && children}
        </section>
    )
}

export default Exercise
