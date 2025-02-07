---
title: 'Chapter 4: Treinando um modelo de rede neural'
description:
  "Neste capítulo, você aprenderá a atualizar os modelos estatísticos da
  spaCy de maneira a adequá-los aos seus casos de uso, como por exemplo,
  prever um novo tipo de entidade em textos de comentários. Você treinará
  seu próprio modelo a partir do zero, e entenderá o ciclo de
  treinamento, bem como aprenderá algumas dicas sobre como ter sucesso
  em seus projetos de processamento de linguagem natural (PLN).
  "
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Treinando e atualizando os modelos" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="Treinando e avaliando os dados">

Para treinar um modelo, tipicamente é necessário dados de treinamento e dados para
validação. Para que são utilizados os dados de validação?

<choice>

<opt text="Para fornecer exemplos de treinamento de reserva caso os dados de treinamento não forem suficientes.">

Durante o treinamento, o modelo só será atualizado com os dados de treinamento.
Os dados de validação são utilizados apenas para avaliar a qualidade do modelo, através
da comparação das predições feitas nesses dados (novos dados) com o resultado esperado. Isso então refletirá
no score de acurácia do modelo.

</opt>

<opt text="Para avaliar a previsão em novos exemplos e calcular a acurácia do modelo."  correct="true">

Os dados de validação são utilizados para avaliar o modelo, comparando a predição feita nesses dados
(novos dados) com o resultado esperado. Isso então refletirá no score de acurácia do modelo.

</opt>

<opt text="Para definir exemplos de treinamento sem anotações.">

Os dados de validação são utilizados para avaliar o modelo, comparando a predição feita nesses dados
(novos dados) com o resultado esperado. Isso então refletirá no score de acurácia do modelo.
</opt>

</choice>

</exercise>

<exercise id="3" title="Criando dados para treinamento (1)">

Através do `Matcher` da spaCy, que é um algoritmo baseado em regras, é possível criar
rapidamente dados de treinamento para modelos de entidades. Uma lista de frases
fica disponível através da variável `TEXTS`. Você pode imprimi-la para inspecionar
o conteúdo. Queremos encontrar todas as menções aos diferentes modelos de iPhone,
então vamos criar dados de treinamento para o modelo reconhecer esses exemplos como
`"GADGET"`.


- Escreva uma expressão para que dois tokens correspondam as palavras em minúsculas
  `"iphone"` e `"x"`.
- Escreva uma expressão com dois tokens: um token cujo formato em minúscula corresponda a
  `"iphone"` e o outro corresponda a um dígito usando o operador `"?"`.

<codeblock id="04_03">

- Para ter correspondência a um token no formato minúsculo, você pode usar o atributo
 `"LOWER"`. Por exemplo: `{"LOWER": "apple"}`.

- Para um token com um dígito, você pode usar o sinalizador `"IS_DIGIT"`. Por exemplo:
  `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Criando dados para treinamento (2)">

Após criar dados para o nosso `corpus`, precisamos salvá-los em um arquivo `.spacy`.
O código do exemplo anterior já está disponível.

- Instancie o `DocBin`com a lista de `docs`
- Salve o `DocBin` em um arquivo chamado `train.spacy`.

<codeblock id="04_04">

- Você pode inicializar o `DocBin` através do parâmetro `docs`, que pode receber uma lista de docs.
- O método `to_disk` do `DocBin` recebe um parâmetro: o caminho do arquivo para salvar os dados binários.
Certifique-se que o arquivo possua a extensão `.spacy`.

</codeblock>

</exercise>

<exercise id="5" title="Configurando e executando o treinamento" type="slides">

<slides source="chapter4_02_training-loop">
</slides>


</exercise>

<exercise id="6" title="As configurações de treinamento">

O arquivo `config.cfg` é a única fonte segura de informações para treinar um
fluxo (pipeline) de processamento com a biblioteca spaCy. Qual das alternativas
abaixo **não está correta** em relação ao arquivo de configuração?

<choice>

<opt text="Ele permite que você configure o processo de treinamento e o hyper-parâmetros.">

O arquivo de configuração inclui todas as configurações para o processo de treinamento, 
inclusive os hyper-parâmetros.

</opt>

<opt text="Ele facilita a reprodutibilidade do processo de treinamento.">

Uma vez que o arquivo de configuração inclui _todas_ as configurações e no processo não há 
nenhuma configuração padrão, o processo de treinamento poderá ser reproduzido baseando-se neste
arquivo, o que permite que outros possam roda os mesmos experimentos com exatamente as mesmas
configurações.

</opt>

<opt text="Ele cria um pacote python instalável contendo o seu fluxo de processamento." correct="true">

O arquivo de configuração inclui todas as configurações relacionadas ao treinamento e instruções de
como criar seu fluxo (pipeline) de processamento. Para criar um pacote python instalável, você pode
utilizar o comando `spacy package`.

</opt>

<opt text="Ele define os componentes do fluxo (pipeline) de processamento e suas configurações.">

O bloco `[components]` do arquivo de configuração inclui todos os componentes do fluxo (pipeline) de processamento e suas configurações, incluindo as implementações do modelo utilizado.

</opt>

</choice>

</exercise>

<exercise id="7" title="Gerando um arquivo de configuração">

O comando [`init config`](https://spacy.io/api/cli#init-config) gera automaticamente
um arquivo de configuração para o treinamento com as configurações padrão. Queremos 
treinar um identificador de entidades, portanto vamos gerar um arquivo de configuração
para apenas um componente do fluxo (pipeline) de processamento : `ner`. Uma vez que neste
curso estamos executando o comando em um ambiente Jupyter, vamos utilizar o prefixo `!`.
Se você estiver executando os comandos diretamente no seu terminal, a utilização do 
prefixo `!` não é necessária.

### Parte 1

- Use o comando da spaCy `init config` para gerar automaticamente um arquivo de 
configuração para o idioma Inglês.
- Salve a configuração em um arquivo `config.cfg`
- Use o parâmetro `--pipeline` para especificar o único componente do pipeline: `ner`.

<codeblock id="04_07_01">

- O parâmetro `--lang` define a classe do idioma, neste caso `en` para o Inglês.

</codeblock>

### Parte 2

Vamos dar uma olhada no arquivo de configuração que foi gerado. Você pode executar
o comando abaixo para imprimir a configuração no terminal e analisá-la.

<codeblock id="04_07_02"></codeblock>

</exercise>

<exercise id="8" title="Usando o comando de treinamento CLI">

Vamos usar o arquivo de configuração que geramos no exercício anterior e o 
corpus de treinamento que criamos para treinar um identificador de entidades!

O comando [`train`](https://spacy.io/api/cli#train) permite treinar um modelo a 
partir de um arquivo de configuração. O arquivo `config_gadget.cfg` está disponível
no diretório `exercises/pt`, bem como o arquivo `train_gadget.spacy` contendo os 
exemplos de treinamento, e o arquivo `dev_gadget.spacy` contendo os exemplos de
validação. Uma vez que neste curso estamos executando o comando em um ambiente Jupyter, 
vamos utilizar o prefixo `!`. Se você estiver executando os comandos diretamente no seu terminal, 
a utilização do prefixo `!` não é necessária.

Use o comando `train` com o arquivo `exercises/pt/config_gadget.cfg`. Salve o fluxo de 
processamento (pipeline) no diretório `output`. Passe os caminhos `exercises/pt/train_gadget.spacy`
e `exercises/pt/dev_gadget.spacy` como parâmetros.

<codeblock id="04_08">

O primeiro parâmetro de `spacy train` é o caminho para o arquivo de configuração.

</codeblock>

</exercise>

<exercise id="9" title="Explorando o modelo">

Vamos agora avaliar como o modelo se comporta com novos dados. Para agilizar,
já treinamos um fluxo (pipeline) de processamento para o marcador `"GADGET"` com algumas frases. Aqui está
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

<exercise id="10" title="Melhores práticas de treinamento" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="11" title="Dados bons vs. dados ruins">

Aqui está um trecho de um conjunto de dados de treinamento rotulados
para a entidade `TOURIST_DESTINATION` em revisões de viajantes.

```python
doc1 = nlp("i went to amsterdem last year and the canals were beautiful")
doc1.ents = [Span(doc1, 3, 4, label="TOURIST_DESTINATION")]
doc2 = nlp("You should visit Paris once, but the Eiffel Tower is kinda boring")
doc2.ents = [Span(doc2, 3, 4, label="TOURIST_DESTINATION")]
doc3 = nlp("There's also a Paris in Arkansas, lol")
doc3.ents = []
doc4 = nlp("Berlin is perfect for summer holiday: great nightlife and cheap beer!")
doc4.ents = [Span(doc4, 0, 1, label="TOURIST_DESTINATION")]
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

- Rescreva o `doc.ents` para usar apenas as partições do marcador `"GPE"` (cidades, estados, países)
ao invés de `"TOURIST_DESTINATION"`.
- Não se esqueça de adicionar as partições à entidade `"GPE"` que não estavam identificadas
nos dados antigos.

<codeblock id="04_11">

- Para as partições que já estavam rotuladas, você só precisa alterar o marcador de
  `"TOURIST_DESTINATION"` para `"GPE"`. 
- Uma frase contém uma cidade e um estado que não tinha sido rotulado. Para
  adicionar a partição da entidade, identifique a posição do início e do final
  da partição. Lembre-se que o índice do último token é _exclusivo_ ! Em seguida, 
  adicione uma nova partição `Span` em `doc.ents`.
  Fique de olho na tokenização! Veja os tokens que estão no `Doc` se você não estiver
  seguro.

</codeblock>

</exercise>

<exercise id="12" title="Treinando múltiplos marcadores">

Aqui está um pequeno exemplo de um conjunto de dados criado para treinar a entidade
`"WEBSITE"`. O conjunto de dados original contém algumas centenas de frases.
Neste exercício, você criará os marcadores manualmente. Na vida real, você provavelmente
irá automatizar este processo e utilizará uma ferramenta de anotação, como por exemplo:
[Brat](http://brat.nlplab.org/), uma solução de código aberto, ou
[Prodigy](https://prodi.gy), nossa ferramenta de anotação integrada à spaCy.

### Parte 1

- Complete os espaços em branco para identificar a entidade `"WEBSITE"` nos dados.

<codeblock id="04_12_01">

- Lembre-se que a indexação é  _exclusiva_ . Portanto se uma entidade se iniciar
na posição 2 e terminar na posição 3, ela terá o token inicial em `2` e o token
final em `4`.

</codeblock>

### Parte 2

Um modelo foi treinado com os dados que você acaba de rotular, com mais alguns
milhares de exemplos similares. Depois do treinamento, ele está performando muito
bem para `"WEBSITE"`, mas parece não estar mais reconhecendo a entidade `"PERSON"`.
O que pode estar acontecendo?

<choice>

<opt text='É muito difícil um modelo aprender a diferenciar várias categorias diferentes, como <code>"PERSON"</code> e <code>"WEBSITE"</code>.'>

É claro que é possível um modelo aprender a identificar diferentes categorias.
Por exemplo, o modelo pré-treinado da spaCy para a língua inglesa consegue
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

<codeblock id="04_12_02">

- Para adicionar mais entidades, adicione outra partição `Span` a `doc.ents`.
Lembre-se que o token final de uma partição é exclusivo. Portanto se uma entidade se iniciar
na posição 2 e terminar na posição 3, ela terá o token inicial em `2` e o token
final em `4`.

</codeblock>

</exercise>

<exercise id="13" title="Finalizando..." type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
