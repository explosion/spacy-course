---
type: slides
---

# Treinando e atualizando modelos

Notes: Bem-vindo ao capítulo final, que vai tratar de um dos aspectos mais
entusiasmantes do processamento de linguagem natural moderno: treinar seus modelos!

Nesta lição, você aprenderá sobre o treinamento e a atualização dos componentes
do fluxo de processamento e seus modelos de redes neurais da spaCy e os dados necessários para isso - com foco principal no identificador de entidades nomeadas.

---

# Por que atualizar o modelo?

- Resultados melhores para seu domínio específico
- Aprende esquemas de classificação adequados ao seu problema
- Essencial para classificação de textos
- Muito útil para reconhecimento de entidades nomeadas
- Menos crítico para tagueamento de classes gramaticas e análise sintática


Notes: Antes de entrarmos nos detalhes do _como_, vale a pena fazermos uma pergunta
para nós mesmos: Para que queremos atualizar um modelo com nossos próprios exemplos?
Por que não podemos simplesmente confiar nos fluxos (pipelines) de processamento que já foram treinados ?

Modelos estatísticos fazem previsões baseadas nos exemplos nos quais foram treinados.

Normalmente você poderá fazer um modelo com melhor acurácia ao apresentar exemplos
do seu próprio domínio.

Na maioria das vezes você também deseja categorizar os textos de acordo com o seu
problema, portanto o modelo precisa aprender isso também.

Esse passo é essencial para a classificação de textos. É muito útil para identificadores
de entidades e bem menos crítico para tagueamento de classes gramaticas e análise 
sintática.

---

# Como o treinamento funciona (1)

1. **Inicializa** os pesos do modelo com valores aleatórios 
2. **Prevê** alguns exemplos utilizando os pesos atuais 
3. **Compara** previsões com os resultados reais
4. **Calcula** como alterar os pesos para melhorar as previsões
5. **Atualiza** ligeiramente os pesos do modelo
6. Volta para 2.

Notes: A biblioteca spaCy oferece suporte para atualizar os modelos existentes com mais exemplos, e treinar novos modelos. Se não 
começarmos com um fluxo de processamento (pipeline) treinado, nós inicialmente inicializamos os pesos com valores aleatórios.

Em seguida, a spaCy chama `nlp.update`, que fará a previsão de um lote de exemplos utilizando os pesos atuais.

O algoritmo então compara as previsões com os valores corretos, e decide como alterar
os pesos de forma a obter melhores previsões na próxima rodada.

Finalmente, fazemos uma pequena alteração nos pesos do modelo e seguimos para a 
próxima rodada de exemplos.

A biblioteca spaCy então continua o processamento, chamando `nlp.update` para cada lote de exemplos dos dados. Geralmente, durante o processo de treinamento, desejamos realizar
diversas passadas pelos dados e continuar com o treinamento até que o modelo deixe de ter resultados melhores.

---

# Como o treinamento funciona (2)

<img src="/training.png" alt="Diagram of the training process" />

- **Training data:** Dados de treinamento: exemplos e seus rótulos.
- **Text:** Texto: o texto de entrada que o modelo deve realizar a previsão.
- **Label:** Rótulo ou marcador: o resultado da previsão do modelo.
- **Gradient:** Gradiente: define como o modelo deve alterar seus pesos.

Notes: Esta é uma ilustração do processo:

Os dados de treinamento são os exemplos que desejamos utilizar para atualizar
o modelo.

O texto pode ser uma frase, parágrafo ou documento. Para melhores resultados,
ele deve ser similar aos textos que o modelo encontrará quando rodar suas
previsões.

O rótulo é o resultado que desejamos obter com a previsão do modelo. Pode ser a categoria
do texto, ou identificação de entidades e seus tipos.

O gradiente define como o modelo deve alterar seus pesos para reduzir o erro atual, 
que é calculado quando comparamos os dados previstos com os resultados esperados 
(reais).

Após o treinamento, podemos salvar o modelo atualizado e usá-lo em nossas aplicações.

---

# Exemplo: Treinando o identificador de entidades

- O identificador de entidades reconhece palavras e frases dentro de seu contexto
- Cada token pode pertencer a apenas uma entidade
- Os exemplos precisam apresentar um contexto

```python
doc = nlp("iPhone X is coming")
doc.ents = [Span(doc, 0, 2, label="GADGET")]
```

- Textos que não contenham entidades também são importantes

```python
doc = nlp("I need a new phone! Any tips?")
doc.ents = []
```

- **Objetivo:** ensinar o modelo a generalizar

Notes: Vamos dar uma olhada em um componente importante: o identificador de entidades.

O identificador de entidades recebe um documento e prevê frases e seus marcadores _dentro de um contexto_. Isso significa que os dados de treinamento necessitam incluir textos, as entidades e seus marcadores.

Entidades não podem ser sobrepostas, então cada token (ou palavra) só pode pertencer
a uma entidade.

A forma mais fácil de se fazer isso é apresentar ao modelo um texto e partições de entidades. A spaCy pode ser atualizada a partir de objetos `Doc` com entidades anotadas
como em `doc.ents`. Por exemplo: "iPhone X" é um "gadget" que começa no token 0 e termina no token 1.

É também muito importante que o modelo aprenda palavras que _não são_ entidades.

Neste caso, os marcadores do intervalo de caracter devem ser vazios.

Nosso objetivo é ensinar o modelo a reconhecer novas entidades em contextos
similares, mesmo que elas não estejam nos dados de treinamento.

---

# Os dados de treinamento

- Examplos daquilo que queremos que o modelo faça a previsão, em um dado contexto
- Para atualizar um **modelo existente**: poucas centenas ou poucos milhares de exemplos
- Para treinar uma **nova categoria**: alguns poucos milhares até milhões de exemplos
  - o modelo da biblioteca spaCy para o Inglês tem 2 milhões de palavras
- Normalmente é criado manualmente por anotadores humanos
- Pode ser semi-automatizada usando, por exemplo, o Comparador `Matcher`!

Notes: Os dados de treinamento dizem ao modelo aquilo que ele precisa prever. Pode
ser texto ou entidades que desejamos reconhecer, ou palavras e suas classes gramaticais ou qualquer outra coisa que o modelo deseje prever.

Para atualizar um modelo existente, podemos começar com algumas poucas centenas a
milhares de palavras.

Para treinar uma nova categoria, podemos precisar de até milhões de palavras.

O fluxo de processamento da biblioteca spaCy para o Inglês, por exemplo, foi treinado com 2 milhões de palavras anotadas com classes gramaticais, termos sintáticos e entidades nomeadas.

Os dados de treinamento normalmente são criados por humanos, que atribuiem marcadores
aos textos.

Isso representa muito trabalho, mas pode ter algumas etapas automatizadas, como por
exemplo, utilizando o Comparador `Matcher` da biblioteca spaCy.

---

# Treinando e validando dados

**Dados de treinamento** são usados para atualizar o modelo
**Dados de validação**
- são dados que o modelo não utilizou no treinamento
- utilizados para calcular a acurácia do modelo
- devem representar os dados que o modelo encontrará quando for utilizado para novas predições

Notes: Ao treinar seu modelo é muito importante poder validar a evolução do treinamento
e se o modelo está aprendendo corretamente. Isso é feito através da avaliação
das previsões do modelo em dados que _não foram utilizados_ durante o treinamento.
Portanto além dos dados de treinamento, você também precisa de dados de validação, 
também conhecidos como dados de desenvolvimento.

Os dados de validação são utilizados para calcular a acurácia do modelo.
Por exemplo, uma acurácia de 90% significa que o modelo previu corretamente
90% dos dados.

É também muito importante que os dados de validação tenham uma boa representatividade
dos dados reais. Caso contrário, a acurácia não será eficiente, uma vez que ela
não indicará o quão bom seu modelo _será de fato_.

---

# Gerando um _corpus_ de treinamento (1)

```python
import spacy
nlp = spacy.blank("en")
# Criar um Doc com as entidades
doc1 = nlp("iPhone X is coming")
doc1.ents = [Span(doc1, 0, 2, label="GADGET")]
# Criar outro Doc sem as entidades
doc2 = nlp("I need a new phone! Any tips?")
docs = [doc1, doc2]  # e assim por diante...
```

Notes: A biblioteca spaCy pode ser atualizada com dados novos através da 
atualização dos objetos `Doc`. Você já aprendeu sobre como criar objetos
`Doc` e `Span` no capítulo 2.

Neste exemplo, estamos criando dois objetos `Doc` para nosso corpus: um
que contém entidades e outro que não contém nenhuma entidade. Para definir
as entidades no `Doc`, podemos adicionar um `Span` ao `doc.ents`.

É claro que são necessários muitos exemplos para treinar o modelo de maneira
eficiente, permitindo que ele faça previsões de entidades similares no mesmo
contexto. Normalmente são utilizadas centenas ou até milhares de exemplos
representativos.

---

# Gerando um _corpus_ de treinamento (2)

- Divida os dados em duas porções:
  - **dados de treinamento:** utilizados para atualizar o modelo
  - **dados de validação:** utilizados para validar o modelo

```python
random.shuffle(docs)
train_docs = docs[:len(docs) // 2)]
dev_docs = docs[len(docs) // 2):]
```

Notes: Conforme mencionado anteriormente, não precisamos de dados apenas para treinar o 
modelo. Precisamos também de dados adicionais para avaliar a acurácia do modelo.
Geralmente os dados são embaralhados e divididos em dois conjuntos: uma
porção para o treinamento e outra para a validação. Neste exemplo estamos 
divindo os dados na proporção 50/50.
---

# Gerando um _corpus_ de treinamento (3)

- `DocBin`: é uma estrutura para armazenar e salvar objetos `Doc` de maneira eficiente.
- Pode ser salvo em um arquivo no formato binário.
- Arquivos binários são utilizados para o treinamento

```python
# Criar e salvar uma coleção de documentos para treinamento
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Criar e salvar uma coleção de documentos para validação
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
```

Notes: Tipicamente desejamos salvar os dados de treinamento e validação como
arquivos em disco, pois desta forma é possível carregá-los durante o processo
de treinamento.


O `DocBin` é uma estrutura que, de maneira bastante eficiente, armazena e
serializa os objetos `Doc`. Você pode instanciá-lo como uma lista de objetos
`Doc` e utilizar o método `to_disk` para salvá-lo em um arquivo binário. Normalmente
utilizamos o arquivo com a extensão `.spacy` para fácil identificação.

Comparativamente a outros algoritmos de serialização binária, como o `pickle`, o
`DocBin` é mais rápido e produz arquivos menores, já que ele apenas 
armazena o vocabulário compartilhado uma vez. Para mais informações, acesse a
[documentação](https://spacy.io/api/docbin).

---

# Dicas: Convertendo seus dados

- `spacy convert` permite a conversão de _corpora_ em vários formatos comuns
- Suporta `.conll`, `.conllu`, `.iob`  e o formato JSON da spaCy

```bash
$ python -m spacy convert ./train.gold.conll ./corpus
```

Notes: Em alguns casos, pode ser que você já tenha dados de treinamento e validação
em formatos comuns, como por exemplo: CoNLL ou IOB. O comando da spaCy `convert` 
automaticamente converte esses arquivos para o formato binário da biblioteca. Ele
também converte os arquivos no formato JSON que eram utilizados previamente na 
versão 2 da spaCy.

---

# Vamos praticar!

Notes: Agora é hora de começar o trabalho e preparar os dados de treinamento.
Vamos dar uma olhada em um exemplo e criar uma pequena base de dados para uma nova
entidade.
