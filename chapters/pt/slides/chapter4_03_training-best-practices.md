---
type: slides
---

# Melhores práticas para treinar modelos na spaCy

Notes: Quando você começar a rodar seus próprios experimentos, você provavelmente
irá descobrir várias coisas que não funcionam do jeito que você deseja. E tudo bem!

Treinar modelos é um processo de melhoria, onde você deve tentar diversas
estratégias até descobrir aquilo que funciona melhor para seu projeto.

Nesta lição, vou dividir com vocês algumas das melhores práticas de treinamento
e apontar algumas coisas que você precisa ter em mente quando estiver
treinando seus próprios modelos.

Vamos dar uma olhada nos possíveis problemas que você provavelmente irá se deparar.

---

# Problema 1: Modelos podem "esquecer" coisas

- Um modelo existente pode superajustar (overfit) com os novos dados.
  - Exemplo: se você apenas atualizar seu modelo com dados de `"WEBSITE"`, 
    ele pode "desaprender" o que é um `"PERSON"`
- Também conhecido como o problema do "esquecimento catastrófico".

Notes: Modelos estatísticos podem aprender muitas coisas, mas eles também podem "desaprender" essas coisas.

Se você estiver atualizando um modelo existente com novos dados, principalmente
se forem novos rótulos, o modelo pode se _superajustar_ (overfit) aos novos exemplos.

Como exemplo, se você estiver atualizando seu modelos com exemplos de "WEBSITE",
o modelo pode esquecer dos outros rótulos aprendidos anteriormente, como "PERSON".

Isso é conhecido como o problema do esquecimento catastrófico.

---

# Solução 1: Misture previsões anteriores corretas

- Por exemplo, se você estiver treinando com dados de `"WEBSITE"`, também inclua
  exemplos de `"PERSON"`
- Rode o modelo existente da biblioteca spaCy e extraia todas as outras entidades relevantes.

Note: Para prevenir esse problema, garanta que seus exemplos incluam também os
exemplos daquilo que o modelo previu corretamente anteriormente.

Se você estiver treinando uma nova categoria `"WEBSITE"`, inclua também exemplos de
`"PERSON"`.

A spaCy pode te ajudar com isso. Você pode criar esses exemplos adicionais necessários
simplesmente rodando o modelo existente em alguns textos e extraindo as partições
de entidades que você deseja preservar.

Você pode então adicionar esses exemplos aos seus dados de treinamento e atualizar
o modelo com todas essas anotações de entidades.

---

# Problema 2: Modelos não podem aprender tudo

- Os modelos da spaCy's fazem suas previsões baseados no **contexto local**
- Um modelo pode ter dificuldade para aprender se a decisão estiver baseada em algum contexto complexo.
- A estratégia de rotulação deve ser consistente e não muito específica
  - Exemplo: `"CLOTHING"` é melhor que `"ADULT_CLOTHING"` e
    `"CHILDRENS_CLOTHING"`

Notes: Outro problema comum é que seu modelo nem sempre aprende aquilo que
você deseja.

Os modelos da spaCy fazem previsões baseados no contexto local. Por exemplo:
para entidades nomeadas, as palavras ao seu redor são bastante importantes.

Se a decisão que precisa ser tomada é difícil e deve ser feita baseada no contexto,
o modelo pode ter muita dificuldade para treinar corretamente.

A estratégia de definição dos rótulos também precisa ser consistente e não 
deve ser muito específica.

Por exemplo, será difícil ensinar um modelo a prever se alguma coisa é uma
roupa de adulto ou roupa de criança baseando-se no contexto local. Por outro
lado, prever apenas roupa deve ser mais fácil e eficiente.

---

# Solução 2: Planeje sua estratégia de rótulos com cuidado

- Escolha categorias que se refletem no contexto local
- Mais genérico é melhor que muito específico
- Para estimar categorias específicas, use regras.


**RUIM:**

```python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

**BOM:**

```python
LABELS = ["CLOTHING", "BAND"]
```

Notes: Antes de iniciar o treinamento e a atualização dos modelos, vale a pena
dar um passo para trás e planejar seu esquema de rotulação.

Tente escolher categorias que são refletidas no contexto local do texto e garanta
que elas sejam o mais genéricas possível.

Você sempre pode adicionar um sistema baseado em regras em seguida para separar
a categoria em outras mais específicas.

Categorias genéricas como "clothing" e "band" são mais fáceis de rotular e de aprender.

---

# Vamos praticar!

Notes: Vamos agora dar uma olhada nesses problemas em seu contexto e consertá-los!
