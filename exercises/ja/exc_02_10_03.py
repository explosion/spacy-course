import spacy

nlp = spacy.load("ja_core_news_md")

doc = nlp("素晴らしいレストランでした。その後、私達はとても素敵なバーに行きました。")

# 「素晴らしいレストラン」と「とても素敵なバー」のスパンを作る
span1 = ____
span2 = ____

# スパンの類似度をはかる
similarity = ____.____(____)
print(similarity)
