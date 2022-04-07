---
type: slides
---

# Comparador baseado em regras

Notes: Nesta lição, vamos dar uma olhada no Comparador (Matcher) da biblioteca spaCy, que permite a criação de regras para encontrar palavras e frases no texto.

---
 
# Por que usar o Comparador e não somente expressões regulares?

- Permite a comparação com objetos `Doc` e não apenas texto (strings)
- Permite a comparação com os tokens e seus atributos
- Utiliza a previsão de um modelo
- Exemplo: "duck" (verbo) vs. "duck" (substantivo)

Notes: Além de comparar com texto (strings), que é o caso das expressões regulares, o Comparador (Matcher) também analisa os objetos `Doc` e `Token`.

Ele é bem mais flexível: você pode fazer a comparação no texto mas também nos seus atributos léxicos.

Você pode até criar regras que usam previsões de um modelo.

Por exemplo, você pode procurar a palavra "duck" (em inglês) somente se for um verbo e não um substantivo.

---

# Expressões de correspondência

- Listas de dicionários, uma por token

- Corresponde exatamente ao texto de um token:
```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- Corresponde a atributos léxicos:
```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- Corresponde a qualquer atributo de um token:
```python
[{"LEMMA": "buy"}, {"POS": "NOUN"}]
```

Notes: As expressões de correspondência são listas de dicionários. Cada dicionário se relaciona a um token. As chaves são os nomes dos atributos dos tokens, mapeadas para os valores esperados.

Neste exemplo, estamos procurando por dois tokens com o texto: "iPhone" e "X".

Podemos fazer a correspondência de acordo com outros atributos dos tokens. Neste exemplo estamos procurando dois tokens cuja forma em letras minúsculas corresponda a "iphone" e "x".

Podemos até escrever expressões usando atributos previstos por um modelo. Neste exemplo estamos procurando um token cujo lema seja "buy" seguido de um substantivo. O lema é o formato base da palavra, então esta expressão terá correspondência com frases como "buying milk" ou "bought flowers".

---

# Usando o Comparador (Matcher) (1)

```python
import spacy

# Importar o Comparador (Matcher)
from spacy.matcher import Matcher

# Carregar o fluxo (pipeline) de processamento e criar um objeto nlp
nlp = spacy.load("en_core_web_sm")

# Inicializar o comparador com o vocabulário 
matcher = Matcher(nlp.vocab)

# Adicionar a expressão ao comparador
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Processar um texto
doc = nlp("Upcoming iPhone X release date leaked")

# Chamar o matcher no doc
matches = matcher(doc)
```

Notes: Para usar uma expressão, devemos importar o comparador `spacy.matcher`.

É necessário carregar um fluxo (pipeline) de processamento e criar um objeto `nlp`.

O comparador será inicializado com o vocabulário `nlp.vocab`. Você irá aprender sobre isso em breve. Por enquanto, lembre-se que esta etapa é necessária.

O método `matcher.add` permite adicionar uma expressão ao comparador. O primeiro argumento é o identificador único da expresssão que terá correspondência no texto. O segundo argumento é uma lista de expressões de correspondência.

Para fazer a correspondência de uma expressão em um texto, chame o comparador (matcher) e passe o texto como parâmetro.

Ele retornará as correspondências.

---

# Usando o Comparador (Matcher) (2)

```python
# Chamar o comparador e passar o texto
doc = nlp("Upcoming iPhone X release date leaked")
matches = matcher(doc)

# Iterar nas correspondências
for match_id, start, end in matches:
    # Selecionar a partição que houve correspondência
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
iPhone X
```

- `match_id`: código hash da expressão
- `start`: índice inicial da partição em que houve correspondência
- `end`: índice final da partição em que houve correspondência

Notes: Quando você usa o comparador em um documento (doc), ele retorna uma lista de tuplas.

Cada tupla consiste em três valores: o ID a expressão, o índice inicial e o índice final da partição em que houve correspondência.

Desta forma é possível iterar nas correspondências e criar um objeto partição `Span` : a parte do texto correspondente (do índice inicial até o índice final).

---

# Expressões com atributos léxicos

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("2018 FIFA World Cup: France won!")
```

```out
2018 FIFA World Cup:
```

Notes: Este é um exemplo de uma expressão mais complexa que utiliza atributos léxicos.

Estamos procurando por cinco tokens:

Um token constituído de apenas dígitos.

Três tokens sem diferenciação de maísculas e minúsculas de "fifa", "world" e "cup".

E um token que é uma pontuação.

Esta expressão tem correspondência com "2018 FIFA World Cup:".

---

# Expressões com outros atributos dos tokens

```python
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I loved dogs but now I love cats more.")
```

```out
loved dogs
love cats
```

Note: Neste exemplo, estamos procurando por dois tokens:

Um verbo com o lema "love", seguido de um substantivo.

Esta expressão terá correspondência com "loved dogs" e "love cats".

---

# Utilizando operadores e quantificadores (1)

```python
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # opcional: corresponde a 0 ou 1 vez
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I bought a smartphone. Now I'm buying apps.")
```

```out
bought a smartphone
buying apps
```

Notes: Operadores e quantificadores permitem definir quantas vezes deverá haver correspondência com a expressão. Eles podem ser usados com a chave "OP".

Neste exemplo, o operador "?" faz com que a ocorrência seja opcional, então a expressão corresponderá a um token com o lema "buy", um artigo (opcional) e um substantivo.

---

# Utilizando operadores e quantificadores (2)

| Exemplo       | Descrição                        |
| ------------- | ----------------------------     |
| `{"OP": "!"}` | Negação: corresponde 1 vez       |
| `{"OP": "?"}` | Opcional: corresponde 0 ou 1 vez |
| `{"OP": "+"}` | Corresponde 1 ou mais vezes      |
| `{"OP": "*"}` | Corresponde 1 ou mais vezes      |

Notes: "OP" pode ter um dos quatro valores abaixo:

"!" nega o valor do token, então corresponde a nenhuma ocorrência.

"?" faz o token opcional, corresponde a 0 ou 1 ocorrência.

"+" corresponde ao token uma ou mais ocorrências do token.

E "\*" corresponde a zero ou mais ocorrências do token.

Os operadores dão poder às suas expressões, mas por outro lado são mais complexos, use-os com sabedoria.

---

# Vamos praticar!

Notes: Correspondências baseadas em tokens abrem um leque de novas possibilidades para a extração de informações dos textos. Vamos exercitar e escrever algumas expressões!
