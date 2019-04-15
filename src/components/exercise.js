import React, { useRef, useCallback, useContext, useEffect } from 'react'
import classNames from 'classnames'

import { ChapterContext } from '../context'
import iconSlides from '../images/icon_slides.svg'
import classes from '../styles/exercise.module.sass'

const Exercise = ({ id, title, type, children }) => {
    const excRef = useRef()
    const excId = parseInt(id)
    const { activeExc, setActiveExc } = useContext(ChapterContext)
    const isExpanded = activeExc === excId
    useEffect(() => {
        if (isExpanded && excRef.current) {
            excRef.current.scrollIntoView()
        }
    })
    const handleExpand = useCallback(() => setActiveExc(isExpanded ? null : excId), [
        isExpanded,
        excId,
    ])
    const handleNext = useCallback(() => setActiveExc(excId + 1))
    const rootClassNames = classNames(classes.root, {
        [classes.expanded]: isExpanded,
        [classes.wide]: isExpanded && type === 'slides',
    })
    const titleClassNames = classNames(classes.title, {
        [classes.titleExpanded]: isExpanded,
    })
    return (
        <section ref={excRef} id={id} className={rootClassNames}>
            <h2 className={titleClassNames} onClick={handleExpand}>
                {title}
                {type === "slides" && <img alt="" width={28} height={28} className={classes.icon} src={iconSlides} />}
            </h2>
            {isExpanded && (
                <div>
                    {children}
                    <footer className={classes.footer}>
                        <button className={classes.button} onClick={handleNext}>
                            Next
                        </button>
                    </footer>
                </div>
            )}
        </section>
    )
}

export default Exercise
