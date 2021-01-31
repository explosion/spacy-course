import React, { useCallback } from 'react'
import { navigate } from 'gatsby'

import SEO from './seo'
import { Link } from './link'
import { H3 } from './typography'
import { Logo } from './logo'
import { LocaleContext } from '../context'

import '../styles/index.sass'
import classes from '../styles/layout.module.sass'
import locale from '../../locale.json'

const Layout = ({ isHome, title, description, lang, pageName, logo, children }) => {
    const localeData = locale[lang] || {}
    const alert = localeData.uiText.alert
    const langs = Object.keys(locale).map(c => ({ langCode: c, langName: locale[c].langName }))
    const handleChangeLang = useCallback(
        ({ target }) => {
            const newLang = target.value
            if (newLang !== lang) {
                navigate(pageName ? `/${newLang}/${pageName}` : `/${newLang}`)
            }
        },
        [lang, pageName]
    )
    return (
        <>
            <SEO title={title} description={description} lang={lang} localeData={localeData} />
            <LocaleContext.Provider value={localeData}>
                <main className={classes.root}>
                    {langs.length > 1 && (
                        <select
                            className={classes.langSelect}
                            defaultValue={lang}
                            onChange={handleChangeLang}
                        >
                            {langs.map(({ langCode, langName }) => (
                                <option key={langCode} value={langCode}>
                                    {langName}
                                </option>
                            ))}
                        </select>
                    )}

                    {!isHome && (
                        <h1 className={classes.logo}>
                            <Link hidden to={`/${lang}`}>
                                <Logo lang={lang} width={150} height={54} />
                            </Link>
                        </h1>
                    )}
                    <div className={classes.content}>
                        {(title || description) && (
                            <header className={classes.header}>
                                {title && <h1 className={classes.title}>{title}</h1>}
                                {description && (
                                    <p className={classes.description}>{description}</p>
                                )}
                            </header>
                        )}
                        {logo}
                        {alert && (
                                <aside className={classes.alert}>
                                    <strong>{alert.title}</strong> {alert.text}{' '}
                                    <Link to="https://spacy.io/usage/v3">
                                        {alert.button} &rarr;
                                    </Link>
                                </aside>
                            )}
                        {children}
                    </div>

                    <footer className={classes.footer}>
                        <div className={classes.footerContent}>
                            <section className={classes.footerSection}>
                                <H3>{localeData.uiText.aboutCourse}</H3>
                                <p>{localeData.description}</p>
                            </section>

                            <section className={classes.footerSection}>
                                <H3>{localeData.uiText.aboutMe}</H3>
                                <img src="/profile.jpg" alt="" className={classes.profile} />
                                <p>{localeData.bio}</p>
                            </section>

                            {localeData.footerLinks && (
                                <ul className={classes.footerLinks}>
                                    {localeData.footerLinks.map(({ text, url }, i) => (
                                        <li key={i} className={classes.footerLink}>
                                            <Link variant="secondary" to={url}>
                                                {text}
                                            </Link>
                                        </li>
                                    ))}
                                </ul>
                            )}
                        </div>
                    </footer>
                </main>
            </LocaleContext.Provider>
        </>
    )
}

export default Layout
