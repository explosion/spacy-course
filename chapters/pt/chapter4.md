---
title: 'Chapter 4: Treinando um modelo de rede neural'
description:
  "Neste capítulo, você aprenderá a atualizar os modelos estatísticos do
  spaCy de maneira a adequá-los aos seus casos de uso, como por exemplo,
  prever um novo tipo de entidade em textos de comentários. Você escreverá
  sua rotina de treinamento a partir do zero, e entenderá o ciclo de
  treinamento, bem como aprenderá algumas dicas sobre como ter sucesso
  em seus projetos de processamento de linguagem natural (PLN)."
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Treinando e atualizando os modelos" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="O propósito do treinamento">

Embora o spaCy já venha com modelos pré-treinados para prever anotações linguísticas,
na _maioria das vezes_ você desejará fazer um ajuste fino no modelo, adicionando
alguns exemplos específicos. Você conseguirá essa calibragem final após
adicionar mais dados rotulados e treinar o modelo.

O que o treinamento **não** faz?

<choice>

<opt text="Aumenta a acurácia do modelo em relação aos seus dados.">

Se um modelo pré-treinado não tiver uma boa performance em seus dados,
treiná-lo com mais exemplos é sempre uma boa solução.

</opt>

<opt text="Aprende novos esquemas de classificação.">

Através do treinamento é possível ensinar o modelo sobre novos marcadores,
entidades ou categorias de classificação.

</opt>

<opt text="Descobre padrões de dados não rotulados." correct="true">

Os componentes do spaCy são modelos _supervisionados_ baseados em anotações de
texto, o que quer dizer que eles aprendem a reproduzir exemplos já aprendidos
e não adivinhar novos marcadores a partir de dados sem tratamento.
</opt>

</choice>

</exercise>

<exercise id="3" title="Criando dados para treinamento (1)">

Através do `Matcher` do spaCy, um algoritmo baseado em regras, é possível criar
rapidamente dados de treinamento para modelos de entidades. Uma lista de frases
fica disponível através da variável `TEXTS`. Você pode imprimi-la para inspecionar
o conteúdo. Queremos encontrar todas as menções aos diferentes modelos de iPhone,
então vamos criar dados de treinamento para o modelo reconhecer esses exemplos como
`"GADGET"`.


- Escreva uma expressão para que dois tokens correspondam as palavras em minúsculas
  `"iphone"` e `"x"`.
- Escreva uma expressão com dois tokens : um token cujo formato em minúscula corresponda a
  `"iphone"` e o outro corresponda a um dígito usando o operador `"?"`.

<codeblock id="04_03">

- Para ter correspondência a um token no formato minúsculo, você pode usar o atributo
 `"LOWER"`. Por exemplo: `{"LOWER": "apple"}`.

- Para um token com um dígito, você pode usar o sinalizador `"IS_DIGIT"`. Por exemplo:
  `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Criando dados para treinamento (2)">

Vamos usar as expressões criadas no exercício anterior para alavancar um conjunto
de dados de treinamento. Uma lista de frases está disponível na variável `TEXTS`.

- Crie um objeto doc para cada frase usando `nlp.pipe`.
- Faça a correspondência ao doc usando o matcher e crie uma lista das partições
  com correspondência.
- Obtenha as tuplas `(caracter inicial, caracter final, marcador)` das partições.
- Formate cada exemplo como uma tupla com o texto e um dicionário, mapeando `"entities"`.
- Adicione o exemplo a `TRAINING_DATA` e imprima em seguida.

<codeblock id="04_04">

- Para encontrar correspondência, use o `matcher` com parâmetro `doc`.
- As correspondências encontradas são retornadas como tuplas `(match_id, start, end)`.
- Para adicionar um exemplo a lista de dados de treinamento, você pode usar:
  `TRAINING_DATA.append()`.

</codeblock>

</exercise>

<exercise id="5" title="O ciclo de treinamento" type="slides">

<slides source="chapter4_02_training-loop">
</slides>

</exercise>

<exercise id="6" title="Definindo o fluxo de processamento">

Neste exercício, você criará um fluxo de processamento para treinar o identificador
de entidades para reconhecer as entidades `"GADGET"` de uma frase, como por
exemplo: "iPhone X".

- Crie um modelo vazio do idioma `"en"`, usando o método `spacy.blank`.
- Crie um novo identificador de entidades usando `nlp.create_pipe` e o adicione
ao fluxo de processamento.
- Adicione o marcador `"GADGET"` ao identificador de entidades, usando o método
`add_label` do componente do fluxo.

<codeblock id="04_06">

- Para criar um identificador de entidades vazio, você pode usar `nlp.create_pipe`
  com o parâmetro "ner"`.
- Para adicionar um componente ao fluxo, use o método `nlp.add_pipe`.
- O método `add_label` é um método do componente identificador de entidades do
  fluxo de processamento que você armazenou na variável `ner`. Para adicionar
  um marcador a ele, use `ner.add_label` com o nome do marcador. Por exemplo:
  `ner.add_label("UM_NOME_DO_ROTULO")`.

</codeblock>

</exercise>

<exercise id="7" title="Construindo um ciclo de treinamento">

Vamos agora criar um ciclo de treinamento simples, a partir do zero!

O fluxo de processamento que você criou no exercício anterior está disponível
como um objeto `nlp`. Ele já contem um identificador de entidades com o marcador
adicionado: `"GADGET"`.

O pequeno conjunto de exemplos com marcadores que você também criou está disponível
como `TRAINING_DATA`. Para ver alguns exemplos você pode imprimi-los em seu
código.

- Use `nlp.begin_training` para criar um ciclo de treinamento com 10 iterações
  e embaralhe os dados de treinamento.
- Crie lotes (batches) de dados de treinamento usando `spacy.util.minibatch` e
  faça a iteração nos lotes.
- Converta as tuplas `(text, annotations)` do lote para listas de `texts` e
  `annotations`.
- Para cada lote (batch), use `nlp.update` para atualizar o modelo com os `texts`
  e `annotations`.


<codeblock id="04_07">

- Para iniciar o treinamento e reiniciar os pesos do modelo, use o método
  `nlp.begin_training()`
- Para dividir os dados de treinamento em lotes, use a função `spacy.util.minibatch`
  com parâmetro a lista de exemplos de treinamento.

</codeblock>

</exercise>

<exercise id="8" title="Explorando o modelo">

Vamos agora avaliar como o modelo se comporta com novos dados. Para agilizar,
já treinamos um modelo para o marcador `"GADGET"` com algumas frases. Aqui está
o resultado:

| Text                                                                                                              | Entities               |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple is slowing down the iPhone 8 and iPhone X - how to stop it                                                  | `(iPhone 8, iPhone X)` |
| I finally understand what the iPhone X 'notch' is for                                                             | `(iPhone X,)`          |
| Everything you need to know about the Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| Looking to compare iPad models? Here’s how the 2018 lineup stacks up                                              | `(iPad,)`              |
| The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple                         | `(iPhone 8, iPhone 8)` |
| what is the cheapest ipad, especially ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics | `(Samsung Galaxy,)`    |

De todas as entidades nos textos, **quantas o modelo acertou**?
Lembre-se que partições incompletas das entidades contabilizam como erros!
Dica: Conte o número de entidades no modelo que _deveriam_ ter sido identificadas.
Depois conte o número de entidades que _de fato_ foram identificadas e as divida
pelo número total de entidades.

<choice>

<opt text="45%">

Conte o número de entidades corretamente identificadas e as divida pelo número
total de entidades que o modelo _deveria_ ter identificado.
</opt>

<opt text="60%">

Conte o número de entidades corretamente identificadas e as divida pelo número
total de entidades que o modelo _deveria_ ter identificado.

</opt>

<opt text="70%" correct="true">

Na nossa base de teste, o modelo atingiu a acurácia de 70%.

</opt>

<opt text="90%">

Conte o número de entidades corretamente identificadas e as divida pelo número
total de entidades que o modelo _deveria_ ter identificado.

</opt>

</choice>

</exercise>

<exercise id="9" title="Melhores práticas de treinamento" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="10" title="Dados bons vs. dados ruins">

Aqui está um trecho de um conjunto de dados de treinamento rotulados
para a entidade `TOURIST_DESTINATION` em revisões de viajantes.

```python
TRAINING_DATA = [
    (
        "i went to amsterdem last year and the canals were beautiful",
        {"entities": [(10, 19, "TOURIST_DESTINATION")]},
    ),
    (
        "You should visit Paris once in your life, but the Eiffel Tower is kinda boring",
        {"entities": [(17, 22, "TOURIST_DESTINATION")]},
    ),
    ("There's also a Paris in Arkansas, lol", {"entities": []}),
    (
        "Berlin is perfect for summer holiday: lots of parks, great nightlife, cheap beer!",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
```

### Parte 1

Por que esses dados e seus marcadores são problemáticos?

<choice>

<opt text="É subjetivo definir se uma localidade é um destino turístico. Será muito difícil o modelo aprender desta maneira." correct="true">


Uma abordagem melhor seria identificar as entidades geopolíticas `"GPE"` ou
localidades `"LOCATION"` e em seguida utilizar um sistema baseado em regras para
determinar se a entidade é um destino turístico neste contexto. Por exemplo,
você poderia comparar esssas entidades identificadas com uma base de conhecimento
ou uma wiki sobre viagens.

</opt>

<opt text="Paris  deveria ter sido rotulada como um destino turístico para ser consistente. Senão o modelo irá se confundir.">

Embora seja possível que Paris, AK seja uma atração turística, este exemplo só
ressalta a subjetividade da definição dessa estratégia e como o processo de
rotulagem será complexo. Como resultado, a distinção desta entidade será bem difícil
para o modelo.

</opt>

<opt text="Palavras pouco frequentes ou digitadas erradas como 'amsterdem' não devem ser rotuladas como entidades.">

Palavras pouco frequentes ou digitadas erradas podem ser rotuladas como entidades.
Na verdade, ser capaz de predizer categorias em textos com erros baseando-se no
contexto do texto é uma das grandes vantagens dos modelos estatísticos preditivos.

</opt>

</choice>

### Parte 2

- Rescreva o `TRAINING_DATA` para usar apenas o marcador `"GPE"` (cidades, estados, países)
ao invés de `"TOURIST_DESTINATION"`.
- Não se esqueça de adicionar as tuplas à entidade `"GPE"` que não estavam identificadas
nos dados antigos.

<codeblock id="04_10">

- Para as partições que já estavam rotuladas, você só precisa alterar o marcador de
  `"TOURIST_DESTINATION"` para `"GPE"`.
- Uma frase contém uma cidade e um estado que não tinha sido rotulado. Para
  adicionar a partição da entidade, identifique a posição do início e do final
  da partição. Em seguida, adicione a tupla `(start, end, label)` à entidade.

</codeblock>

</exercise>

<exercise id="11" title="Treinando múltiplos marcadores">

Aqui está um pequeno exemplo de um conjunto de dados criado para treinar a entidade
`"WEBSITE"`. O conjunto de dados original contém algumas centenas de frases.
Neste exercício, você criará os marcadores manualmente. Na vida real, você provavelmente
irá automatizar este processo e utilizará uma ferramenta de anotação, como por exemplo:
[Brat](http://brat.nlplab.org/), uma solução de código aberto, ou
[Prodigy](https://prodi.gy), nossa ferramenta de anotação integrada ao spaCy.


### Parte 1

- Complete os espaços em branco para identificar a entidade `"WEBSITE"`. Você pode usar
  `len()` para contar a quantidade de caracteres.

<codeblock id="04_11_01">

- o início e fim de uma partição para uma entidade são ao localização no texto.
  Por exemplo, se uma entidade se iniciar na posição 5, significa que o início
  é `5`. Lembre-se que o fim é _exclusivo_, ou seja, `10` significa **até**
  o caracter 10.

</codeblock>

### Parte 2

Um modelo foi treinado com os dados que você acaba de rotular, com mais alguns
milhares de exemplos similares. Depois do treinamento, ele está performando muito
bem para `"WEBSITE"`, mas parece não estar mais reconhecendo a entidade `"PERSON"`.
O que pode estar acontecendo?

<choice>

<opt text='É muito difícil um modelo aprender a diferenciar várias categorias diferentes, como <code>"PERSON"</code> e <code>"WEBSITE"</code>.'>

É claro que é possível um modelo aprender a identificar diferentes categorias.
Por exemplo, o modelo pré-treinado do spaCy para a língua inglesa consegue
identificar pessoas, e também organizações e até percentuais.

</opt>

<opt text='Os dados de treinamento não incluíram exemplos de <code>"PERSON"</code>, portanto o modelo aprendeu que esse marcador é incorreto.' correct="true">

Se exemplos de entidades `"PERSON"`aparecerem nos dados de treinamento e não estiverem
rotuladas, o modelo aprenderá que essas entidades não deverm ser identificadas.
Similarmente, se exemplos da entidade **não** estiverem presentes nos dados de treinamento,
o modelo poderá \"esquecer\" e parar de identificá-la.

</opt>

<opt text="Os hiper-parâmetros precisam ser ajustados para que ambas entidades sejam identificadas.">

Embora os hiper-parâmetros influenciem a acurácia de um modelo, eles não são o problema fundamental
deste exemplo.

</opt>

</choice>

### Parte 3

- Atualize os dados de treinamento para incluir as anotações "PewDiePie" e
  "Alexis Ohanian" pra a entidade `"PERSON"`.

<codeblock id="04_11_02">

- Para adicionar mais entidades, adicione outra tupla `(start, end, label)` à lista.

</codeblock>

</exercise>

<exercise id="12" title="Finalizando..." type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
