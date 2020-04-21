import React, { useContext } from 'react'

import { UiTextContext } from '../context'
import Logos from '../../static/logos.svg'

export const Logo = ({ width = 300, height = 107, lang, className, ...props }) => {
    const uiText = useContext(UiTextContext)
    return (
        <>
            <Logos aria-hidden="true" width={1} height={1} style={{ visibility: 'hidden' }} />
            <svg
                aria-label={uiText.courseTitle}
                viewBox={Logos.defaultProps.viewBox}
                className={className}
                width={width}
                height={height}
                {...props}
            >
                <use xlinkHref={`#${lang}`} />
            </svg>
        </>
    )
}
