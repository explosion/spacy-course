---
type: slides
---

# Combinando modelos e regras

Notes: Combinar modelos estatísticos com sistemas baseados em regras é um dos truques
mais poderosos que você pode encontrar em uma ferramenta de PLN.

Nesta lição, vamos dar uma olhada em como fazer isso na spaCy.

---

# Previsões estatísticas versus regras

|                            | **Modelos estatísticos**                                              | **Sistemas baseados em regras**|
| -------------------------- | ----------------------------------------------------------------------| -------------------------------|
| **Casos de uso**           | aplicação precisa _generalizar_ a partir de exemplos                  |             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀|
| **Exemplos do mundo real** | nomes de produtos, nomes de pessoas, relações sujeito/objeto          |                                |
| **Recursos da spaCy**      | reconhec. de entidades, análise sintática, tag. de classes gramaticais|                                |

Notes: Modelos estatísticos são úteis se sua aplicação necessita precisa generalizar a partir de alguns exemplos.

Por exemplo, a tarefa de identificar produtos ou nomes de pessoas pode se beneficiar de um modelo
estatístico. Ao invés de prover uma lista de todos os possíveis nomes de pessoas,
sua aplicação poderá prever se uma partição de tokens é um nome próprio. De maneira similar, 
é possível prever termos sintáticos e identificar relações entre sujeito e objeto.

Para alcançar esse objetivo você pode usar as recursos da spaCy: reconhecimento de entidades,
analisador sintático e o tagueador de classes gramaticais.

---

# Previsões estatísticas versus regras


|                            | **Modelos estatísticos**                                              | **Sistemas baseados em regras**|
| -------------------------- | ----------------------------------------------------------------------| -------------------------------|
| **Casos de uso**           | aplicação precisa _generalizar_ a partir de exemplos                  | dicionário com número finito de exemplos|
| **Exemplos do mundo real** | nomes de produtos, nomes de pessoas, relações sujeito/objeto          | países do mundo, cidades, nomes de remédios, raças caninas |
| **Recursos da spaCy**      | reconhec. de entidades, análise sintática, tag. de classes gramaticais| toquenizador, `Matcher`, `PhraseMatcher`|


Notes: Por outro lado, estratégias baseadas em regras são úteis se há um 
número finito de ocorrências que você deseja identificar. Por exemplo,
todos os países ou cidades do mundo, nomes de remédios ou raças de cachorros.

Na spaCy, você pode alcançar esse objetivo com regras de toquenização customizadas,
bem como usando o comparador e o comparador de frases.

---

# Recap: Comparador baseados em regras

```python
# Inicializar com o vocabulario compartilhado
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Expressões são listas de dicionários descrevendo os tokens
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", None, pattern)

# Operadores podem determinar a frequência de correspondência de um token
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", None, pattern)

# Chamar o comparador no documento doc retorna uma lista com tuplas (match_id, start, end) 
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: No último capítulo você aprendeu a utilizar o comparador baseado
em regras para identificar padrões complexos nos seus textos. 

Recapitulando: o comparador é inicializado com o vocabulário compartilhado,
geralmente o `nlp.vocab`.

Expressões são listas de dicionários, e cada dicionário descreve um token
e seus atributos. Expressões podem ser adicionadas ao comparador utilizando
o método `matcher.add`.

Operadores permitem você especificar a frequência de correspondencia de um
token. Por exemplo: "+" significa uma ou mais ocorrências.

Chamar o comparador em um objeto doc retornará uma lista de correspondências.
Cada correspondência é uma tupla consistindo de um identificador ID, e o 
índice do início e final do token no documento.

---

# Adicionando previsões estatísticas

```python
matcher = Matcher(nlp.vocab)
matcher.add("DOG", None, [{"LOWER": "golden"}, {"LOWER": "retriever"}])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # Obter o token raiz e o token cabeçalho da partição 
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # Obter o token anterior e seu marcador de classe gramatical
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Matched span: Golden Retriever
Root token: Retriever
Root head token: have
Previous token: a DET
```

Notes: Esse é um exemplo de uma regra do comparador para "golden retriever".

Se iterarmos nas correspondências retornadas pelo comparador, podemos obter
o identificador da correspondência e o índice do início e do final da partição
correspondente. Podemos então analisar melhor o resultado. Objetos `Span` nos
dão acesso ao documento original e todos os outros atributos e anotações
linguísticas previstas pelo modelo.

Por exemplo, podemos obter o token raiz de uma partição. Se a partição consiste
de um ou mais tokens, este é o token que define a categoria da frase. Por exemplo,
o token raiz de "Golden Retriever" é "Retriever". Podemos também obter o token
cabeçalho de um token raiz. Este é o "pai" sintático que governa a frase. Neste 
exemplo, o token cabeçalho é o verbo "have".

E finalmente podemos obter o token anterior e seus atributos. Neste exemplo,
é um determinante, o artigo "a".

---

# Correspondência eficiente de frases (1)

- O `PhraseMatcher` é similar a expressões regulares ou busca por palavras-chave,
  mas com acesso aos tokens ! 
- Recebe o objeto `Doc` como expressão
- Mais eficiente e mais rápido que o comparador `Matcher`
- Excelente para comparar listas grandes de palavras.

Notes: O comparador de frases é outra ferramenta útil para identificar sequências de
palavras em seus textos.

Ele realiza uma busca por palavras-chave no documento, mas ao invés de apenas procurar
por strings, ele permite acesso aos tokens e os contextos.

Ele recebe o objeto `Doc` como expressão.

E também é muito rápido.

Por tudo isso ele é muito útil para comparar longos dicionários e listas de palavras
em grandes volumes de texto.

---

# Correspondência eficiente de frases (2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", None, pattern)
doc = nlp("I have a Golden Retriever")

# Iterar nas correspondências
for match_id, start, end in matcher(doc):
    # Obter a partição que houve correspondência
    span = doc[start:end]
    print("Matched span:", span.text)
```

```out
Matched span: Golden Retriever
```

Notes: Aqui está um exemplo:

O comparador de frases pode ser importado a partir de `spacy.matcher` e segue a mesma lógica que 
o comparador padrão.

Ao invés de uma lista de dicionários, passamos um objeto `Doc` como expressão.

Nós podemos iterar nos resultados da comparação, que contêm o identificador (ID) da comparação,
e o início e o final da equivalência. Isso permite criar objetos partição `Span` e analisá-los
em um contexto.

---

# Vamos praticar!

Notes: Vamos testar algumas dessas novas técnicas de combinar regras com modelos estatísticos.
