---
type: slides
---

# Fluxos de processamento (pipelines)

Notes: Bem-vindo de volta ! Este capítulo é dedicado aos fluxos de processamento:
uma série de funções que são aplicadas sequencialmente no documento para
adicionar atributos como classes gramaticais,  marcadores sintáticos e
entidades nomeadas.

Nesta lição, você conhecerá os componentes do fluxo de processamento da spaCy
e o que acontece nos bastidores quando você chama nlp em um texto.

---

# O que acontece quando você usa nlp?

<img src="/pipeline.png" alt="Ilustracao do fluxo de processamento transformando um texto em um documento processado" width="90%" />

```python
doc = nlp("This is a sentence.")
```

Notes: Você já viu esse comando diversas vezes: passar um texto como 
argumento para o objeto `nlp` e receber um objeto `Doc`.

Mas o que o objeto `nlp` _de fato_ faz?

Inicialmente o toquenizador (tokenizer) é aplicado ao texto e ele é transformado em um 
objeto `Doc`. Em seguida, uma série de componentes são aplicados sequencialmente
no objeto `Doc`: o tagueador (tagger), o analisador (parser) e o identificador de 
entidades. Por fim, o documento processado é retornado, e você poderá trabalhar com 
ele.

---

# Componentes padrão do fluxo de processamento 

| Name        | Description                                              | Creates                                                   |
| ----------- | :------------------------------------------------------- | :-------------------------------------------------------- |
| **tagger**  | Tagueador de classses gramaticais (part-of-speech tagger)| `Token.tag`, `Token.pos`                                  |
| **parser**  | Analisador sintático (dependency parser)                 | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | Identificador de entidades (named entity recognizer)     | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | Classificador de texto (text classifier)                 | `Doc.cats`                                                |

Notes: Como padrão, a spaCy tem os seguintes componentes no fluxo de processamento:

O tagueador de classes gramaticais cria os atributos `token.tag` e `token.pos`.

O analisador sintático cria os atributos `token.dep` e `token.head` e também
é responsável por identificar sentenças e frases nominais, também conhecidas
como "pedaços de substantivos" (noun chunks).

O identificador de entidades adiciona entidades ao atributo `doc.ents`. Ele
também define o atributo de tipo de entidade aos tokens que indica se
um token é parte de uma entidade ou não.

E por último, o classificador de textos define os marcadores de categoria que
se aplicam ao texto como um todo, adicionando essa informação ao atributo `doc.cats`.

Devido ao fato que as categorias de texto são bastante específicas, o 
classificador de texto não está incluso como padrão em nenhum dos modelos 
pré-treinados. Mas você pode utilizá-lo em seu projeto.

---

# Nos bastidores

<img src="/package_meta.png" alt="Ilustracao de um pacote com nome en_core_web_sm, arquivos e pastas e metadados meta.json" />

- O Fluxo de processamento ocorre sequencialmente conforme definido no `meta.json` do modelo 
- Os componentes padrão usam dados binários para fazer as previsões

Notes: Todos os modelos que você pode importar na spaCy incluem vários arquivos,
dentre eles um `meta.json`.

O arquivo meta define o idioma e o fluxo de processamento. Ele indica quais componentes
precisam ser instanciados pela spaCy.

Os componentes internos que fazem as previsões necessitam de dados binários. Esses
dados estão inclusos no pacote do modelo e são carregados nos componentes quando
você carrega o modelo.

---

# Atributos do fluxo de processamento

- `nlp.pipe_names`: lista dos nomes dos componentes

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: lista de tuplas `(name, component)`

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: Para conferir os nomes dos componentes do fluxo de processamento
presentes no objeto atual, você pode usar o atributo `nlp.pipe_names`.

Para obter uma lista de tuplas com o nome do componente e sua função,
você pode usar o atributo `nlp.pipeline`.

A função de um componente é a função que é aplicada ao documento
para processá-lo e definir alguns atributos, como por exemplo, classe 
gramatical, marcadores sintáticos e de entidades.

---

# Vamos praticar!

Notes: Vamos agora dar uma olhada em alguns fluxos de processamento da spaCy !
