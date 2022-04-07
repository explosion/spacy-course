---
type: slides
---

# Combinando previsões e regras

Notes: Combinar previsões de modelos estatísticos com sistemas baseados em regras é um dos recursos mais poderosos que você pode encontrar em uma ferramenta de PLN.

Nesta lição, vamos dar uma olhada em como fazer isso na biblioteca spaCy.

---

# Previsões estatísticas versus regras

|                            | **Modelos estatísticos**                                              | **Sistemas baseados em regras**|
| -------------------------- | ----------------------------------------------------------------------| -------------------------------|
| **Casos de uso**           | aplicação precisa _generalizar_ a partir de exemplos                  |             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀|
| **Exemplos do mundo real** | nomes de produtos, nomes de pessoas, relações sujeito/objeto          |                                |
| **Recursos da spaCy**      | reconhec. de entidades, análise sintática, tag. de classes gramaticais|                                |

Notes: Modelos estatísticos são úteis se sua aplicação necessita generalizar a partir de alguns exemplos.

Por exemplo, a tarefa de identificar produtos ou nomes de pessoas pode se beneficiar de um modelo treinado. Ao invés de prover uma lista de todos os possíveis nomes de pessoas,
sua aplicação poderá prever se uma partição de tokens é um nome próprio. De maneira similar, é possível prever termos sintáticos e identificar relações entre sujeito e objeto.

Para alcançar esse objetivo você pode usar alguns recursos da biblioteca spaCy: reconhecimento de entidades,
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

Na biblioteca spaCy, você pode alcançar esse objetivo com regras de toquenização personalizadas,
bem como usando o Comparador (Matcher) e o Comparador de frases (PhraseMatcher).

---

# Recapitulando: Comparador baseados em regras

```python
# Inicializar com o vocabulario compartilhado
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Expressões são listas de dicionários descrevendo os tokens
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS",[pattern])

# Operadores podem determinar a frequência de correspondência de um token
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", [pattern])

# Chamar o comparador no documento doc retorna uma lista com tuplas (match_id, start, end) 
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: No último capítulo você aprendeu a utilizar o comparador baseado
em regras para identificar padrões complexos em seus textos. 

Recapitulando: o Comparador é inicializado com o vocabulário compartilhado,
geralmente o `nlp.vocab`.

Expressões são listas de dicionários, e cada dicionário descreve um token
e seus atributos. Expressões podem ser adicionadas ao Comparador utilizando
o método `matcher.add`.

Operadores permitem que você especifique a frequência de correspondência de um
token. Por exemplo: "+" significa uma ou mais ocorrências.

Chamar o Comparador em um objeto Doc retornará uma lista de correspondências.
Cada correspondência é uma tupla consistindo de um identificador ID, e o 
índice do início e final do token no documento.

---

# Adicionando previsões estatísticas

```python
matcher = Matcher(nlp.vocab)
matcher.add("DOG", [[{"LOWER": "golden"}, {"LOWER": "retriever"}]])
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

Notes: Esse é um exemplo de uma regra do Comparador para "golden retriever".

Se iterarmos nas correspondências retornadas pelo Comparador, podemos obter
o identificador da correspondência e o índice do início e do final da partição
correspondente. Podemos então analisar melhor o resultado. Objetos `Span` nos
dão acesso ao documento original e a todos os outros atributos e anotações
linguísticas previstas por um modelo.

Por exemplo, podemos obter o token raiz de uma partição. Se a partição consiste
de um ou mais tokens, este é o token que define a categoria da frase. Por exemplo,
o token raiz de "Golden Retriever" é "Retriever". Podemos também obter o token
cabeçalho de um token raiz. Este é o "pai" sintático que governa a frase. Neste 
exemplo, o token cabeçalho é o verbo "have".

E finalmente podemos obter o token anterior e seus atributos. Neste exemplo,
é um determinante, o artigo "a".

---

# Correspondência eficiente de frases (1)

- O Comparador de frases `PhraseMatcher` é similar a expressões regulares ou a busca por palavras-chave,
  mas com acesso aos tokens! 
- Recebe o objeto `Doc` como expressão
- Mais eficiente e mais rápido que o Comparador `Matcher`
- Excelente para comparar listas grandes de palavras.

Notes: O Comparador de frases é outra ferramenta útil para identificar sequências de
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
matcher.add("DOG", [pattern])
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

O Comparador de frases pode ser importado a partir de `spacy.matcher` e segue a mesma lógica que 
o Comparador padrão.

Ao invés de uma lista de dicionários, passamos um objeto `Doc` como expressão.

Nós podemos iterar nos resultados da comparação, que contêm o identificador (ID) da comparação,
e o início e o final da equivalência. Isso permite criar objetos partição `Span` e analisá-los
em um contexto.

---

# Vamos praticar!

Notes: Vamos testar algumas dessas novas técnicas de combinar regras com previsões.
