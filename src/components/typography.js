import React from 'react'

import classes from '../styles/typography.module.sass'

export const H3 = ({ children }) => <h3 className={classes.h3}>{children}</h3>
export const Hr = () => <hr className={classes.hr} />
export const InlineCode = ({ children }) => <code className={classes.code}>{children}</code>

export const Ol = ({ children }) => <ol className={classes.ol}>{children}</ol>
export const Ul = ({ children }) => <ul className={classes.ul}>{children}</ul>
export const Li = ({ children }) => <li className={classes.li}>{children}</li>
