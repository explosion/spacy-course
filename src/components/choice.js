import React, { useState, useCallback } from 'react'
import classNames from 'classnames'

import Button from './button'
import classes from '../styles/choice.module.sass'

const Choice = ({ children = [] }) => {
    const [selected, setSelected] = useState(null)
    const [answer, setAnswer] = useState(null)
    const handleAnswer = useCallback(() => setAnswer(selected), [selected])
    const options = children.filter(child => child != '\n')
    return (
        <div className={classes.root}>
            {options.map(({ key, props }, i) => (
                <div key={key} className={classes.option}>
                    <input
                        className={classes.input}
                        name="choice"
                        id={`choice-${i}`}
                        value={i}
                        type="radio"
                        checked={selected === i}
                        onChange={() => setSelected(i)}
                    />
                    <label className={classes.label} htmlFor={`choice-${i}`}>
                        {props.text}
                    </label>
                </div>
            ))}
            <Button variant="primary" onClick={handleAnswer}>
                Submit
            </Button>
            {options.map(({ key, props }, i) => {
                const isCorrect = !!props.correct
                return answer === i ? (
                    <div className={classNames(classes.answer, { [classes.correct]: isCorrect })}>
                        <strong
                            className={classNames(classes.answerLabel, {
                                [classes.answerLabelCorrect]: isCorrect,
                            })}
                        >
                            {isCorrect ? "That's correct! " : 'Incorrect. '}
                        </strong>
                        {props.children}
                    </div>
                ) : null
            })}
        </div>
    )
}

export const Option = ({ children }) => {
    return children
}

export default Choice
