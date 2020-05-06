import spacy

# en_core_web_sm モデルをロード
nlp = spacy.load("en_core_web_sm")

# パイプラインの名前をプリント
print(nlp.pipe_names)

# (name, component) のタプルからなるパイプライン情報をプリント
print(nlp.pipeline)
