日本語への翻訳時のメモ:

statistical model: 直訳すると「統計モデル」だが、「機械学習モデル」ということが多い。

UD の用語の参考: https://www.jstage.jst.go.jp/article/jnlp/26/1/26_3/_pdf/-char/ja

""は「」に

lemma -> 見出し語

lexeme -> 語彙素

v3の翻訳メモ:

training data -> 学習データ (not 訓練データ)
validation data -> 検証データ
training (a model) -> 訓練
training (spaCy feature) -> トレーニング

config file -> 設定ファイル (not コンフィグ)

v2 と比べて「model」がより狭義で使われるようになり、「機械学習モデル」はほとんど「機械学習パイプライン」になった。
特に、spaCyが提供する`ja_core_news_sm`などは「パイプライン」と呼ぶ。
