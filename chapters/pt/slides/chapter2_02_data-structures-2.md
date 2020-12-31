---
type: slides
---

# Estruturas de dados (2): Doc, partição Span e Token

Notes: Agora que vocÊ já conhece o vocabulário e o armazenamento das strings, podemos
dar uma olhada nas estruturas de dados mais importantes da spaCy: o documento `Doc` e 
as visões `Token` e partição `Span`.

---

# O objeto Doc

```python
# Criar um objeto nlp
from spacy.lang.en import English
nlp = English()

# Importar a classe Doc 
from spacy.tokens import Doc

# As palavras e espaços em branco necessários para criar um doc:
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Criar um doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: O objeto `Doc` é uma das estruturas de dados centrais da spaCy.
Ele é criado automaticamente quando você processa um texto com o objeto 
`nlp`. Mas você também pode instanciar o objeto manualmente.

Após criar o objeto `nlp`, podemos importar a classe `Doc` a partir de
`spacy.tokens`.

Aqui estamos criando um doc a partir de três palavras. Os espaços em branco
são representados por uma lista de valores boleanos que indicam se a palavra
é seguida por um espaço em branco ou não. Todos os tokens incluem essa informação, 
inclusive o último!

O objeto `Doc` tem três parâmetros: o vocabulário compartilhado, as palavras e os
espaços em branco.

---

# O objeto partição Span (1)

<img src="/span_indices.png" width="65%" alt="Ilustracao de um objeto Span em um Doc com indices dos tokens" />

Notes: Um objeto `Span` é uma partição do documento consistindo de um ou mais tokens.
Ele necessita de pelo menos três parâmetros: o doc ao qual a partição se refere,
os índices do início e do fim da partição. Lembre-se que o índice final não é
incluso na partição!

---

# O objeto partição Span (2)

```python
# Importar as classes Doc e Span
from spacy.tokens import Doc, Span

# As palavras e espaços em branco necessários para criar o doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Criar um doc manualmente 
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Criar uma particção span manualmente
span = Span(doc, 0, 2)

# Criar uma partição span com um marcador
span_with_label = Span(doc, 0, 2, label="GREETING")

# Adicionar a partição a doc.ents
doc.ents = [span_with_label]
```

Notes: Também é possível criar uma partição `Span` manualmente a partir da 
importação da classe `spacy.tokens`. Em seguida, deve-se instanciar o objeto
com o doc e os índices de início e fim da particão, e opcionalmente um marcador.

O atributo `doc.ents` pode ser atualizado, sendo possível adicionar manualmente
novas entidades a partir de uma lista de partições.

---

# Melhores práticas

- `Doc` e `Span` são recursos bastente poderosos e armazenam referencias e relações
entre palavras e sentenças:
  - **Converta os resultados para strings o mais tarde possível**
  - **Use os atributos dos tokens, se estiverem disponíveis.** – por exemplo: `token.i` para o
  índice do token
- Não se esqueça de passar o parâmetro do vocabulário compartilhado `vocab`

Notes: Algumas dicas e segredos antes de começar:

Os objetos `Doc` e `Span` são bastante poderosoe e foram otimizados para melhor performance.
Eles te dão acesso a todas as referências e relações entre as palavras e as sentenças.

Se sua aplicação necessita de saídas em texto (strings), faça as conversões
para texto o mais tarde possível. Se você fizer isso muito cedo, você 
corre o risco de perder todas as relações entre os tokens.

Para que seu projeto seja consistente, use os atributos dos tokens já existentes sempre
que possível

are very powerful and optimized for performance. They give
you access to all references and relationships of the words and sentences.

If your application needs to output strings, make sure to convert the doc as
late as possible. If you do it too early, you'll lose all relationships between
the tokens. Por exemplo: `token.i` para o índice do token.

E também é preciso sempre passar o vocabulário compartilhado como parâmetro!

---

# Vamos praticar!

Notes: Vamos agora experimentar isso tudo e criar alguns docs e partições do zero.
