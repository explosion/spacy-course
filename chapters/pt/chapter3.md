---
title: 'Chapter 3: Fluxos de processamento (pipelines)'
description:
  "Neste capítulo você conhecer melhor os fluxos de processamento
  (pipelines) da spaCy. Você entenderá o que acontece nos bastidores
  quando você processa um texto. Vai aprender a escrever seus próprios
  componentes e adicioná-los ao fluxo, e também a usar atributos customizados
  para adicionar metadados próprios aos seus documentos, partições e tokens."
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Fluxos de processamento (pipelines)" type="slides">

<slides source="chapter3_01_processing-pipelines">
</slides>

</exercise>

<exercise id="2" title="O que acontece quando você usa nlp()?">

O que a spaCy faz quando você usa `nlp` em uma sequência de texto?

```python
doc = nlp("This is a sentence.")
```

<choice>

<opt text="Executa o tagueador (tagger), o analisador (parser), o identificador de entidades e em seguida o toquenizador (tokenizer).">

O toquenizador sempre é executado _antes_ de qualquer componente do fluxo, pois
ele é responsável por transformar uma string de texto em um objeto `Doc`. O fluxo
de processamento (pipeline) não é obrigatoriamente composto por um tagueador (tagger),
um analisador (parser) e um identificador de entidades.

</opt>

<opt text="Toqueniza o texto e aplica os componentes do fluxo (pipeline) sequencialmente." correct="true">

O toquenizador transforma uma string de texto em um objeto `Doc`. a spaCy
então aplica cada componente do fluxo de processamento (pipeline) ao documento,
sequencialmente.

</opt>

<opt text="Conecta ao servidor da spaCy para processar o texto e retorna o resultados.">

a spaCy processa tudo localmente e não se conecta a nenhum servidor externo.

</opt>

<opt text="Inicializa o idioma, adiciona o fluxo de processamento (pipeline) e carrega os pesos binários dos modelos.">

Quando você usa `spacy.load()` para carregar um modelo, a spaCy irá inicializar o
idioma, adicionar o fluxo de processamento (pipeline) e carregar os pesos binários do modelo.
Quando você _usar_ o objeto `nlp` em um texto, o modelo já estará carregado.

</opt>

</exercise>

<exercise id="3" title="Examinando o fluxo de processamento (pipeline)">

Vamos examinar o fluxo de processamento do modelo pequeno do idioma inglês!

- Carregue o modelo `en_core_web_sm` e crie um objeto `nlp`.
- Imprima o nome dos componentes do fluxo utilizando `nlp.pipe_names`.
- Imprima as informações das tuplas `(name, component)` usando `nlp.pipeline`.

<codeblock id="03_03">

A lista de componentes do fluxo está disponível no atributo `nlp.pipe_names`. A
lista completa dos componentes na forma de tuplas `(name, component)` está
disponível em `nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="Customizando os componentes de um fluxo (pipeline)" type="slides">

<slides source="chapter3_02_custom-pipeline-components">
</slides>

</exercise>

<exercise id="5" title="Casos de uso de componentes customizados">

Quais desses problemas pode ser solucionado utilizando um componente customizado?

1. Atualizar um modelo pré-treinado e melhorar suas predições.
2. Calcular alguns valores utilizando os tokens e seus atributos.
3. Adicionar entidades nomeadas baseado em um dicionário, por exemplo.
4. Implementar suporte a um idioma adicional.

<choice>

<opt text="1 and 2.">

Componentes customizados podem apenas alterar o objeto `Doc` e não podem ser usados
para atualizar pesos ou outros componentes diretamente.

</opt>

<opt text="1 and 3.">

Componentes customizados podem apenas alterar o objeto `Doc` e não podem ser usados
para atualizar pesos ou outros componentes diretamente.

</opt>

<opt text="1 and 4.">

Componentes customizados podem apenas alterar o objeto `Doc` e não podem ser usados
para atualizar pesos ou outros componentes diretamente. Eles são adicionados ao fluxo
de processamento após o idioma ser carregado e depois da toquenização, portanto não
são adequados para adicionar novos idiomas.

</opt>

<opt text="2 and 3." correct="true">

Componentes customizados são ótimos para adicionar informações customizadas aos
documentos, tokens e partições e também para customizar as entidades `doc.ents`.
</opt>

<opt text="2 and 4.">

Componentes customizados são adicionados ao fluxo de processamento após o idioma
ser carregado e depois da toquenização, portanto não são adequados para adicionar
novos idiomas.

</opt>

<opt text="3 and 4.">

Componentes customizados são adicionados ao fluxo de processamento após o idioma
ser carregado e depois da toquenização, portanto não são adequados para adicionar
novos idiomas.

</opt>

</choice>

</exercise>

<exercise id="6" title="Componentes simples">

Este exemplo mostra um componente customizado que imprime o número de tokens
em um documento. Você consegue completar o código?

- Complete a função para calcular o tamanho do objeto `doc`.
- Adicione o `length_component` ao fluxo de processamento como o **primeiro**
  componente.
- Experimente o novo fluxo e processe qualquer texto com o objeto `nlp`. Por
  exemplo: "This is a sentence.".

<codeblock id="03_06">

- Para obter o tamanho de um objeto `Doc`, você pode usar a função `len()` do Python.
- Use o método `nlp.add_pipe` para adicionar um componente ao fluxo. Lembre-se de
  definir o argumento `first` como `True` para garantir que ele seja adicionado
  antes do processamento dos outros componentes.
- Para processar um texto, chame `nlp` e passe o texto como argumento.

</codeblock>

</exercise>

<exercise id="7" title="Componentes complexos">

Neste exercício você escreverá um componente customizado que usará o
`PhraseMatcher` para identificar nomes de animais no documento e adicionar as partições
reconhecidas ao `doc.ents`. O `PhraseMatcher` será criado como a variável `matcher`.

- Defina o componente customizado e aplique o `matcher` ao `doc`.
- Crie uma partição `Span` para cada correspondência, atribua o marcador `"ANIMAL"`
  e sobrescreva `doc.ents` com as novas correspondências.
- Adicione o novo componente ao fluxo _após_ o componente `"ner"`.
- Processe o texto e imprima o texto e os marcadores das entidades em `doc.ents`.


<codeblock id="03_07">

- Observe que as correspondências são uma lista de tuplas `(match_id, start, end)`.
- A classe `Span` tem 4 argumentos: o `doc` pai, o índice inicial, o índice final e
  o marcador.
- Para adicionar um componente após o outro, use o argumento `after` em
  `nlp.add_pipe`.

</codeblock>

</exercise>

<exercise id="8" title="Propriedades extendidas" type="slides">

<slides source="chapter3_03_extension-attributes">
</slides>

</exercise>

<exercise id="9" title="Definindo propriedades extendidas (1)">

Vamos exercitar a criação de propriedades extendidas.

### Passo 1

- Use `Token.set_extension` para criar a propriedade `"is_country"` (default `False`).
- Atualize o valor para o token `"Spain"` e imprima os resultados para todos os tokens.

<codeblock id="03_09_01">

Observe que as propriedades extendidas estão disponíveis através da propriedade `._` .
Por exemplo: `doc._.has_color`.

</codeblock>

### Passo 2

- Use `Token.set_extension` para criar a propriedade `"reversed"` (com o argumento getter
  sendo a função `get_reversed`).
- Imprima o valor da nova propriedade para cada token.

<codeblock id="03_09_02">

- Observe que as propriedades extendidas estão disponíveis através da propriedade `._` .
  Por exemplo: `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Definindo propriedades extendidas (2)">

Vamos agora tentar definir propriedades mais complexas usando o argumento getter
e a extensão de métodos.

### Parte 1

- Complete a função `get_has_number`.
- Use `Doc.set_extension` para definir `"has_number"` (getter `get_has_number`)
  e imprima seu valor.

<codeblock id="03_10_01">

- Observe que as propriedades extendidas estão disponíveis através da propriedade `._` .
  Por exemplo: `doc._.has_color`.
- A função `get_has_number` deve retornar verdadeiro (True) se algum token do `doc`
  se parecer com um número (`token.like_num`).

</codeblock>

### Parte 2

- Use `Span.set_extension` para definir `"to_html"` (método `to_html`).
- Aplique em `doc[0:2]` com o parâmetro `"strong"`.

<codeblock id="03_10_02">

- Métodos extendidos podem ter um ou mais parâmetros. Por exemplo:
  `doc._.algum_metodo("parametro")`.
- O primeiro parâmetro a ser passado é sempre o objeto `Doc`, `Token`
  ou `Span`.

</codeblock>

</exercise>

<exercise id="11" title="Entidades e extensões">

Neste exercício você combinará propriedades extendidas personalizadas com as
previsões do modelo e criará um método extendido que retornará o endereço (URL)
de busca na Wikipedia se a partição for uma pessoa, organização ou localidade.

- Defina a função `get_wikipedia_url` que só retornará uma URL da Wikipedia
  caso o marcador da partição seja igual ao valor de uma lista de marcadores.
- Defina a propriedade extendida `"wikipedia_url"` para a partição `Span` com
  o atributo getter igual a `get_wikipedia_url`.
- Itere nas entidades do `doc` e imprima a URL da Wikipedia.

<codeblock id="03_11">

- Para obter o marcador (label) de uma partição span, use a propriedade `span.label_`.
  Este é o marcador previsto pelo identificador de entidades caso o texto seja uma
  entidade.
- Observe que as propriedades extendidas estão disponíveis através da propriedade `._`.
  Por exemplo: `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Componentes com extensões">

Propriedades extendidas podem ser poderosas quando combinadas com componentes
customizados do fluxo de processamento. Neste exercício, você escreverá um
componente do fluxo de processamento para identificar nomes de países e
definirá uma propriedade que retornará a capital do país, se houver.

Um comparador com todos os países deverá ser disponibilizado na variável
`matcher`. Um dicionário que mapeie os países e suas capitais deverá ser
disponibilizado na variável `CAPITALS`.

- Complete a função `countries_component` que defina um marcador `"GPE"`
  (geopolitical entity) para todas as correspondências.
- Adicione o componente ao fluxo de processamento.
- Defina uma propriedade extendida `"capital"` para a partição Span com o
  argumento getter como `get_capital`.
- Processe o texto e imprima o texto da entidade, o marcador (label) e a
  propriedade extendida capital para cada partição em `doc.ents`.

<codeblock id="03_12">

- A classe `Span` tem quatro argumentos: o `doc`, o índice iníciial `start` e o
  índice final `end` do token e o seu marcador `label`.
- Use o `PhraseMatcher` com argumento `doc`, que retornará uma lista de tuplas:
  `(match_id, start, end)`.
- Para definir uma nova propriedade extendida, use o método  `set_extension` na
  classe global (`Doc`, `Token` ou `Span`). Para definir o argumento getter, use o
  argumento `getter`.
- Observe que as propriedades extendidas estão disponíveis através da propriedade `._`.
  Por exemplo: `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Aumentando a escala e o desempenho" type="slides">

<slides source="chapter3_04_scaling-performance">
</slides>

</exercise>

<exercise id="14" title="Fluxos de processamento">

Neste exercício, você usará `nlp.pipe` para processar texto de maneira mais
eficiente. O objeto `nlp` já terá sido criado. Uma lista de tweets sobre uma rede
popular de lanchonetes americana está disponível na variável TEXTS`.

### Parte 1

- Reescreva o exemplo usando `nlp.pipe`. Ao invés de iterar os textos e processá-los,
  itere o objetos `doc` disponíveis através de `nlp.pipe`.

<codeblock id="03_14_01">

- A função `nlp.pipe` permite que você substitua as 2 primeiras linhas de comando por
apenas 1 linha.
- `nlp.pipe` recebe como argumento `TEXTS` e retorna objetos `doc` para você fazer a iteração.

</codeblock>

### Parte 2

- Reescreva o exemplo e use `nlp.pipe`. Não se esqueça de usar `list()` no resultado
  para transformá-lo em uma lista.

<codeblock id="03_14_02"></codeblock>

### Parte 3

- Reescreva o exemplo e use `nlp.pipe`. Não se esqueça de usar `list()` no resultado
  para transformá-lo em uma lista.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Processando dados em contextos">

Neste exercício você utilizará propriedades customizadas para adicionar metadados
de autor e livro para as citações.

Uma lista de exemplos `[text, context]` está disponível na variável `DATA`. Os
textos são citações de livros famosos, e o contexto são dicionários com as chaves
`"author"` e `"book"`.

- Use o método `set_extension` para definir as propriedades customizadas `"author"`
  e `"book"` no `Doc`, com o valor padrão (default) `None`.
- Processe os pares `[text, context]` em `DATA` usando `nlp.pipe` com o argumento
  `as_tuples=True`.
- Sobrescreva `doc._.book` e `doc._.author` com as respectivas informações passadas
  como contexto.

<codeblock id="03_15">

- O método `Doc.set_extension` tem dois parâmetros: uma string com o nome da
  propriedade, e os descritores default, getter, setter ou method indicando
  esses valores. Por exemplo: `default=True`.
- Se o argumento `as_tuples` for `True`, o método `nlp.pipe` receberá uma lista
  `(text, context)` e retornará as tuplas `(doc, context)`.

</codeblock>

</exercise>

<exercise id="16" title="Processamento seletivo (condicional)">

Neste exercício você usará os métodos `nlp.make_doc` e `nlp.disable_pipes` para
executar componentes específicos durante o processamento do texto.

### Parte 1

- Reescreva o código para apenas toquenizar o texto usando `nlp.make_doc`.

<codeblock id="03_16_01">

O método `nlp.make_doc` pode ser usado em um texto e retornará um objeto `Doc`,
de maneira similar à função `nlp`.

</codeblock>

### Parte 2

- Desabilite o tagueador (tagger) e o interpretador (parser) através do método
  `nlp.disable_pipes`.
- Processe o texto e imprima todas as entidades do `doc`.

<codeblock id="03_16_02">

O método `nlp.disable_pipes` pode receber diversos parâmetros: os nomes dos componentes
do fluxo de processamento que devem ser desabilitados.
Por exemplo: `nlp.disable_pipes("ner")` irá desabilitar o identificador de entidades nomeadas.

</codeblock>

</exercise>
