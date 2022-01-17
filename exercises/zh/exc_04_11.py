import spacy
from spacy.tokens import Span

nlp = spacy.blank("zh")

doc1 = nlp("我去年去了西安，那里的城墙很壮观！")
doc1.ents = [Span(doc1, 5, 7, label="TOURIST_DESTINATION")]

doc2 = nlp("人一辈子一定要去一趟巴黎，但那里的埃菲尔铁塔有点无趣。")
doc2.ents = [Span(doc2, 10, 12, label="TOURIST_DESTINATION")]

doc3 = nlp("深圳也有个巴黎的埃菲尔铁塔，哈哈哈")
doc3.ents = []

doc4 = nlp("北京很适合暑假去：长城、故宫，还有各种好吃的小吃！")
doc4.ents = [Span(doc4, 0, 2, label="TOURIST_DESTINATION")]
