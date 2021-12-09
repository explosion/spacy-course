---
type: slides
---

# Extensões de atributos

Notes: Nesta lição, você vai aprender como adicionar atributos personalizados
aos objetos `Doc`, `Token` e `Span` para armazenar informações adicionais.

---

# Definindo atributos personalizados

- Adicionam metadados personalizados a documentos, partições e tokens
- Accessíveis através da propriedade `._`

```python
doc._.title = "My document"
token._.is_color = True
span._.has_color = False
```

- São registrados na classe global `Doc`, `Token` ou `Span` através do método `set_extension`

```python
# Importar classes globais
from spacy.tokens import Doc, Token, Span

# Definir extensões para os objetos Doc, Token e Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: Atributos personalizados permitem que você adicione metadados aos 
documentos, partições ou tokens. Os dados podem ser adicionados uma vez ou
calculados dinamicamente.

Atributos personalizados ficam disponíveis através da propriedade `._` 
(ponto sublinhado). Isso deixa claro que foram adicionados pelo usuário
e não são padrão da spaCy, como por exemplo `token.text`.

Esses atributos devem ser registrados nas classes globais `Doc`, `Token` e `Span`,
que podem ser importadas de `spacy.tokens`. Você já trabalhou com essas
classes nos capítulos anteriores. Para registrar um atributo personalizado no
`Doc`, `Token` e `Span` você deve usar o método `set_extension`.

O primeiro parâmetro é o nome do atributo. Parâmetros nomeados permitem que
você defina como o valores serão computados. Neste caso, ele tem um valor
padrão que pode ser posteriormente alterado.

---

# Tipos de extensões 

1. Extensões de atributos
2. Extensões de propriedades
3. Extensões de métodos

Notes: Existem três tipos de extensões: extensões de atributos, extensões
de propriedades, extensões de métodos.

---

# Extensões de atributos

- Define um valor padrão que pode ser modificado

```python
from spacy.tokens import Token

# define a extensão do token com valor padrão
Token.set_extension("is_color", default=False)

doc = nlp("The sky is blue.")

# Sobrescreve o valor do atributo extendido
doc[3]._.is_color = True
```

Notes: Extensões de atributos definem um valor que pode ser alterado
posteriormente.

Por exemplo, a extensão de atributo `is_color` que tem o valor padrão
como `False`.

Em tokens individuais, o valor pode ser alterado sobrescrevendo o valor.
Neste caso será "True" para o token "blue".

---

# Extensões de propriedades (1)

- Definem funções opcionais "getter" e "setter"
- A função "getter" só pode ser usada quando você _recuperar_ o valor do atributo

```python
from spacy.tokens import Token

# Definir uma função getter 
def get_is_color(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors

# Define uma extensão ao token com a função getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("The sky is blue.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
True - blue
```

Notes: Extensões de propriedades são similares às propriedades em Python:
elas definem uma função getter e uma função setter opcional.

A função getter só é utilizada quando você recupera os valores de um atributo.
Isso permite calcular o valor dinamicamente e até levar em conta valores de
outros atributos.

Funções getter recebem apenas um parâmetro: o objeto, neste caso, o token.
Neste exemplo, a função retorna se o texto do token está na lista de cores.

Quando registramos uma extensão, definimos a função getter através do parâmetro
nomeado `getter`.

O token "blue" agora retorna `True` para a propriedade extendida `._.is_color`.

---

# Extensões de propriedades (2)

- Extensões de partições `Span` devem sempre usar uma função getter.

```python
from spacy.tokens import Span

# Definir a função getter
def get_has_color(span):
    colors = ["red", "yellow", "blue"]
    return any(token.text in colors for token in span)

# Definir a extensão com o parametro getter sendo a função definida
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("The sky is blue.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - sky is blue
False - The sky
```

Notes: Se você quiser definir uma extensão de uma partição,
você sempre deve usar a extensão de propriedade com uma função getter.
Se não fizer assim, você terá que atualizar _toda e qualquer partição_
manualmente para definir todos seus valores.

Neste exemplo, a função `get_has_color` recebe a partição e retorna
se o texto ou algum token do texto está na lista de cores.

Após processarmos o documento, podemos checar diferentes partições do
texto e inspecionar a propriedade `._.has_color`, que indicará se a
partição contém um token das cores selecionadas ou não.

---

# Extensões de métodos

- Definem uma **função** que se torna disponível como um método do objeto
- Permitem que você passe **parâmetros** para essa nova função

```python
from spacy.tokens import Doc
s
# Definir método com seus parâmetros
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Definir a extensão do documento com o parâmetro nomeado method
Doc.set_extension("has_token", method=has_token)

doc = nlp("The sky is blue.")
print(doc._.has_token("blue"), "- blue")
print(doc._.has_token("cloud"), "- cloud")
```

```out
True - blue
False - cloud
```

Notes: Extensões de métodos permitem que um atributo se torne um método que pode
ser chamado.

Você pode passar um ou mais parâmetros para o método extendido, e calcular valores
de atributos dinamicamente. Por exemplo, baseado em algum argumento ou configuração.

Neste exemplo, a função verifica se o documento contém um token com
um dado texto. O primeiro parâmetro do método é sempre o objeto em si, neste caso,
o documento. Ele é passado automaticamente quando o método é chamado. Todos os
outros parâmetros serão passados à função extendida, neste caso, `token_text`.

Aqui o método extendido `._.has_token` retornará `True` para a palavra "blue" e
`False` para a palavra "cloud".

---

# Vamos praticar!

Notes: Agora é a sua vez. Vamos adicionar algumas extensões personalizadas!
