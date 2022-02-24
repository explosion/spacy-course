---
type: slides
---

# Vetores de palavras e similaridades semânticas

Notes: Nesta lição você aprenderá a usar a biblioteca spaCy para prever o quão dois
documentos, partições ou tokens são similares entre si.

Você também aprenderá a usar vetores de palavras e como tirar vantagem
de seu uso em aplicações de PLN.

---

# Comparando similaridades semânticas

- A biblioteca `spaCy` pode comparar dois objetos e prever a sua similaridade.
- `Doc.similarity()`, `Span.similarity()` e `Token.similarity()`
- Recebem outro objeto e retornam um score de similaridade ( entre `0` e `1` )
- **Importante:** é necessário incluir um fluxo (pipeline) de processamento que tenha vetores de palavras incluso,
como por exemplo:
  - ✅ `en_core_web_md` ou `pt_core_news_md` ( tamanho médio )
  - ✅ `en_core_web_lg` ou `pt_core_news_lg` ( tamanho grande )
  - 🚫 **NÃO USE** `en_core_web_sm` ou `pt_core_news_sm` ( tamanho pequeno )

Notes: A spaCy consegue comparar dois objetos e prever o quão similares eles são
entre si. Os objetos podem ser documentos, partições ou tokens.

Os objetos `Doc`, `Token` e `Span` possuem o método `.similarity` que recebe
outro objeto e retorna um número de ponto flutuante entre 0 e 1 indicando o
quão similares estes objetos são entre si.

Um detalhe importante: para poder usar a similaridade, você necessita usar um
fluxo (pipeline) de processamento maior que inclua a representação das palavras em vetores (word vectors).

Você pode usar o fluxo (pipeline) de processamento médio ou grande da língua inglesa, mas _não_ o modelo pequeno.
Se você desejar usar os vetores, sempre use um fluxo (pipeline) de processamento que termine com os caracteres
"md" ou "lg". Para mais detalhes, visite a [documentação dos modelos](https://spacy.io/models).

---

# Exemplos de similaridades (1)

```python
# Carregar o fluxo (pipeline) de processamento maior com os vetores
nlp = spacy.load("en_core_web_md")

# Comparar dois documentos
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
```

```out
0.8627204117787385
```

```python
# Comparar dois tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
```

```out
0.7369546
```

Notes: Aqui está um exemplo: vamos supor que você deseja saber se dois documentos
são similares.

Inicialmente carregamos o modelo médio da língua inglesa : "en_core_web_md".

Em seguida podemos criar dois objetos o usar o método  `similarity` do primeiro
documento, comparando com o segundo.

Neste caso, encontramos uma similaridade razoavelmente alta entre "I like fast food"
e "I like pizza".

O mesmo pode ser feito para tokens.

De acordo com os vetores de palavras, os tokens "pizza" e "pasta" são relativamente
similares e receberam um score de 0.7.

---

# Exemplos de similaridades (2)

```python
# Comparar um documento com um token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))
```

```out
0.32531983166759537
```

```python
# Comparar uma partição com um documento
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))
```

```out
0.619909235817623
```

Notes: Você também pode usar o método `similarity` para comparar tipos de
objetos diferentes.

Por exemplo: um documento e um token.

No primeiro exemplo, o score de similaridade é bem baixo e podemos considerar que esses
objetos não são similares.

No outro exemplo comparamos uma partição "pizza and pasta" com um documento
sobre McDonalds.

O score foi 0.61, que significa que são um pouco similares.

---

# Como a spaCy prevê similaridades?

- A similaridade é determinada usando os **vetores de palavras**
- Vetores são representações multi dimensionais das palavras
- São gerados utilizando algoritmos similares a 
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) e uma enorme quantidade de textos.
- Podem ser adicionados aos fluxos (pipelines) de processamento da spaCy.
- Algoritmo padrão: similaridade por cosseno, mas pode ser alterado
- Os vetores de `Doc` e `Span` são a média dos vetores de seus tokens.
- Frases curtas são melhores que grandes documentos com palavras irrelevantes.

Notes: Mas como a spaCy faz esse cálculo de similaridade?

A similaridade é determinada utilizando-se vetores de palavras, que são representações
multi dimensionais do significado de cada palavra.

Você deve ter ouvido falar do Word2Vec, um algoritmo que é usado com frequencia para
treinar vetores de palavras a partir de textos.

Os vetores podem ser adicionados aos modelos estatísticos da spaCy.

Por padrão, a similaridade calculada pela spaCy é a similaridade cosseno entre os
dois vetores, mas isso pode ser alterado se necessário.

O vetor de um objeto consistido de vários tokens, como o `Doc` e o `Span`, é calculado 
como a média dos vetores dos seus tokens.

É por este motivo que você consegue extrair mais valor de frases curtas com poucas
palavras irrelevantes.

---

# Vetores de palavras na spaCy

```python
# Carregar um fluxo (pipeline) de processamento maior com vetores
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Acessar o vetor através do atributo token.vector
print(doc[3].vector)
```

```out
 [2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
  3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
 -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
  5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
 -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
  1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
  5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
  2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
  1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
 -4.00279984e-02,   9.59490016e-02,  -5.06900012e-01,
 -8.53179991e-02,   1.79800004e-01,   3.38669986e-01,
  ...
```

Notes: Para termos uma idéia de como são esses vetores, vamos ver este exemplo.

Primeiro, carregamos o fluxo (pipeline) de processamento médio novamente, que inclui os vetores das palavras.

Em seguida, processamos o texto e consultamos o vetor de um token através do atributo
`.vector`.

O resultado é um vetor com 300 dimensões para a palavra "banana".

---

# A similaridade depende do contexto da aplicação 

- Útil para diversas aplicações: sistemas de recomendação, identificar textos duplicados, etc.
- Não há uma definição objetiva do que é "similaridade"
- Depende do contexto e do que se espera de resultado da aplicação.


```python
doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))
```

```out
0.9501447503553421
```

Notes: Prever similaridades pode ser bastante útil em algumas aplicações. Por
exemplo, para recomendar para um usuário textos similares aos que ele já leu.
Também pode ser usado para identificar conteúdos duplicados, como publicações
em plataformas online.

Contudo é importante ter em mente que não existe uma definição objetiva daquilo
que é similar ou não. Isso sempre vai depender do contexto e do objetivo da
sua aplicação.

Analise este exemplo: os vetores padrão das palavras da biblioteca spaCy atribuem um score
de alta similaridade entre "I like cats" e "I hate cats". Isso faz sentido,
pois os dois textos expressam sentimentos relacionados a gatos. Mas no contexto
de uma aplicação, você pode considerar que as duas frases são _pouco similares_, 
pois expressam sentimentos opostos.

---

# Vamos praticar!

Notes: Agora é a sua vez. Vamos dar uma olhada nos vetores de palavras da spaCy
e usá-los para prever similaridades.
