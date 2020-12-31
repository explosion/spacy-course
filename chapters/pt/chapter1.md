---
title: 'Capítulo 1: Selecionando palavras, frases, nomes e alguns conceitos'
description:
  "Neste capítulo vamos apresentar os conceitos básicos de processamento de texto utilizanda spaCy.
  Você vai aprender sobre as estruturas de dados, como trabalhar com modelos estatísticos e como
  usá-los para prever anotações linguísticas do seu texto."
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introdução a spaCy" type="slides">

<slides source="chapter1_01_introduction-to-spacy">
</slides>

</exercise>

<exercise id="2" title="Primeiros passos">

Vamos começar colocando a mão na massa! Neste exercício você fará
experimentos com alguns dos mais de 55 [idiomas disponíveis](https://spacy.io/usage/models#languages).

### Parte 1: Inglês

- Faça a importação da classe `English` da biblioteca `spacy.lang.en` e crie um objeto `nlp`.
- Crie uma variável `doc` e imprima o seu conteúdo.

<codeblock id="01_02_01"></codeblock>

### Parte 2: Alemão

- Faça a importação da classe `German` da biblioteca `spacy.lang.de` e crie um objeto `nlp`.
- Crie uma variável `doc` e imprima o seu conteúdo.

<codeblock id="01_02_02"></codeblock>

### Parte 3: Espanhol

- Faça a importação da classe `Spanish` da biblioteca `spacy.lang.es` e crie um objeto `nlp`.
- Crie uma variável `doc` e imprima o seu conteúdo.

<codeblock id="01_02_03"></codeblock>

</exercise>

<exercise id="3" title="Documentos, partições e tokens">

Quando você chama o objeto `nlp` passando uma string como parâmetro, a spaCy
faz a toquenização do texto e cria um objeto do tipo documento. Neste exercício, você
vai aprender mais sobre o documento `Doc`, assim como os objetos `Token` e
partição `Span`.

### Passo 1

- Faça a importação da classe `English` e crie um objeto `nlp`.
- Processe o texto e instancie um objeto `Doc` na variável `doc`.
- Selecione o primeiro token do objeto `Doc` e imprima seu texto `text`.

<codeblock id="01_03_01">

Você pode indexar um `Doc` da mesma maneira que você indexa uma lista em Python.
Por exemplo, `doc[4]` irá retornar o token com índice 4, que é o quinto token do texto.
Lembre-se que em Python o primeiro índice é 0 e não 1.

</codeblock>

### Passo 2

- Faça a importação da classe `English` e crie um objeto `nlp`.
- Processe o texto e instancie um objeto `Doc` na variável `doc`.
- Crie uma partição do `Doc` para os tokens "tree kangaroos" e
"tree kangaroos and narwhals".

<codeblock id="01_03_02">

Criar uma partição do `Doc` é semelhante a particionar uma lista em Python usando
a notação `:`. Lembre-se que essa indexação exclui o segundo índice, por exemplo:
`0:4` mapeia os tokens indexados em 0 até o 3, não incluindo o índice 4.

</codeblock>

</exercise>

<exercise id="4" title="Atributos léxicos">

Neste exemplo, você poderá usar os objetos `Doc` e `Token` combinados com
atributos léxicos para encontrar referências de porcentagem em seu texto. Você irá procurar
por dois elementos (tokens) sequenciais: um número e um sinal de porcentagem.

- Use o atributo `like_num` para identificar se algum token no documento
`doc` se assemelha a um número.
- Selecione o token _seguinte_ ao token atual no documento. O índice para o
próximo token no `doc` é `token.i + 1`.
- Verifique se o atributo `text` do próximo token é o sinal de porcentagem "%".

<codeblock id="01_04">

Para obter o token em uma determinada posição no texto, você pode indexar diretamente
a variável `doc`. Por exemplo, para obter o token na posição 5 escreva `doc[5]`.

</codeblock>

</exercise>

<exercise id="5" title="Modelos estatísticos" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="Biblioteca dos modelos" type="choice">

O que **NÃO** está incluído nos modelos que você pode carregar na spaCy?

<choice>
<opt text="Um arquivo com metadados do idioma, pipeline e licença.">

Todos modelos incluem um arquivo `meta.json` que apresenta o idioma, os nomes dos
componentes do pipeline de processamento que serão carregados e metadados
do modelo, como nome, versão, licença, fontes de dados, autor e acurácia (se disponível).

</opt>
<opt text="Pesos binários para efetuar as previsões estatísticas.">

Para fazer a previsão de anotações linguísticas como o tagueamento de classes
gramaticais, termos sintáticos e reconhecimento de entidades, os modelos incluem
os pesos binários.

</opt>
<opt correct="true" text="Os dados nos quais o modelo foi treinado.">

Os modelos estatísticos permitem a generalização a partir de um conjunto de
exemplos de treinamento. Uma vez treinados, os modelos usam os pesos binários
para fazer as previsões. É por este motivo que não é necessário que os dados de
treinamento sejam incluídos nos modelos.

</opt>
<opt text="O vocabulário do modelo e seus códigos indexadores (hashes).">

As bibliotecas de modelos incluem um arquivo `strings.json` que armazena o mapeamento
do vocabulário para códigos indexadores (hash). Isso permite que a spaCy utilize apenas os
códigos hash e faça a consulta da palavra correspondente, se necessário.

</opt>
</choice>

</exercise>

<exercise id="7" title="Carregando os modelos">

Os modelos que estamos usando neste treinamento já vem pré-instalados. Para
saber mais informações sobre os modelos estatísticos e como instalá-los em seu
computador, consulte [essa documentação](https://spacy.io/usage/models).

- Utilize `spacy.load` para carregar o modelo pequeno da língua inglesa `"en_core_web_sm"`.
- Processe o texto e imprima o texto do documento.

<codeblock id="01_07">

Para carregar um modelo, use `spacy.load` com o nome do modelo. Os nomes do
modelo variam de acordo com o idioma e os dados nos quais o modelo foi treinado,
por isso verifique se você está usando o nome correto do modelo.

</codeblock>

</exercise>

<exercise id="8" title="Prevendo anotações linguísticas">

Agora vamos experimentar um dos modelos pré-treinados da spaCy e
ver o resultado de sua previsão. Fique à vontade e experimente com seu
próprio texto! Use `spacy.explain` para saber o significado de um determinado
marcador. Por exemplo: `spacy.explain("PROPN")` ou `spacy.explain("GPE")`.


### Parte 1

- Processe o texto utilizando o objeto `nlp` e crie um `doc`.
- Para cada token, imprima seu texto, sua classe gramatical  `.pos_` e seu
 termo sintático `.dep_`

<codeblock id="01_08_01">

Para criar um `doc`, chame o objeto `nlp` e coloque o texto como parâmetro.
Observe que os atributos do token possuem o caractere "sublinhado" no final.

</codeblock>

### Parte 2

- Processe o texto utilizando o objeto `nlp` e crie um `doc`.
- Construa uma iteração em `doc.ents` e imprima os atributos texto e o
marcador `label_`.

<codeblock id="01_08_02">

Para criar um `doc`, chame o objeto `nlp` e coloque o texto como parâmetro.
Observe que os atributos do token possuem o caractere "sublinhado" no final.

</codeblock>

</exercise>

<exercise id="9" title="Prevendo Entidades em um contexto">

Os modelos são estatísticos e por isso não acertam 100% dos casos.  A acurácia
do modelo depende dos dados nos quais o modelo foi treinado e também dos
dados que você está processando. Vamos ver um exemplo:

 - Processe o texto utilizando o objeto `nlp`.
 - Construa uma iteração nas entidades e imprima o texto e o marcador (label) da entidade.
 - Note que o modelo não previu "iPhone X". Crie manualmente uma partição
 para esses tokens.

<codeblock id="01_09">

 - Para criar um `doc`, chame o objeto `nlp` e coloque o texto como parâmetro.
 As entidades reconhecidas estarão na propriedade `doc.ents`.
 - A forma mais fácil de criar um um objeto partição  (`Span`) é utilizar a notação
 indexada, por exemplo `doc[5:10]` para o token na posição 5 até a posição 10.
 Observe que o token na posição 10 não será incluído.

</codeblock>

</exercise>

<exercise id="10" title="Correspondência de texto baseada em regras" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="Usando o comparador Matcher">

Vamos agora testar o comparador de expressões  `Matcher` baseado em
regras. Você vai usar o exemplo do exercício anterior e escrever uma expressão
que faça a correspondência para a frase "iPhone X" no texto.

- Importe o `Matcher` de `spacy.matcher`.
- Inicialize o comparador com o objeto compartilhado `vocab`do `nlp`.
- Crie uma expressão que faça a correspondência dos valores em `"TEXT"` para dois tokens:
  `"iPhone"` e `"X"`.
- Use o método `matcher.add` e adicione essa expressão ao comparador.
- Chame o comparador passando como parâmetro o `doc` e armazene o resultado
  na variável `matches`.
- Itere nos resultados e selecione a partição de texto com o índice `start` até
`end`.


<codeblock id="01_11">

- O vocabulário compartilhado está disponível no atributo `nlp.vocab`.
- Uma expressão é composta por uma lista de dicionários cuja chave é o nome do
  atributo. Por exemplo:  `[{"TEXT": "Hello"}]` fará a correspondência do atributo
  texto (TEXT) para o texto exatamente igual a "Hello".
- Os atributos `start` e `end` de cada resultado da correspondência são os
  índices no `doc` da partição de texto equivalente. Para retornar o resultado da
  correspondência, basta criar uma partição no `doc` usando os indices `start` e `end`.

</codeblock>

</exercise>

<exercise id="12" title="Escrevendo expressões de correspondência">

Neste exercício, você vai escrever algumas expressões mais complexas de
correspondência, usando os atributos dos tokens e operadores.

### Parte 1

- Escreva **uma** expressão que corresponda às menções da versão IOS  _completa_:
  "iOS 7", "iOS 11" e "iOS 10".

<codeblock id="01_12_01">

- Para indicar a correspondência exata de um texto, você deve usar o atributo
`TEXT`. Por exemplo,  `{"TEXT": "Apple"}` fará a correspondência exata do
texto "Apple".
- Para indicar a correspondência de um token com números, use o atributo
`"IS_DIGIT"`, que retornará `True` se o token tiver somente caracteres numéricos.

</codeblock>

### Parte 2

- Escreva **uma** expressão que corresponda às variações de "download" (tokens
que tenham "download" como lema), seguido de um token da classe gramatical
substativo próprio `"PROPN"`.

<codeblock id="01_12_02">

- Para indicar um lema, use o atributo `"LEMMA"` como expressão para o token.
  Por exemplo, `{"LEMMA": "be"}` fará a correspondência para "is", "was" ou "being".
- Para encontrar substativos próprios, você deve fazer a correspondência dos
  tokens cujo atributo `"POS"` seja `"PROPN"`.

</codeblock>

### Part 3

- Escreva **uma** expressão que corresponda a adjetivos (`"ADJ"`) seguidos por um
  ou dois substantivos. (um substantivo obrigatório e um seguinte opcional).

<codeblock id="01_12_03">

- Para identificar adjetivos, procure por tokens cujo atributo `"POS"` seja `"ADJ"`.
  Para substantivos procure por `"NOUN"`.
- Operadores podem ser adicionados à expressão utilizando a chave `"OP"`.
  Por exemplo: `"OP": "?"` para comparar zero ou uma vez.

</codeblock>

</exercise>
