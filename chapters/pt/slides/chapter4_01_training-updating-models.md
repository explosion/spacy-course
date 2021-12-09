---
type: slides
---

# Treinando e atualizando modelos

Notes: Bem-vindo ao capítulo final, que vai tratar de um dos aspectos mais
entusiasmantes do processamento de linguagem natural moderno: treinar seus modelos!

Nesta lição, você aprenderá sobre o treinamento e a atualização dos modelos
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
para nós mesmos: Para que queremos atualizar um modelo com nossos próprios exemplos?
Por que não podemos simplesmente confiar nos modelos que já foram treinados ?

Modelos estatísticos fazem previsões baseadas nos exemplos nos quais foram treinados.

Normalmente você poderá fazer um modelo com melhor acurácia ao apresentar exemplos
do seu próprio domínio.

Na maioria das vezes você também deseja categorizar os textos de acordo com o seu
problema, portanto o modelo precisa aprender isso também.

Esse passo é essencial para a classificação de textos. É muito útil para identificadores
de entidades e bem menos crítico para tagueamento de classes gramaticas e análise 
sintática.

---

# Como o treinamento funciona (1)

1. **Inicializa** os pesos do modelo com valores aleatórios com `nlp.begin_training`
2. **Prevê** alguns exemplos utilizando os pesos atuais com `nlp.update`
3. **Compara** previsões com os resultados reais
4. **Calcula** como alterar os pesos para melhorar as previsões
5. **Atualiza** ligeiramente os pesos do modelo
6. Volta para 2.

Notes: A biblitoeca spaCy oferece suporte para atualizar os modelos existentes com mais exemplos, e
treinar novos modelos.

Se não estamos iniciando com um modelo pré-treinado, o primeiro passo é inicializar
os pesos do modelo com valores aleatórios.

Em seguida, chamamos `nlp.update`, que fará a previsão de um lote de exemplos utilizando
os pesos atuais.

O algoritmo então compara as previsões com os valores corretos, e decide como alterar
os pesos de forma a obter melhores previsões na próxima rodada.

Finalmente, fazemos uma pequena alteração nos pesos do modelo e seguimos para a 
próxima rodada de exemplos.

Continuamos chamando `nlp.update` para cada lote de exemplos dos dados.

---

# Como o treinamento funciona (2)

<img src="/training.png" alt="Diagram of the training process" />

- **Training data:** Dados de treinamento: exemplos e seus rótulos.
- **Text:** Texto: o texto de entrada que o modelo deve realizar a previsão.
- **Label:** Rótulo ou marcador: o resultado da previsão do modelo.
- **Gradient:** Gradiente: define como o modelo deve alterar seus pesos.

Notes: Aqui está uma ilustração do processo:

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

Após o treinamento, podemos salvar o modelo atualizado e usá-lo em nossas aplicações.

---

# Exemplo: Treinando o identificador de entidades

- O identificador de entidades reconhece palavras e frases dentro de seu contexto
- Cada token pode pertencer a apenas uma entidade
- Os exemplos precisam apresentar um contexto

```python
("iPhone X is coming", {"entities": [(0, 8, "GADGET")]})
```

- Textos que não contenham entidades também são importantes

```python
("I need a new phone! Any tips?", {"entities": []})
```

- **Objetivo:** ensinar o modelo a generalizar

Notes: Vamos dar uma olhada em um componente importante: o identificador de entidades.

O identificador de entidades recebe um documento e prevê frases e seus marcadores.
Isso significa que os dados de treinamento necessitam incluir textos, as entidades e
seus marcadores.

Entidades não podem ser sobrepostas, então cada token (ou palavra) só pode pertencer
a uma entidade.

Devido ao fato que o identificador de entidades prevê entidades _dentro de um contexto_,
o modelo precisa ser treinado com as entidades _e_ o contexto que estão inseridas.

A forma mais fácil de se fazer isso é apresentar ao modelo um texto e um intervalo de 
caracteres. Por exemplo: "iPhone X" é um "gadget" que começa no caracter na posição 0 e 
termina no caracter na posição 8.

É também muito importante que o modelo aprende palavras que _não são_ entidades.

Neste caso, os marcadores do intervalo de caracter devem ser vazios.

Nosso objetivo é ensinar o modelo a reconhecer novas entidades em contextos
similares, mesmo que elas não estejam nos dados de treinamento.

---

# Os dados de treinamento

- Examplos daquilo que queremos que o modelo faça a previsão, em um dado contexto
- Para atualizar um **modelo existente**: poucas centenas ou poucos milhares de exemplos
- Para treinar uma **nova categoria**: alguns poucos milahres até milhões de exemplos
  - o modelo da biblioteca spaCy para o Inglês tem 2 milhões de palavaras
- Normalmente é criado manualmente por anotadores humanos
- Pode ser semi-automatizada usando, por exemplo, o Comparador `Matcher`!

Notes: Os dados de treinamento dizem ao modelo aquilo que ele precisa prever. Pode
ser texto ou entidades que desejamos reconhecer, ou palavras e suas classes gramaticais.

Para atualizar um modelo existente, podemos começar com algumas poucas centenas a
milhares de palavras.

Para treinar uma nova categoria, podemos precisar de até milhões de palavras.

O modelo da biblioteca spaCy para o Inglês, por exemplo, foi treinados com 2 milhões
de palavras anotadas com classes gramaticais, termos sintáticos e entidades nomeadas.

Os dados de treinamento normalmente são criados por humanos, que atribuiem marcadores
aos textos.

Isso representa muito trabalho, mas pode ter algumas etapas automatizadas, como por
exemplo, utilizando o Comparador `Matcher` da biblioteca spaCy.


---

# Vamos praticar!

Notes: Agora é hora de começar o trabalho e preparar os dados de treinamento.
Vamos dar uma olhada em um exemplo e criar uma pequena base de dados para uma nova
entidade.
