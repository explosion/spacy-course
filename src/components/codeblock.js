import React from 'react'
import { StaticQuery, graphql } from 'gatsby'

function getFiles({ allPython }) {
    return Object.assign(
        {},
        ...allPython.edges.map(({ node }) => ({
            [node.name]: node.code,
        }))
    )
}

class CodeBlock extends React.Component {
    state = { Juniper: null, showSolution: false }

    handleShowSolution() {
        this.setState({ showSolution: true })
    }

    updateJuniper() {
        if (window.Juniper && !this.state.Juniper) {
            this.setState({ Juniper: window.Juniper })
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
        const { source, solution, test, children } = this.props
        const query = graphql`
            {
                site {
                    siteMetadata {
                        juniper {
                            repo
                        }
                    }
                }
                allPython {
                    edges {
                        node {
                            name
                            code
                        }
                    }
                }
            }
        `
        return !Juniper ? (
            'Loading Juniper...'
        ) : (
            <StaticQuery
                query={query}
                render={data => {
                    const files = getFiles(data)
                    // TODO: validation
                    const sourceFile = files[source]
                    const solutionFile = files[solution]
                    // const testFile = files[test]
                    return (
                        <>
                            <Juniper repo={data.site.siteMetadata.juniper.repo}>
                                {showSolution ? solutionFile : sourceFile}
                            </Juniper>
                            {children}
                            <button onClick={() => this.handleShowSolution()}>Show solution</button>
                        </>
                    )
                }}
            />
        )
    }
}

export default CodeBlock
