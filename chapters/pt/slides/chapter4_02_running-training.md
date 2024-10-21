---
type: slides
---

# Configurando e executando o treinamento

Notes: Agora que você já aprendeu como criar dados de treinamento, vamos dar
uma olhada no treinamento e na configuração do fluxo de processamento (pipeline).
Nesta lição, você vai aprender tudo sobre a configuração do processo de
treinamento: como gerar seu arquivo de configuração, como usar o comando CLI 
para treinar um modelo e como explorar seu fluxo de processamento após o 
treinamento.

---

# O arquivo config de treinamento (1)

- **Única fonte de informação** para todas as configurações
- Por convenção chama-se `config.cfg`
- Define como inicializar o objeto `nlp`
- Inclui todas as configurações dos componentes do fluxo de processamento (pipeline) e seus modelos implementados
- Configura o processo de treinamento e os hyper-parâmetros
- Permite que seu processo de treinamento seja reproduzível

Notes: A spaCy utiliza um arquivo de configuração, normalmente chamado de `config.cfg`
como a única fonte para todas as configurações. O arquivo config estabelece como inicializar
o objeto `nlp`, quais componentes do fluxo de processamento devem ser utilizados e
como as suas implementações internas devem ser configuradas. Ele também inclui todas
as configurações para o processo de treinamento e como carregar os dados, e até os
hyper-parâmetros.

Ao invés de adicionar vários parâmetros na linha de comando e ter que lembrar como
definir as configurações dentro do código, basta apenas incluir o arquivo de configuração
na linha de comando para o treinamento.

Os arquivos de configuração ajudam na reprodutibilidade do seu fluxo de processamento:
todas as configurações necessárias estão em apenas um lugar e podem ser verificadas.
Você pode incluir seu arquivo de configuração em um repositório Git e compartilhar com
outras pessoas, permitindo que elas façam o mesmo treinamento do seu fluxo de 
processamento, exatamente da mesma maneira.

---

# O arquivo config de treinamento (2)

```ini
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000
[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"
[components]
[components.ner]
factory = "ner"
[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# E assim por diante...
```

Notes: Este é um trecho de um arquivo de configuração utilizado para treinar
um fluxo de processamento (pipeline) de um identificador de entidades nomeadas.
O arquivo de configuração é organizado em seções, e as seções aninhadas são
definidas através de um ponto. Por exemplo:  `[components.ner.model]` define
as configurações para a implementação do modelo do identificador de entidades
nomeadas.

Os arquivos de configuração podem referenciar funções Python utilizando a notação 
`@`. Por exemplo: o toquenizador define uma função registrada de um toquenizador.
Você pode utilizar esse recurso para personalizar partes do objeto `nlp` e do treinamento,
como adicionar seu próprio toquenizador ou até implementar sua própria arquitetura
do modelo. Mas por ora não vamos nos preocupar com isso. O que você aprenderá neste
capítulo utilizará as opções padrão disponíveis na biblioteca spaCy!

---

# Gerando um arquivo config

- A spaCy pode gerar automaticamente um arquivo config com as configurações padrão
- Interativamente: [ferramenta de inicialização rápida](https://spacy.io/usage/training#quickstart)
- Linha de comando: [`init config`](https://spacy.io/api/cli#init-config) 

```bash
$ python -m spacy init config ./config.cfg --lang en --pipeline ner
```

- `init config`: o comando a ser executado
- `config.cfg`: caminho para o arquivo que será gerado
- `--lang`: idioma do fluxo de processamento (pipeline). Ex: `en` para o Inglês
- `--pipeline`: componentes que devem ser incluídos, separados por vírgula

Notes: É claro que não é necessário definir o arquivo de configuração manualmente.
Na maioria das vezes nem será necessário personalizar este arquivo. A biblioteca
spaCy pode gerar este arquivo automaticamente para você.

A ferramenta de inicialização rápida presente na documentação permite que você 
gere seu arquivo de configuração de maneira interativa. É possível selecionar o idioma,
os componentes do fluxo de processamento necessários, o hardware opcional e
os objetivos da otimização.

Alternativamente, você pode utilizar o comando da spaCy `init config`. Ele
recebe o nome do arquivo de saída como primeiro argumento. Normalmente esse
arquivo é chamado de `config.cfg`. O argumento `--lang` define o idioma que
será utilizado no fluxo de processamento, por exemplo: `pt` para o Português.
O argumento `--pipeline` permite especificar um ou mais componentes do fluxo de
processamento, que devem ser separados por vírgula. Neste exemplo, estamos 
criando um arquivo de configuração com apenas um componente: o identificador 
de entidades nomeadas.

---

# Treinando um fluxo de processamento (pipeline) (1)

- Tudo o que você precisa é o arquivo `config.cfg` e os dados de treinamento e validação
- Configurações podem ser sobrescritas na linha de comando

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train`: o comando que deve ser executado
- `config.cfg`: o caminho para o arquivo de configuração
- `--output`: o caminho do diretório de saida para salvar o fluxo de processamento treinado
- `--paths.train`: sobrescrever com o caminho para os dados de treinamento
- `--paths.dev`: sobrescrever com o caminho para os dados de validação

Notes: Para treinar um fluxo de processamento (pipeline), tudo o que você precisa
é o arquivo de configuração e os dados de treinamento e validação. Esses são os
arquivos `.spacy`com os quais você já trabalhou no exercício anterior.

O primeiro argumento de `spacy train` é o caminho para o arquivo de configuração.
O argumento `--output` permite especificar um diretório para salvar o fluxo
de processamento treinado.

Você também pode sobrescrever configurações definidas no arquivo de configuração
na própria linha de comando. Neste caso, sobrescrevemos o caminho para o arquivo
`train.spacy` utilizando o argumento `paths.train` e sobrescrevemos o caminho para
o arquivo `dev.spacy` utilizando o argumento `paths.dev`.

---

# Treinando um fluxo de processamento (pipeline) (2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57
✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: Este é um exemplo das informações que serão apresentadas durante
e depois do treinamento. Não se esqueça que é desejável fazer diversas passadas
nos dados durante o treinamento, como já foi apresentado anteriormente. Cada
passada nos dados é conhecida como `epoch`. Esta informação está na primeira
coluna da tabela.

A cada passo (`epoch`), a biblioteca spaCy mostra a pontuação de acurácia
para os 200 exemplos do passo. A quantidade de exemplos já treinados é apresentada na
segunda coluna. Você pode alterar essa frequência no arquivo de configuração.
Cada linha também mostra a perda e a pontuação de acurácia calculada a cada passo.

A pontuação mais importante para acompanhar é o score apresentado na
última coluna. Ele reflete o quão corretamente o modelo previu os dados de validação.

O treinamento é executado até que o modelo deixe de melhorar, quando automaticamente
finaliza a execução.

---

# Carregando um fluxo de processamento (pipeline) treinado

- Ao finalizar o treinamento, o resultado é um fluxo de processamento que pode ser carregado.
  - `model-last`: o último fluxo de processamento (pipeline) treinado
  - `model-best`: o melhor fluxo de processamento (pipeline) treinado
- Carregue o fluxo com o comando `spacy.load`

```python
import spacy
nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)
```

Notes: O fluxo de processamento disponível após o treinamento é um fluxo de processamento
que pode ser carregado, similar aos fluxos de processamento treinados disponíveis na biblioteca
spaCy, como por exemplo: `en_core_web_sm`. Ao final do processo de treinamento, o último fluxo de
processamento treinado e o fluxo com o melhor score são salvos no diretório de saída.

Você pode carregar seu fluxo de processamento treinado passando seu caminho como parâmetro
no comando `spacy.load`. Em seguida, você pode usar seu modelo para processar e analisar
texto.

---

# Dica: Empacotando seu fluxo de processamento (pipeline)

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): cria um pacote Python instalável contendo seu fluxo de processamento
- Fácil para controle de versões e para a implantação (deployment)

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
```

```bash
$ cd ./packages/en_my_pipeline-1.0.0
$ pip install dist/en_my_pipeline-1.0.0.tar.gz
```

Carregue e utilize o fluxo de processamento após a sua instalação:

```python
nlp = spacy.load("en_my_pipeline")
```

Notes: Para facilitar a implantação de seus fluxos de processamento, a biblioteca
spaCy oferece um comando muito útil para empacotá-los como pacotes Python. O
comando `spacy package` necessita do caminho para o fluxo de processamento salvo 
e um diretório de saída. Ele gera um pacote Python contendo seu fluxo de processamento.
O pacote Python é um arquivo do tipo `.tar.gz` e pode ser instalado em seu ambiente
de trabalho.

Na linha de comando você também pode informar nome e versão. Isso permite
gerenciar múltiplas versões do fluxo de processamento. É possível, por exemplo,
personalizar seu fluxo de processamento posteriormente ou treiná-lo com dados adicionais,
mantendo o controle das versões.

O pacote é similar a qualquer pacote Python. Após a instalação, você pode carregar o
fluxo de processamento pelo seu nome. Note que a spaCy automaticamente adicionará
o código do idioma ao nome do pacote. Por exemplo: `my_pipeline` será salvo como
`en_my_pipeline`.

---

# Vamos praticar!

Notes: Vamos ao trabalho! Vamos treinar seu primeiro fluxo de processamento.
Você irá gerar seu arquivo de configuração para um identificador de entidades
nomeadas e treinar um fluxo de processamento utilizando os dados utilizados
nos exercícios anteriores.
