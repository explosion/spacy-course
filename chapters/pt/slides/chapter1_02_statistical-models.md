---
type: slides
---

# Modelos estatísticos

Notes: Agora vamos adicionar alguns poderes ao objeto `nlp`!

Nesta lição você irá aprender sobre os modelos estatísticos da spaCy.

---

# O que são modelos estatísticos?

- Permitem que a spaCy faça previsões de atributos linguísticos _em contextos_.
  - Marcadores das classes gramaticais
  - Dependências sintáticas
  - Entidades nomeadas
- Treinados com exemplos de textos rotulados.
- Podem ser atualizados com mais exemplos para um ajuste fino das previsões.

Notes: Algumas das análises mais interessantes são aquelas específicas a um contexto. Por exemplo: se uma palavra é um verbo ou se uma palavra é o nome de uma pessoa.

Os modelos estatísticos permite que a spaCy faça previsões dentro de um contexto. Isso normalmente inclui marcadores de classes gramaticais, dependências sintáticas e entidades nomeadas.

Os modelos são treinados em grandes conjuntos de dados com textos de exemplos já rotulados.

Os modelos podem ser atualizados com mais exemplos para fazer um ajuste fino nas predições, como por exemplo, melhorar os resultados em um conjunto de dados específico.

---

# Pacotes dos modelos

<img src="/package.png" alt="Um pacote com o marcador en_core_web_sm" width="30%" align="right" />

```bash
$ python -m spacy download en_core_web_sm
```

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

- Pesos binários
- Vocabulário
- Metadados (idioma, fluxo de processamento)

Notes: a spaCy oferece vários pacotes de modelos que você pode baixar usando o comando `spacy download`. Por exemplo, o pacote "en_core_web_sm" é um modelo pequeno em inglês que tem todas as capacidades e foi treinado com texto da internet. 

O método `spacy.load` carrega o pacote de um modelo a partir do seu nome e retorna um objeto `nlp`.

O pacote contém os pesos binários que permitem que a spaCy faça as previsões.

Também inclui o vocabulário e metadados com informações sobre o idioma e como configurar o fluxo de processamento.

---

# Previsão dos marcadores de classe gramatical

```python
import spacy

# Carregar o modelo pequeno do Inglês
nlp = spacy.load("en_core_web_sm")

# Processar um texto
doc = nlp("She ate the pizza")

# Iterar nos tokens
for token in doc:
    # Imprimir o texto e a classe gramatical prevista
    print(token.text, token.pos_)
```

```out
She PRON
ate VERB
the DET
pizza NOUN
```

Notes: Vamos dar uma olhada nas previsões do modelo. Neste exemplo, estamos usando a spaCy para prever as classes gramaticais, que são os tipos de palavras em seu contexto.

Primeiramente, carregamos o modelo pequeno do Inglês no objeto `nlp`.

Em seguida, processamos o texto: "She ate the pizza".

Para cada token no doc, podemos imprimir o texto e o atributo `.pos_`, que é a classe gramatical prevista.

Na spaCy, atributos que retornam strings normalmente terminam com um underscore (sublinhado) e atributos sem o underscore retornam um inteiro.

Neste exemplo, o modelo previu corretamente "ate" como um verbo e "pizza" como um substantivo.

---

# Previsão de dependências sintáticas

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
She PRON nsubj ate
ate VERB ROOT ate
the DET det pizza
pizza NOUN dobj ate
```

Notes: Em adição à previsão de classes gramaticais, podemos prever como as palavras estão relacionadas. Por exemplo, se uma palavra é o sujeito ou o predicado de uma sentença.

O atributo `.dep_` retorna o marcador de dependência (ou termo sintático) previsto.

O atributo `.head` retorna o índice do token principal. Você pode pensar nele como o "pai" ao qual a palavra está conectada.

---

# Esquema dos marcadores de dependência ou termos sintáticos

<img src="/dep_example.png" alt="Visualização do esquema de dependências para 'She ate the pizza'" />

| Marcador  | Descrição            | Exemplo |
| --------- | -------------------- | ------- |
| **nsubj** | nominal subject (sujeito simples)    | She     |
| **dobj**  | direct object (objeto direto)      | pizza   |
| **det**   | determiner (adjunto adnominal) | the     |

Notes: Para descrever as dependências sintáticas, a spaCy usa um esquema com marcadores padronizados. Esse é um exemplo dos marcadores mais comuns:

O pronome (pronoun) "She" é um sujeito simples (nominal subject) relacionado com um verbo (verb), neste exemplo "ate".

O substantivo (noun) "pizza" é um objeto direto (direct object) relacionado ao verbo (verb) "ate". Ela é "eaten" pelo sujeito "she".

O adjunto adnominal (determiner) "the" está relacionado ao substantivo (noun) "pizza".

---

# Previsão de Entidades Nomeadas

<img src="/ner_example.png" alt="Visualização das entidades nomeadas em 'Apple is looking at buying U.K. startup for $1 billion'" width="80%" />

```python
# Processar um texto
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterar nas entidades previstas
for ent in doc.ents:
    # Imprimir o texto da entidade e seu marcador
    print(ent.text, ent.label_)
```

```out
Apple ORG
U.K. GPE
$1 billion MONEY
```

Notes: Entidades nomeadas são "objetos do mundo real" que possuem um nome. Por exemplo: uma pessoa, uma organização ou um país.

A propriedade `doc.ents` permite o acesso às entidades nomedas identificadas (previstas) pelo modelo.

Ela retorna um iterável de objetos do tipo `Span`, possibilitando o acesso ao texto e ao marcador através do atributo `.label_`.

Neste caso, o modelo previu corretamente "Apple" como uma organização, "U.K." como uma entidade geopolítica e "\$1 billion" como dinheiro.

---

# Dica: o método spacy.explain

Obtenha uma suscinta explicação dos marcadores mais comuns:

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: Uma dica: Para obter a definição dos marcadores mais comuns, você pode usar a função auxiliar `spacy.explain`.

Por exemplo, a sigla "GPE" para entidade geopolítica (geopolitical entity) não é muito intuitiva, mas o comando `spacy.explain` irá lhe explicar que se refere a países, cidades e estados.

O mesmo vale para marcadores de classes gramaticais e termos sintáticos.

---

# Vamos praticar!

Notes: Agora é a sua vez. Vamos dar uma olhada nos modelos estatísticos da spaCy e suas predições.
