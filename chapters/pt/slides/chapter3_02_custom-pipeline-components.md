---
type: slides
---

# Componentes personalizados do fluxo de processamento

Notes: Agora que você já sabe como o fluxo de processamento da spaCy funciona,
vamos dar uma olhada em outro recurso muito poderoso: componentes personalizados
do fluxo de processamento.

Componentes personalizados permitem que você adicione uma função feita por você ao
fluxo de processamento (pipeline), que é executado quando você chama `nlp` em um texto. Por 
exemplo: você pode modificar o documento e adicionar mais dados a ele.

---

# Por que personalizar componentes ?

<img src="/pipeline.png" alt="Ilustracao do fluxo de processamento da spaCy" width="90%" />

- Permite que uma função seja executada automaticamente quando você chamar `nlp`
- Adiciona metadados personalizados ao documentos e aos tokens
- Atualiza atributos padrão como por exemplo entidades `doc.ents`

Notes: Após o texto ser toquenizado e o objeto  ser criado, os componentes do 
fluxo de processamento (pipeline) são aplicados sequencialmente. A biblioteca spaCy suporta uma
grande variedade de componentes pré-existentes, mas também permite que você
crie seu próprio componente.

Componentes personalizados são executados automaticamente quando você chamar
o objeto `Doc` em um texto.

Eles são especialmente úteis para você adicionar metadados personalizados 
aos documentos e tokens.

Você também pode usá-los para atualizar os atributos já existentes, como
as partições com entidades nomeadas.

---

# Anatomia de um componente (1)

- Função que recebe um `doc`, o modifica, e em seguida o retorna
- Pode ser adicionado ao fluxo de processamento através do método `nlp.add_pipe`

```python
def custom_component(doc):
    # Faz alguma coisa com o documento
    return doc

nlp.add_pipe(custom_component)
```

Notes: Fundamentalmente, o componente de um fluxo de processamento é uma função
ou um objeto que recebe um documento, o modifica e em seguida retorna este objeto,
que pode ser processado em seguida pelo próximo componente do fluxo de processamento.

Componentes podem ser adicionados ao fluxo de processamento (pipeline) através do método `nlp.add_pipe`. 
O método recebe pelo menos um parâmetro: a função do componente.


---

# Anatomia de um componente (2)

```python
def custom_component(doc):
    # Faz alguma coisa com o documento
    return doc

nlp.add_pipe(custom_component)
```

|Parâmetro | Descrição                      | Exemplo                                   |
| -------- | ------------------------------ | ----------------------------------------- |
| `last`   | Se `True`, adicionar no final  | `nlp.add_pipe(component, last=True)`      |
| `first`  | Se `True`, adicionar no início | `nlp.add_pipe(component, first=True)`     |
| `before` | Adicionar antes do componente  | `nlp.add_pipe(component, before="ner")`   |
| `after`  | Adicionar depois do componente | `nlp.add_pipe(component, after="tagger")` |

Notes: Para definir _onde_ o componente será adicionado ao fluxo de processamento,
você pode usar os seguintes argumentos:

Definir `last` como `True` irá adicionar o componente ao final do fluxo de processamento.
Esse é o comportamento padrão.

Definir `first` como `True` irá adicionar o componente ao início do fluxo de processamento,
logo após o toquenizador.

Os argumentos `before` e `after` permitem definir o nome de um componente existente de tal
forma que o novo componente seja adicionado antes ou depois dele. Por exemplo: `before="ner"`
irá adicionar o novo componente antes do identificador de entidados nomeadas.

O componente existente ao qual o novo componente deve ser adicionado antes ou depois precisa
existir, senão a spaCy gerará um erro.


---

# Exemplo: um componente simples (1)

```python
# Criar um objeto nlp
nlp = spacy.load("en_core_web_sm")

# Definir um componente personalizado
def custom_component(doc):
    # Imprimir o tamanho do documento
    print("Doc length:", len(doc))
    # Retornar o objeto doc
    return doc

# Adicionar o componente como primeiro no fluxo de processamento
nlp.add_pipe(custom_component, first=True)

# Imprimir o nome dos componentes do fluxo de processamento
print("Pipeline:", nlp.pipe_names)
```

```out
Pipeline: ['custom_component', 'tagger', 'parser', 'ner']
```

Notes: Aqui está mais um exemplo de um componente simples do fluxo de processamento

Começamos com o modelo pequeno da língua inglesa.

Em seguida definimos o componente: uma função que recebe um objeto `Doc` e o 
retorna.

Vamos fazer algo simples e imprimir o tamanho do documento recebido.

Não se esqueça de retornar o documento para que ele seja processado pelo
próximo componente no fluxo de processamento! O documento criado pelo
toquenizador é passado para todos os componentes, portanto é essencial
retornar o documento modificado.

Agora podemos adicionar o componente ao fluxo de processamento. Vamos
adicioná-lo logo no início, após o toquenizador, definindo o atributo 
`first=True`.

Quando imprimimos os nomes dos componentes do fluxo de processamento, o
componente personalizado agora aparece no início. Isso significa que ele
será aplicado logo no início do processamento do documento.


---

# Exemplo: um componente simples (2)

```python
# Criar um objeto nlp
nlp = spacy.load("en_core_web_sm")

# Definir um componente customizado
def custom_component(doc):

    # Imprimir o tamanho do documento
    print("Doc length:", len(doc))

    # Retornar o objeto doc
    return doc

# Adicionar o componente no inicio do fluxo de processamento
nlp.add_pipe(custom_component, first=True)

# Processar o texto
doc = nlp("Hello world!")
```

```out
Doc length: 3
```

Notes: Agora quando processarmos um texto usando o objeto `nlp`, o 
componente customizado será aplicado ao documento e o tamanho do documento
será impresso.

---

# Vamos praticar!

Notes: Agora é sua hora de praticar! Escreva seu primeiro componente personalizado do fluxo de processamento!
