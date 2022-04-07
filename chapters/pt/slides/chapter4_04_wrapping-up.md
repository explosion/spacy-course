---
type: slides
---

# Recapitulando...

Notes: Parabéns – você conseguiu e chegou ao final do curso!

---

# Suas novas habilidades da biblioteca spaCy que foram aprendidas:

- Extrair **características linguísticas**: classes gramaticais, termos sintáticos,
  e entidades nomeadas.
- Trabalhar com **fluxos de processamento (pipelines)** treinados.
- Encontrar palavras ou frases utilizando **expressões** e os comparadores `Matcher` e `PhraseMatcher` 
- Melhores práticas para trabalhar com **estruturas de dados**: `Doc`, `Token` `Span`,
  `Vocab`, `Lexeme`
- Encontrar **similaridades semânticas** utilizando **vetores de palavras**
- Escrever **componentes do fluxo de processamento** personalizados com **atributos extendidos**
- **Aumentar a escala e desempenho** dos fluxos de processamento (pipelines)
- Criar **dados de treinamento** para os modelos estatísticos da spaCy
- **Treinar e atualizar** os modelos de redes neurais da spaCy com novos dados

Notes: Aqui está um resumo de todas as novas habilidades que você aprendeu neste curso:

No primeiro capítulo, você aprendeu a extrair características linguísticas como
classes gramaticais, termos sintáticos e entidades nomeadas, e como trabalhar com 
fluxos de processamento treinados.

Você também aprendeu a escrever expressões de comparação poderosas para extrair
palavras e frases usando o comparador e o comparador de frases da spaCy.

O capítulo dois tratou da extração de informações, e você aprendeu a trabalhar com 
estruturas de dados como o `Doc`, `Token` e `Span`, bem como o `Vocab` e os
atributos léxicos.

Você também usou a biblioteca spaCy para prever similaridades semânticas usando
os vetores de palavras.

No capítulo três, você recebeu alguns insights sobre o fluxo de processamento, 
e aprendeu a escrever seus componentes personalizados que podem modificar seus 
documentos.

Você também criou novos atributos extendidos para os documentos, tokens e partições,
e aprendeu a usar o recurso de processamento em fluxo e tornar o processamento de 
seus textos muito mais rápido.

Por último, no capítulo quatro, você aprendeu a treinar e atualizar os modelos
estatísticos da spaCy, mais especificamente: o identificador de entidades.

Você aprendeu algumas dicas e truques para criar dados de treinamento e como
definir seu esquema de rótulação para obter melhores resultados.

---

# Mais coisas para você fazer com a spaCy (1)

- [Treinar e atualizar](https://spacy.io/usage/training) outros componentes do fluxo 
  de processamento (pipeline)
  - Tagueador de classes gramaticas
  - Analizador sintático
  - Classificador de textos

Notes: Mas é claro que há muito mais coisa que a spaCy consegue fazer que não está
neste curso.

Embora nosso foco neste curso tenha sido no identificador de entidades, você também
pode treinar e atualizar outros componentes do fluxo de processamento, como o
tagueador de classes gramaticais e o analisador sintático.

Outro componente poderoso do fluxo de processamento é o classificador de textos,
que pode aprender a prever rótulos que são aplicados ao texto como um todo. Ele
não está incluso nos modelos pré-treinados, mas você pode adicioná-lo a um 
modelo existente e treiná-lo com seus próprios dados.

---

# Mais coisas para você fazer com a spaCy (2)

- [Personalizar o toquenizador](https://spacy.io/usage/linguistic-features#tokenization)
  - Adicionar regras e exceções para particionar as frases de maneira diferente.
- [Adicionar ou melhorar o suporte para outros idiomas](https://spacy.io/usage/adding-languages)
  - 60+ idiomas atualmente
  - Muito espaço para melhoria e muitos idiomas para serem adicionados.
  - Permite o treinamento de outros idiomas. 

Notes: Neste curso, nós basicamente aceitamos o algoritmo padrão de toquenização
como ele está. Mas isso não é obrigatório!

A spaCy permite que você personalize as regras utilizadas para decidir onde as
frases devem ser particionadas.

Você também pode adicionar ou melhorar o suporte para outros idiomas.

Enquanto a spaCy atualmente já suporta toquenizações diferentes de acordo com o 
idioma, há muitas oportunidades de melhoria.

Suporte à toquenização de um novo idioma é o primeiro passo para treinar seu 
modelo estatístico.

---

# Visite o website para mais informações e documentações!

<img src="/website.png" alt="Laptop com o site spacy.io" width="50%" />

👉 [spacy.io](https://spacy.io)

Notes: Para mais exemplos, tutoriais e a documentação detalhada da API, visite o site
da biblioteca spaCy.
---

# Muito obrigada e nos vemos em breve! 👋

Notes: Muito obrigada por fazer este curso! Espero que você tenha se divertido, e estou
muito animada para conhecer as coisas legais que você construir usando a spaCy.

