---
type: slides
---

# Treinando e atualizando modelos

Notes: Bem-vindo ao capítulo final, que vai tratar de um dos aspectos mais
entusiasmantes do processamento de linguagem natural moderno: treinar seus modelos!

Nesta lição, você irá aprender sobre o treinamento e a atualização dos modelos
de redes neurais da spaCy e os dados necessários para isso - com foco principal
no identificador de entidades nomeadas.

---

# Por que atualizar o modelo?

- Resultados melhores para seu domínio específico
- Aprende esquemas de classificação adequados ao seu problema
- Essencial para classificação de textos
- Muito útil para reconhecimento de entidades nomeadas
- Menos crítico para tagueamento de classes gramaticas e análise sintática


Notes: Antes de entrarmos nos detalhes do _como_, vale a pena fazermos uma pergunta
para nós mesmos: Para que queremos atualizar o modelo com nossos próprios exemplos?
Por que não podemos simplesmente confiar nos modelos que já foram treinados ?

Modelos estatísticos fazem previsões baseadas nos exemplos nos quais foram treinados.

Normalmente você poderá fazer um modelo com melhor acurácia ao apresentar exemplos
do seu próprio domínio.

Na maioria das vezes você também deseja categorizar os textos de acordo com o seu
problema, portanto o modelo precisa aprender isso também.

Esse passo é essencial para a classificação de textos muito útil para identificadores
de entidades e bem menos crítico para tagueamento debclasses gramaticas e análise 
sintática.

---

# Como o treinamento funciona (1)

1. **Inicializa** os pesos do modelo com valores aleatórios com `nlp.begin_training`
2. **Prevê** alguns exemplos utilizando os pesos atuais com `nlp.update`
3. **Compara** previsões com os resultados reais
4. **Calcula** como alterar os pesos para melhorar as previsões
5. **Atualiza** ligeiramente os pesos do modelo
6. Volte para 2.

Notes: A spaCy dá suporte para atualizar os modelos existentes com mais exemplos, e
treinar novos modelos.

Se não estamos iniciando com um modelo pré-treinado, o primeiro passo é inicializar
os pesos do modelo com valores aleatórios.

Em seguida, chamamos `nlp.update`, que fará a previsão de um lote de exemplos utilizando
os pesos atuais.

O modelo então compara as previsões com os valores corretos, e decide como alterar
os modelos de forma a obter melhores previsões na próxima rodada.

Finalmente, fazemos uma pequena alteração nos pesos do modelo e seguimos para a 
próxima rodada de exemplos.

Continuamos chamando `nlp.update` para cada lote de exemplos dos dados.

---

# Como o treinamento funciona (2)

<img src="/training.png" alt="Diagram of the training process" />

- **Training data:** Examples and their annotations.
- **Text:** The input text the model should predict a label for.
- **Label:** The label the model should predict.
- **Gradient:** How to change the weights.

Notes: Here's an illustration showing the process.

The training data are the examples we want to update the model with.

The text should be a sentence, paragraph or longer document. For the best
results, it should be similar to what the model will see at runtime.

The label is what we want the model to predict. This can be a text category, or
an entity span and its type.

The gradient is how we should change the model to reduce the current error. It's
computed when we compare the predicted label to the true label.

After training, we can then save out an updated model and use it in our
application.

---

# Exemplo: Treinando o identificador de entidades

- The entity recognizer tags words and phrases in context
- Each token can only be part of one entity
- Examples need to come with context

```python
("iPhone X is coming", {"entities": [(0, 8, "GADGET")]})
```

- Texts with no entities are also important

```python
("I need a new phone! Any tips?", {"entities": []})
```

- **Objetivo:** teach the model to generalize

Notes: Let's look at an example for a specific component: the entity recognizer.

The entity recognizer takes a document and predicts phrases and their labels.
This means that the training data needs to include texts, the entities they
contain, and the entity labels.

Entities can't overlap, so each token can only be part of one entity.

Because the entity recognizer predicts entities _in context_, it also needs to
be trained on entities _and_ their surrounding context.

The easiest way to do this is to show the model a text and a list of character
offsets. For example, "iPhone X" is a gadget, starts at character 0 and ends at
character 8.

It's also very important for the model to learn words that _aren't_ entities.

In this case, the list of span annotations will be empty.

Our goal is to teach the model to recognize new entities in similar contexts,
even if they weren't in the training data.

---

# Os dados de treinamento

- Examples of what we want the model to predict in context
- Update an **existing model**: a few hundred to a few thousand examples
- Train a **new category**: a few thousand to a million examples
  - spaCy's English models: 2 million words
- Usually created manually by human annotators
- Can be semi-automated – for example, using spaCy's `Matcher`!

Notes: The training data tells the model what we want it to predict. This could
be texts and named entities we want to recognize, or tokens and their correct
part-of-speech tags.

To update an existing model, we can start with a few hundred to a few thousand
examples.

To train a new category we may need up to a million.

spaCy's pre-trained English models for instance were trained on 2 million words
labelled with part-of-speech tags, dependencies and named entities.

Training data is usually created by humans who assign labels to texts.

This is a lot of work, but can be semi-automated – for example, using spaCy's
`Matcher`.

---

# Vamos praticar!

Notes: Now it's time to get started and prepare the training data. Let's look at
some examples and create a small dataset for a new entity type.
