import spacy

nlp = spacy.load("ja_core_news_md")

doc = nlp("素晴らしいレストランでした。その後、私達はとても素敵なバーに行きました。")

# 「素晴らしいレストラン」と「とても素敵なバー」のスパンを作る
span1 = doc[0:2]
span2 = doc[11:15]

# スパンの類似度をはかる
similarity = span1.similarity(span2)
print(similarity)
