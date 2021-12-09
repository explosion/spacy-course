---
type: slides
---

# Introdução a biblioteca spaCy

Notes: Olá, eu sou a Ines! Sou uma desenvolvedora pricipal da spaCy, uma biblioteca bastante popular para o Processamento de Linguagem Natural avançado em Python.

Nesta lição, vamos dar uma olhada nos principais conceitos da spaCy e percorrer nossos primeiros passos.

---

# O objeto nlp

```python
# Importar a classe para a língua inglesa
from spacy.lang.en import English

# Criar o objeto nlp
nlp = English()
```

- contém o fluxo de processamento
- inclui regras específicas da linguagem, como toquenização etc.

Notes: No cerne da spaCy está o objeto nlp, que contém o fluxo de processamento. Por convenção, normalmente chamamos essa variável de "nlp".

Como exemplo, para criar o objeto `nlp` em inglês, importamos a classe `English` de `spacy.lang.en` e criamos uma instância desta classe. Podemos utilizar o objeto nlp como se chamássemos uma função para analisar algum texto.

O objeto contém os diferentes componentes do fluxo de processamento do texto.

Ele também contém regras específicas de cada idioma para a toquenização do texto em palavras e pontuação. A spaCy oferece suporte para diversos idiomas, que estão disponíveis em `spacy.lang`.

---

# O objeto Doc

```python
# Criado após processar um texto com o objeto nlp
doc = nlp("Hello world!")

# Iterar nos tokens do Doc
for token in doc:
    print(token.text)
```

```out
Hello
world
!
```

Notes: Quando você processa um texto com o objeto `nlp`, a spaCy cria um objeto `Doc`- abreviação de "documento". Através do Doc é possível acessar informações do texto de uma maneira estruturada, sendo que nenhuma informação é perdida.

O Doc se comporta de maneira semelhante a uma sequência do Python, permitindo a iteração nos tokens e o acesso a um token através do seu índice. Mas falaremos disso mais tarde!


---

# O objeto Token

<img src="/doc.png" alt="Ilustração de um objeto Doc contendo quatro tokens" width="50%" />

```python
doc = nlp("Hello world!")

# Indexar o Doc para obter um Token
token = doc[1]

# Obter o texto do token através do atributo .text
print(token.text)
```

```out
world
```

Notes: O objeto `Token` representa uma parte do texto: uma palavra ou um caracter de pontuação.

Para acessar um token em uma posição específica, você pode indexar o objeto Doc.

Os objetos `Token` também contêm vários atributos que permitem acessar mais informações sobre os tokens. Por exemplo: o atributo `.text` retorna o texto _verbatim_.

---

# O objeto Partição (Span)

<img src="/doc_span.png" width="50%" alt="Ilustração de um objeto Doc com quatro tokens e três deles agrupados em uma Partição." />

```python
doc = nlp("Hello world!")

# Um pedaço do Doc é um objeto Partição (Span) 
span = doc[1:3]

# Obter o texto da partição com o atributo .text
print(span.text)
```

```out
world!
```

Notes: Um objeto partição `Span` é uma partição do documento consistindo de um ou mais tokens. É apenas um apontamento para o `Doc` e não contém dados em si mesmo.

Para criar uma partição, você pode usar a notação de partição do Pyhton. Por exemplo, `1:3` criará uma partição do token na posição 1 até o token na partição 3, mas não incluindo este último.

---

# Atributos léxicos

```python
doc = nlp("It costs $5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['It', 'costs', '$', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Notes: Aqui você pode observar alguns dos atributos dos tokens disponíveis :

`i` é o índice do token no documento principal.

`text` retorna o texto do documento.

`is_alpha`, `is_punct` e `like_num` retornam valores boleanos (verdadeiro ou falso) indicando respectivamente se o token tem caracteres alfabéticos, se é uma pontuação ou se _assemelha-se_ a um número, por exemplo, o token "10" – um, zero – ou a palavra "dez" – D,E,Z.

Esses atributos são também chamados de atributos léxicos: referem-se ao token em si e não dependem de nenhum contexto no qual o token está inserido.

---

# Vamos praticar!

Notes: Vamos agora ver isso tudo em ação e processar seu primeiro texto com a spaCy.
