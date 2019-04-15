import React from 'react'
import rehypeReact from 'rehype-react'

import Exercise from './components/exercise'
import CodeBlock from './components/codeblock'
import Hint from './components/hint'

export const renderAst = new rehypeReact({
    createElement: React.createElement,
    components: {
        exercise: Exercise,
        codeblock: CodeBlock,
        hint: Hint,
        // a: Link,
        // h2: H2,
        // h3: H3,
        // h4: H4,
        // h5: H5,
        // code: InlineCode,
        // aside: Aside,
        // hr: Hr,
    },
}).Compiler
