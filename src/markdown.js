import React from 'react'
import rehypeReact from 'rehype-react'

import Exercise from './components/exercise'
import CodeBlock from './components/code'
import Link from './components/link'
import Slides from './components/slides'
import { H3, Hr, Ul, Li, InlineCode } from './components/typography'

export const renderAst = new rehypeReact({
    createElement: React.createElement,
    components: {
        exercise: Exercise,
        slides: Slides,
        codeblock: CodeBlock,
        a: Link,
        hr: Hr,
        h3: H3,
        ul: Ul,
        li: Li,
        code: InlineCode,
        // h2: H2,
        // h3: H3,
        // h4: H4,
        // h5: H5,
        // ,
        // aside: Aside,
        // hr: Hr,
    },
}).Compiler
