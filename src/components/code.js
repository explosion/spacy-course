import React from 'react'
import { StaticQuery, graphql } from 'gatsby'
import classNames from 'classnames'

import Hint from './hint'

import classes from '../styles/code.module.sass'

function getFiles({ allCode }) {
    return Object.assign(
        {},
        ...allCode.edges.map(({ node }) => ({
            [node.name]: node.code,
        }))
    )
}

function makeTest(template, testFile, solution) {
    return template
        .replace(/\${solution}/g, solution)
        .replace(/\${test}/g, testFile)
}

class CodeBlock extends React.Component {
    state = { Juniper: null, showSolution: false }

    handleShowSolution() {
        this.setState({ showSolution: true })
    }

    updateJuniper() {
        if (!this.state.Juniper) {
            import('./juniper').then(Juniper => {
                this.setState({ Juniper: Juniper.default })
            })
        }
    }

    componentDidMount() {
        this.updateJuniper()
    }

    componentDidUpdate() {
        this.updateJuniper()
    }

    render() {
        const { Juniper, showSolution } = this.state
        const { id, source, solution, test, children } = this.props
        const sourceId = source || `exc_${id}`
        const solutionId = solution || `solution_${id}`
        const testId = test || `test_${id}`

        const juniperClassNames = {
            cell: classes.cell,
            input: classes.input,
            button: classes.button,
            output: classes.output,
        }
        const hintActions = [{ text: 'Show solution', onClick: () => this.handleShowSolution() }]
        // TODO: fix
        return !Juniper ? (
            'Loading Juniper...'
        ) : (
            <StaticQuery
                query={graphql`
                    {
                        site {
                            siteMetadata {
                                testTemplate
                                juniper {
                                    repo
                                    branch
                                    kernelType
                                }
                            }
                        }
                        allCode {
                            edges {
                                node {
                                    name
                                    code
                                }
                            }
                        }
                    }
                `}
                render={data => {
                    const { testTemplate } = data.site.siteMetadata
                    const { repo, branch, kernelType } = data.site.siteMetadata.juniper
                    const files = getFiles(data)
                    // TODO: validation
                    const sourceFile = files[sourceId]
                    const solutionFile = files[solutionId]
                    const testFile = files[testId]
                    return (
                        <div className={classes.root}>
                            <Juniper
                                msgButton="Run code"
                                classNames={juniperClassNames}
                                repo={repo}
                                branch={branch}
                                kernelType={kernelType}
                                actions={({ runCode }) => (
                                    <button
                                        onClick={() => runCode(value => makeTest(testTemplate, testFile, value))}
                                        className={classNames(
                                            classes.button,
                                            classes.buttonPrimary
                                        )}
                                    >
                                        Submit
                                    </button>
                                )}
                            >
                                {showSolution ? solutionFile : sourceFile}
                            </Juniper>
                            <Hint actions={hintActions}>{children}</Hint>
                        </div>
                    )
                }}
            />
        )
    }
}

export default CodeBlock
