import React, { useContext } from 'react'
import { navigate } from 'gatsby'

import { Button } from './button'
import { UiTextContext } from '../context'

export const Pagination = ({ prev, next, lang, className }) => {
    const uiText = useContext(UiTextContext)
    const buttons = [
        { slug: prev, text: `« ${uiText.prevChapter}` },
        { slug: next, text: `${uiText.nextChapter} »` },
    ]

    return (
        <section className={className}>
            {buttons.map(({ slug, text }) => (
                <div key={slug}>
                    {slug && (
                        <Button
                            variant="secondary"
                            small
                            onClick={() => navigate(`${lang}/${slug}`)}
                        >
                            {text}
                        </Button>
                    )}
                </div>
            ))}
        </section>
    )
}
