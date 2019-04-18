import React from 'react'
import { StaticQuery, graphql } from 'gatsby'

import { Hint } from './hint'
import { Button } from './button'

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
    return template.replace(/\${solution}/g, solution).replace(/\${test}/g, testFile)
}

class CodeBlock extends React.Component {
    state = { Juniper: null, showSolution: false, key: 0 }

    handleShowSolution() {
        this.setState({ showSolution: true })
    }

    handleReset() {
        // Using the key as a hack to force component to rerender
        this.setState({ showSolution: false, key: this.state.key + 1 })
    }

    updateJuniper() {
        // This type of stuff only really works in class components. I'm not
        // sure why, but I've tried with function components and hooks lots of
        // times and couldn't get it to work. So class component it is.
        if (!this.state.Juniper) {
            // We need a dynamic import here for SSR. Juniper's dependencies
            // include references to the global window object and I haven't
            // managed to fix this using webpack yet. If we imported Juniper
            // at the top level, Gatsby won't build.
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
        const hintActions = [
            { text: 'Show solution', onClick: () => this.handleShowSolution() },
            { text: 'Reset', onClick: () => this.handleReset() },
        ]

        return (
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
                                    debug
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
                    const { repo, branch, kernelType, debug } = data.site.siteMetadata.juniper
                    const files = getFiles(data)
                    const sourceFile = files[sourceId]
                    const solutionFile = files[solutionId]
                    const testFile = files[testId]
                    return (
                        <div className={classes.root} key={this.state.key}>
                            {Juniper && (
                                <Juniper
                                    msgButton={null}
                                    classNames={juniperClassNames}
                                    repo={repo}
                                    branch={branch}
                                    kernelType={kernelType}
                                    debug={debug}
                                    actions={({ runCode }) => (
                                        <>
                                            <Button onClick={() => runCode()}>Run Code</Button>
                                            {testFile && (
                                                <Button
                                                    variant="primary"
                                                    onClick={() =>
                                                        runCode(value =>
                                                            makeTest(testTemplate, testFile, value)
                                                        )
                                                    }
                                                >
                                                    Submit
                                                </Button>
                                            )}
                                        </>
                                    )}
                                >
                                    {showSolution ? solutionFile : sourceFile}
                                </Juniper>
                            )}
                            <Hint actions={hintActions}>{children}</Hint>
                        </div>
                    )
                }}
            />
        )
    }
}

export default CodeBlock
