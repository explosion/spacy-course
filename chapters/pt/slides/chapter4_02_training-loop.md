---
type: slides
---

# O laço (loop) de treinamento

Notes: Enquanto outras bibliotecas entregam um método responsável pelo
treinamento completo de um modelo, a biblioteca spaCy possibilita o controle total de todas 
as etapas envolvidas no treinamento de um modelo.

---

# Os passos do laço (loop) de treinamento:

1. **Repita** uma série de vezes.
    1.1. **Embaralhe** os dados de treinamento.
    1.2. **Divida** os dados em lotes.
    1.3. **Atualize** o modelo para cada lote.
    1.4. **Salve** o modelo atualizado.

Notes: O loop de treinamento engloba uma série de passos que são executados
para treinar ou atualizar um modelo.

Normalmente precisamos executar esses passos diversas vezes, em múltiplas iterações,
de forma que o modelo aprenda eficientemente. Se desejarmos treinar o modelo
por 10 iterações, precisamos executar o loop 10 vezes.

Para prevenir que o modelo convirja para uma solução sub-ótima, nós embaralhamos
os dados aleatoriamente a cada iteração. Essa é uma estratégia bastante comum
quando se usa o algoritmo de gradiente descendente estocástico.

Em seguida, dividimos os dados de treinamento em lotes com alguns exemplos,
também conhecido como "minibatching". Isso aumenta a confiança das estimativas
do gradiente.

Finalmente, atualizamos o modelo após processar cada lote, e reiniciamos o loop
até finalizarmos a última iteração.

Então podemos salvar o modelo em um diretório e usá-lo na spaCy.

---

# Recapitulando: Como o treinamento funciona

<img src="/training.png" alt="Diagrama do processo de treinamento" />

- **Dados de treinamento:** Exemplos e suas anotações.
- **Texto:** O texto de entrada que o modelo deve prever um rótulo associado.
- **Rótulo:** O rótulo que o modelo deve prever.
- **Gradiente:** Como mudar os pesos do modelo.

Notes: Recapitulando:

Os dados de treinamento são os exemplos que desejamos utilizar para atualizar
o modelo.

O texto pode ser uma frase, parágrafo ou documento. Para melhores resultados,
ele deve ser similar aos textos que o modelo encontrará quando rodar suas
previsões.

O rótulo é o resultado que desejamos obter com a previsão do modelo. Pode ser a categoria
do texto, ou identificação de entidades e seus tipos.

O gradiente define como o modelo deve alterar seus pesos para reduzir o erro atual, 
que é calculado quando comparamos os dados previstos com os resultados esperados 
(reais).

---

# Exemplo de um loop

```python
TRAINING_DATA = [
    ("How to preorder the iPhone X", {"entities": [(20, 28, "GADGET")]})
    # E muitos outros exemplos...
]
```

```python
# Loop por 10 iterações
for i in range(10):
    # Embaralhar os dados de treinamento
    random.shuffle(TRAINING_DATA)
    # Criar lotes e iterar 
    for batch in spacy.util.minibatch(TRAINING_DATA):
        # Dividir o lote em textos e anotações
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Atualizar o modelo
        nlp.update(texts, annotations)

# Salvar o modelo 
nlp.to_disk(path_to_model)
```

Notes: Aqui está um exemplo:

Vamos imaginar que temos uma lista de exemplos de treinamento consistindo de
texto e anotações de entidades.

Queremos executar o laço (loop) por 10 vezes, portanto nossa iteração terá um
alcance (`range`) de 10.

Em seguida , usamos o módulo `random` para embaralhar os dados de treinamento
aleatoriamente.

Então usamos a função da spaCy `minibatch` para agrupar os exemplos em lotes.

Para cada lote, obtemos os textos e anotações e chamamos o método `nlp.update`
para atualizar o modelo.

Por fim, usamos `nlp.to_disk` para salvar o modelo treinado em um diretório.

---

# Atualizando um modelo existente

- Melhora as previsões para novos dados
- Muito útil para estender categorias existentes, como `"PERSON"`
- Também é possível adicionar novas categorias.
- Atenção! Garanta que o modelo não irá "esquecer" a classificação já aprendida.

Notes: A spaCy permite que você atualize um modelo pré-treinado com mais
dados, para por exemplo, melhorar as previsões em diferentes textos.

Isso é especialmente útil se você deseja adicionar exemplos a um modelo
existente, como "person" ou "organization".

E você também pode atualizar um modelo existente com novas categorias.

Mas tenha cuidado e garanta que seus dados de treinamento contenham 
exemplos das novas categorias _e_ exemplos das categorias previamente
aprendidas, senão você corre o risco de prejudicar o que já foi aprendido
anteriormente.

---

# Definindo um novo fluxo de processamento a partir do zero

```python
# Começar com o modelo vazio da língua inglesa
nlp = spacy.blank("en")
# Criar identificador de entidades vazio, e adicionar ao fluxo de processamento
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Adicionar um novo rótulo
ner.add_label("GADGET")

# Iniciar o treinamento
nlp.begin_training()
# Treinar por 10 iterações
for itn in range(10):
    random.shuffle(examples)
    # Dividir os exemplos em lotes
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Atualizar o modelo
        nlp.update(texts, annotations)
```

Notes: Neste exemplo, começamos com o modelo da língua inglesa vazio, através
do comando `spacy.blank`. O modelo vazio não tem nenhum componente no fluxo
de processamento, apenas os dados do idioma e as regras de toquenização.

Então criamos um identificador de entidades e o adicionamos ao fluxo de
processamento.

Utilizando o método `add_label`, podemos adicionar novos rótulos ao modelo.

Em seguida chamamos `nlp.begin_training` para inicializar o modelo com pesos 
aleatórios.

Para obter uma melhor acurácia, desejamos iterar nos exemplos mais de uma
vez e embaralhar aleatoriamente os dados a cada iteração.

A cada iteração, agrupamos os exemplos em lotes usando a função da spaCy
`spacy.util.minibatch`. Cada exemplo consiste no texto e suas anotações.

Por último, atualizamos o modelo com os textos e anotações e seguimos com
o loop.

---

# Vamos praticar!

Notes: É hora de praticar! Agora que você já conhece o loop de treinamento, vamos
usar os dados criados no exercício anterior para atualizar um modelo.
