---
type: slides
---

# Estruturas de dados (1): Vocabulário, Lexemas e armazenamento de Strings

Notes: Bem-vindo de volta! Agora que você já teve uma experiência real com a biblioteca spaCy em ação, é hora de aprender um pouco mais sobre o que acontece nos bastidores.

Nesta lição, vamos dar uma olhada no vocabulário compartilhado (Vocab) e como a spaCy lida com strings.


---

# Vocabulário compartilhado e armazenamento de strings (1)

- `Vocab`: armazena informações compartilhadas entre diversos documentos
- Para economizar memória, a spaCy mapeia as strings em **códigos hash**
- Strings são armazenadas apenas uma vez na `StringStore` via `nlp.vocab.strings`
- Armazenamento de Strings: **tabelas de consultas** que funcionam em ambos sentidos

```python
nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]
```

- Códigos hash não podem ser revertidos - por isso é preciso sempre prover o vocabulário compartilhado

```python
# Gera um erro se a string não foi mapeada anteriomente
string = nlp.vocab.strings[3197928453018144401]
```

Notes: A spaCy armazena todos os dados compartilhados em um vocabulário: o **Vocab**.

Ele inclui palavras e também esquemas para marcadores e entidades. 

Para economizar memória, todas as strings são mapedas em códigos hash. Se uma palavra
ocorre mais de uma vez, só é necessário salvá-la uma vez.

A spaCy usa uma função hash para gerar um identificador (ID) e armazena a string apenas
uma vez. As strings armazenadas estão disponíveis em `nlp.vocab.strings`.

Trata-se de uma tabela de consulta que pode ser utilizada nos dois sentidos. Você pode
pesquisar uma string e obter o seu código hash, ou pode pesquisar um código hash e obter
a string correspondente. Internamente, a spaCy só lida com códigos hash.

Mas os códigos hash não podem ser revertidos diretamente. Isso quer dizer que se uma palavra 
não estiver registrada no vocabulário, não será possível obter sua string. Por isso 
é sempre necessário fazer o registro no vocabulário compartilhado.

---

# Vocabulário compartilhado e armazenamento de strings (2)

- Consultar as strings e códigos hash no `nlp.vocab.strings`

```python
doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])
```

```out
hash value: 3197928453018144401
string value: coffee
```

- O objeto `doc` também expõe o vocabulário compartilhado com as strings e códigos hash

```python
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])
```

```out
hash value: 3197928453018144401
```

Notes: Para obter o código hash de uma string, podemos fazer a consulta em `nlp.vocab.strings`.

Para obter a string que representa um código hash, fazemos a consulta com o hash.

O objeto `Doc` também expõe o vocabulário compartilhados e suas strings e códigos hash.

---

# Lexemas: entradas do vocabulário 

- Um objeto lexema `Lexeme` corresponde a uma entrada do vocabulário.

```python
doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# Imprimir os atributos léxicos
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
coffee 3197928453018144401 True
```

- Contém as informações **independentes de contexto** de cada palavra:
  - Texto da palavra: `lexeme.text` e `lexeme.orth` (o código hash)
  - Atributos léxicos, como por exemplo `lexeme.is_alpha`
  - **Não incluem** marcadores que dependem do contexto, como classe gramatical, termo sintático ou entidade.

Notes: Lexemas são entradas do vocabulário que independem do contexto.

Você obtém um lexema a partir da consulta de uma string ou código hash no vocabulário.

Lexemas possuem atributos, assim como os tokens.

Eles armazenam informações de uma palavra que são independentes de contexto: texto,
se a palavra é composta por apenas caracteres alfabéticos, etc.

Lexemas não armazenam marcadores de classe gramatical, termo sintático ou entidade. Eles dependem
do contexto no qual a palavra está inserida.

---

# Vocabulário, códigos hash e lexemas

<img src="/vocab_stringstore.png" width="70%" alt="Ilustracao das palavras 'I', 'love' e 'coffee' no Doc, Vocab e StringStore" />

Notes: Aqui está um exemplo:

O `Doc` contém palavras em seu contexto - neste caso, os tokens "I", "love" e
"coffee"- com seus marcadores de classe gramatical e dependência sintática.

Cada token está mapeado a um lexema, e também ao código hash da palavra. Para obter
a string que representa uma palavra, a spaCy faz a consulta do código hash nas strings 
armazenadas.

---

# Vamos praticar!

Notes: Tudo isso está soando um pouco abstrato... então vamos dar uma olhada no vocabulário e suas strings
armazenadas.
