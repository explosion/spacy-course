import React, { useContext } from 'react'

import { LocaleContext } from '../context'
import Logos from '../../static/logos.svg'

export const Logo = ({ width = 300, height = 107, lang, className, ...props }) => {
    const { title } = useContext(LocaleContext)
    return (
        <>
            <Logos aria-hidden="true" width={1} height={1} style={{ visibility: 'hidden' }} />
            <svg
                aria-label={title}
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
