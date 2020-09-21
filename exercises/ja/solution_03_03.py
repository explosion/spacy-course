import spacy

# ja_core_news_sm モデルを読み込む
nlp = spacy.load("ja_core_news_sm")

# パイプラインの名前を出力
print(nlp.pipe_names)

# (name, component) のタプルからなるパイプライン情報を表示
print(nlp.pipeline)
