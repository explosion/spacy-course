---
title: 'Chapter 2: Análise da dados em larga escala usando a biblioteca spaCy'
description:
  "Neste capítulo você desenvolverá novas habilidades ao extrair informações
  específicas de um grande volume de texto. Você vai aprender a otimizar o uso
  das estruturas de dados da spaCy e como criar estratégias combinadas de estatística
  e baseadas em regras para efetuar análises de textos de maneira eficiente."
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Estruturas de Dados (1)" type="slides">

<slides source="chapter2_01_data-structures-1">
</slides>

</exercise>

<exercise id="2" title="Strings e hashes">

### Parte 1

- Consulte a string "cat" em `nlp.vocab.strings` para obter seu código indexador (hash).
- Consulte o código indexador (hash) para obter a string novamente.

<codeblock id="02_02_01">

- Você pode acessar `nlp.vocab.strings` de maneira semelhante a dicionários
  em Python. Por exemplo, `nlp.vocab.strings["unicorn"]` retornará o código
  hash e ao fazer a consulta do hash irá retornar a string  `"unicorn"`.

</codeblock>

### Parte 2

- Consulte a marcador "PERSON" em `nlp.vocab.strings` para obter o código hash.
- Consulte o código hash para obter a string de volta.

<codeblock id="02_02_02">

- Você pode acessar `nlp.vocab.strings` de maneira semelhante a dicionários
  em Python. Por exemplo, `nlp.vocab.strings["unicorn"]` retornará o código
  hash e ao fazer a consulta do hash irá retornar a string  `"unicorn"`.

</codeblock>

</exercise>

<exercise id="3" title="Vocabulários, códigos hash e lexemas">

Por que o código abaixo dá erro?

```python
import spacy

# Criar um objeto do idioma inglês e um objeto do idioma alemão
nlp = English()
nlp_de = German()

# Consultar o código hash da palavra 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Consultar o código hash de "Bowie" no vocabulário
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='A string <code>"Bowie"</code> não pertence ao vocubulário alemão, por isso o código hash não pode ser mapeado para uma string.'>

Códigos hash não pode ser revertidos. Para prevenir este problema, adicione a
palavra ao vocabulário processando um texto ou consultando a palavra, ou use
o mesmo vocabulário para mapear o código hash de volta para a palavra.

</opt>

<opt text='<code>"Bowie"</code> não é uma palavra regular do Inglês ou Alemão, portanto ela não pode ser consultada.'>

Qualquer palavra pode ser mapeada para um código hash.

</opt>

<opt text="<code>nlp_de</code> não é um nome válido. O vocabulário só pode ser compartilhado se o objeto <code>nlp</code> tiver o mesmo nome.">

O nome da variável `nlp` é apenas uma convenção. Se no código fosse feita a atribuição
da variável `nlp` ao invés de `nlp_de`, ele teria sobrescrito a variável `nlp` existente
e o seu vocabulário.

</opt>

</choice>

</exercise>

<exercise id="4" title="Estruturas de Dados (2)" type="slides">

<slides source="chapter2_02_data-structures-2">
</slides>

</exercise>

<exercise id="5" title="Criando um objeto Doc">

Vamos criar objetos `Doc` a partir do zero!

### Parte 1

- Importe a classe `Doc` de `spacy.tokens`.
- Crie um `Doc` a partir das palavras `words` e espaçamento `spaces`. Não se esqueça
 de passar o vocabulário como argumento!

<codeblock id="02_05_01">

A classe `Doc` tem 3 argumentos: o vocabulário compartilhado, geralmente
`nlp.vocab`, a lista de palavras `words` e espaçamento `spaces` formado por valores
booleanos que indicam se a palavra é ou não seguida de um espaço em branco.

</codeblock>

### Parte 2

- Importe a classe `Doc` de `spacy.tokens`.
- Crie um `Doc` a partir das palavras `words` e espaçamento `spaces`. Não se esqueça
 de passar o vocabulário como argumento!

<codeblock id="02_05_02">

Observe cada palavra no texto desejado e verifique se ela é seguida de um
espaço. Se sim, o valor em `spaces` deve ser `True`. Se não, deve ser `False`.

</codeblock>

### Parte 3

- Importe a classe `Doc` de `spacy.tokens`.
- Complete os valores de  `words` e `spaces` para que o resultado seja o texto
desejado. Em seguida crie o `doc`.

<codeblock id="02_05_03">

Preste atenção nos tokens. Para entender como a spaCy toqueniza uma string, você
pode tentar imprimir os tokens de `nlp("Oh, really?!")`.

</codeblock>

</exercise>

<exercise id="6" title="Docs, partições Span e Entidades a partir do zero">

Neste exercício você criará os objetos `Doc` e `Span` manualmente e
atualizará as Entidades Nomeadas (named entities), da mesma maneira que
a spaCy faz nos bastidores. Um objeto `nlp` deve ser previamente criado.

- Importe as classes `Doc` e `Span` de `spacy.tokens`.
- Use a classe `Doc` para criar diretamente um `doc` a partir das palavras e
espaçamento.
- Crie uma partição `Span` para "David Bowie" a partir do `doc` e atribua a ela
o marcador  `"PERSON"`.
- Sobrescreva o `doc.ents` com uma lista contendo uma entidade: a partição
`span` com "David Bowie"


<codeblock id="02_06">

- O `Doc` é inicializado com três parâmetros: o vocabulário compartilhado,
  por exemplo: `nlp.vocab`, uma lista de palavras e uma lista de valores
  booleanos que indicam se uma palavra é seguida de um espaço em branco.
- A classe `Span` tem dois parâmetros: a referência ao `doc`, os índices do
  token inicial e do token final e opcionalmente um marcador.
- A propriedade `doc.ents` é sobrescrevível, e por isso você pode atribuir a ela
  qualquer objeto iterável do tipo `Span`.


</codeblock>

</exercise>

<exercise id="7" title="Melhores práticas em estruturas de dados">

No exemplo abaixo, o texto será analizado e todos os substantivos próprios
serão selecionados.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Seleciona os textos dos tokens e os marcadores com as classes gramaticais
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Verifica se o token atual é um substantivo próprio
    if pos == "PROPN":
        # Verifica se o próximo token é um verbo
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### Parte 1

Por que esse código não é eficiente?

<choice>

<opt text="O token em <code>result</code> deve ser convertido de volta para um objeto <code>Token</code>. Isso permitirá seu reuso na spaCy.">

Não é necessário converter string para objetos `Token`. Evite converter tokens
para strings se você ainda precisar acessar seus atributos e relações.

</opt>

<opt correct="true" text="São utilizadas listas de strings ao invés de atributos nativos dos tokens. Isso é normalmente menos eficiente, e não captura relações mais complexas entre as palavras.">

Sempre converta um resultado para string o mais tarde possível, e tente sempre
usar atributos nativos para manter a consistência da informação.

</opt>

<opt text='O atributo <code>pos_</code> não é o correto para extrair substantivos próprios. Você deve utilizar  <code>tag_</code> e os marcadores   <code>"NNP"</code> e <code>"NNS"</code>.'>

O atributo `.pos_` retorna a classe gramatical genérica enquanto `"PROPN"` é a forma correta
de verificar se trata-se de um substantivo próprio.

</opt>

</choice>

### Parte 2

- Rescreva o código utilizando diretamente os atributos nativos dos tokens
  ao invés de criar uma lista de `token_texts` e `pos_tags`.
- Crie um loop (laço) e para cada `token` no `doc` verifique o atributo
  `token.pos_`.
- Use `doc[token.i + 1]` para referenciar o próximo token e verifique seu
  atributo `.pos_`.

<codeblock id="02_07">

- Não é necessário gerar uma lista de strings antecipadamente: remova
  `token_texts` e `pos_tags`.
- Ao invés de iterar em `pos_tags`, crie um loop (laço) e para cada `token`
  em `doc`, verifique o atributo `token.pos_`.
- Para verificar se o próximo token é um verbo, use: `doc[token.i + 1].pos_`.


</codeblock>

</exercise>

<exercise id="8" title="Vetores das palavras e similaridade semântica" type="slides">

<slides source="chapter2_03_word-vectors-similarity">
</slides>

</exercise>

<exercise id="9" title="Inspeção dos vetores das palavras">

Neste exercício vamos usar um [fluxo de processamento do Inglês maior](https://spacy.io/models/en) que inclui
cerca de 20.000 vetores das palavras. Esse pacote do fluxo (pipeline) de processamento já está instalado.

- Carregue o fluxo (pipeline) de processamento médio `"en_core_web_md"`com seus vetores das palavras.
- Imprima o vetor para `"bananas"` usando o atributo `token.vector`.

<codeblock id="02_09">

- Para carregar um fluxo (pipeline) de processamento, use `spacy.load` passando uma string
com o nome do modelo.
- Para acessar um token no doc, você pode indexá-lo. Por exemplo: `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Comparando similaridades">

Neste exercício, você utilizará o método `similarity` para comparar objetos do
tipo `Doc`, `Token` and `Span` e obter o sua pontuação (score).

### Parte 1

- Use o método `doc.similarity` para comparar `doc1` e `doc2` e imprima o
  resultado.

<codeblock id="02_10_01">

- O método `doc.similarity` tem um argumento: o outro objeto para ser comparado
ao objeto atual.

</codeblock>

### Parte 2

- Use o método `token.similarity` para comparar `token1` e `token2` e imprima
  o resultado.

<codeblock id="02_10_02">

- O método `token.similarity` tem um argumento: o outro objeto para ser comparado
  ao objeto atual.

</codeblock>

### Parte 3

- Crie partições para "great restaurant" e "really nice bar".
- Use `span.similarity` para comparar e imprima o resultado.

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="Combinando predições e regras" type="slides">

<slides source="chapter2_04_models-rules">
</slides>

</exercise>

<exercise id="12" title="Depurando expressões (padrões) (1)">

Por que essa expressão não corresponde aos tokens "Silicon Valley" no `doc`?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

<choice>

<opt text='Os tokens "Silicon" e "Valley" não são minúsculos, portanto o atributo <code>"LOWER"</code> não terá correspondência.'>

O atributo `"LOWER"` na expressão refere-se a tokens na _forma minúscula_ que
corresponderão a um valor. Então a expressão `{"LOWER": "valley"}` corresponderá aos tokens
"Valley", "VALLEY", "valley" etc.

</opt>

<opt correct="true" text='O toquenizador não cria tokens para espaço em branco, portanto não existe token com o valor <code>" "</code> entre as palavras.'>

O toquenizador automaticamente retira os espaços em branco entre as palavras, e cada
dicionário na expressão deve ser um token.


</opt>

<opt text='Está faltando o operador <code>"OP"</code> que indica que os tokens devem corresponder somente uma vez.'>

Por padrão (default) os tokens em uma expressão irão corresponder somente uma vez.
Operadores são necessários para alterar esse comportamento padrão, como por
exemplo, corresponder uma ou mais vezes.

</opt>

</choice>

</exercise>

<exercise id="13" title="Depurando expressões (padrões) (2)">

As expressões neste exercício contêm erros e não haverá correspondência com o texto.
Você consegue corrigí-las? Se tiver dificuldade, tente imprimir os tokens do `doc`
para entender como o texto será quebrado e ajuste a expressão de forma que cada
dicionário represente um token.

- Edite `pattern1` de forma que ele faça a correspondência de todas as combinações
  de maiúscula e minúsculas de `"Amazon"` seguido de um substantivo próprio
  iniciado com letra maiúscula.

- Edite `pattern2` de forma que ele faça a correspondência de todas as combinações
  maiúsculas e minúsculas de `"ad-free"`, seguido de um substantivo.

<codeblock id="02_13">

- Tente processar os textos que devem fazer a correspondência utilizando o objeto
  `nlp` da seguinte forma: `[token.text for token in nlp("ad-free viewing")]`.
- Inspecione os tokens e certique-se que cada dicionário na expressão descreva
  corretamtente o token desejado.

</codeblock>

</exercise>

<exercise id="14" title="Correspondência eficiente de frases">

Muitas vezes é mais eficiente fazer a correspondência exata dos textos ao invés
de escrever expressões descrevendo os tokens individualmente. Esso é o caso
de categorias finitas, como por exemplo, lista dos países do mundo. Nós já temos
uma lista de países, então vamos usá-la como base para o nosso roteiro. A lista
com os nomes está disponível na variável `COUNTRIES`.

- Importe o `PhraseMatcher`, inicializando-o com o vocabulário compartilhado
  `vocab` com a variável `matcher`.
- Adicione a expressão e chame o comparador matcher no `doc`.

<codeblock id="02_14">

O vocabulário compartilhado `vocab` está disponível em `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Extraindo países e relacionamentos">

No exercício anterior, você escreveu um roteiro usando o `PhraseMatcher`
para localizar nomes de países no texto. Vamos usar esse comparador em
um texto maior, fazer a análise sintática e atualizar as entidades do documento
com os países encontrados.

- Itere nos resultados do comparador e crie uma partição `Span`
  com o marcador `"GPE"` (entidade geopolítica).
 - Sobrescreva `doc.ents` com as entidades encontradas.
 - Identifique o token inicial da partição dos resultados encontrados.
 - Imprima o texto da partição a partir do token inicial.

<codeblock id="02_15">

- Lembre-se que o texto está disponível na variável `text`.
- A referência ao token está no atributo `span.root`. O início do token
  está no atributo `token.head`.

</codeblock>

</exercise>
