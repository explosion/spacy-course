---
type: slides
---

# Aumentando a escala e o desempenho

Notes: Nesta lição, vou te mostrar algumas dicas e truques para fazer seus
fluxos de processamento do spaCy rodarem o mais rápido possível e processarem
grandes volumes de texto de maneira eficiente.

---

# Processando grandes volumes de texto

- Use o método `nlp.pipe`
- Processa textos com um fluxo (stream), produzindo objetos `Doc`
- Muito mais rápido que usar `nlp` para cada texto

**RUIM:**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**BOM:**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: Se você precisa processar um grande volume de textos e criar vários
objetos `Doc` de uma só vez, o método `nlp.pipe` pode acelerar o processamento
de maneira significativa.

Ele processa os textos como um fluxo e produz objetos `Doc`.

É muito mais rápido que ir chamando nlp em cada texto, pois neste caso
os textos são tratados em lotes.

O `nlp.pipe` é um gerador que produz objetos `Doc`, então para obter uma
lista de documentos, lembre-se de incluir `list`.

---

# Passando o contexto (1)

- Definir `as_tuples=True` em `nlp.pipe` permite você passar as tuplas `(text, context)`
- Produz tuplas `(doc, context)` 
- Útil para associar metadados ao documento `doc`

```python
data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
```

```out
This is a text 15
And another text 16
```

Notes: `nlp.pipe` também suporta passar tuplas de texto / contexto se você definir
`as_tuples` como `True`.

O método vai produzir tuplas documento / contexto.

Isso é útil para passar metadados adicionais, como um ID associado ao texto, ou o
número de uma página.

---

# Passando o contexto (2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
```

Notes: Você pode até adicionar metadados de contexto para personalizar atributos.

Neste exemplo, estamos registrando duas extensões: `id` e `page_number`, com
valor padrão como `None`.

Após processar o texto e passar o contexto, podemos sobrescrever as extensões do
documento com os metadados do contexto.

---

# Usando o toquenizador (1)

<img src="/pipeline.png" width="90%" alt="Ilustracao do fluxo de processamento do spaCy">

- não processe o fluxo de processamento (pipeline) completo!

Notes: Outro cenário comum é que muitas vezes você já tem um modelo carregado para
fazer o processamento, mas você só precisa do toquenizador para um texto 
específico.

Rodar o fluxo de processamento completo será muito ineficiente, uma vez que você
processará previsões que não serão utilizadas.

---

# Usando o toquenizador (2)

- Use `nlp.make_doc` para converter um texto em um objeto `Doc`

**RUIM:**

```python
doc = nlp("Hello world")
```

**BOM:**

```python
doc = nlp.make_doc("Hello world!")
```

Notes: Se você apenas precisa de um objeto `Doc` toquenizado, você pode usar o método
`nlp.make_doc`, que recebe um texto e retorna um objeto doc.

Isso é exatamente o que o spaCy faz: `nlp.make_doc` transforma o texto em um documento
doc antes de chamar os componentes do fluxo de processamento.

---

# Desabilitando componentes do fluxo de processamento

- Use `nlp.disable_pipes` para temporariamente desabilitar um ou mais componentes

```python
# Desabilitar o tagueador tagger e o analisador parser
with nlp.disable_pipes("tagger", "parser"):
    # Processar o texto e imprimir as entidades
    doc = nlp(text)
    print(doc.ents)
```

- Restaura os componentes após o bloco `with`
- Apenas roda os componentes remanescentes 

Notes: O spaCy também permite que você desabilite temporariamente componentes
do fluxo de processamento usando o comando gerenciador de contexto 
`nlp.disable_pipes`. 

Ele recebe uma alguns parâmetros, como o nome dos componentes
que devem ser desabilitados. Por exemplo, se você deseja usar o identificador
de entidades para processar o documento, você pode temporariamente desabilitar
o tagueador e o analisador.

Após o bloco `with`, os componentes desabilitados são automaticamente 
reabilitados.

No bloco `with`, o spaCy vai apenas rodar os componentes remanescentes.

---

# Vamos praticar!

Notes: Agora é a sua vez ! Vamos testar novos métodos e otimizar um código
para ser mais rápido e eficiente.
