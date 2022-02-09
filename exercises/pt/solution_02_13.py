import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_md")
doc = nlp(
    " Twitch Prime, um programa de regalias para os membros da Amazon Prime que "
    " oferece saques gratuitos, jogos e outros benefícios, está abandonando uma "
    " de suas melhores funcionalidades: visualização sem anúncios . De acordo com "
    " um email enviado hoje aos membros da Amazon Prime, a partir de 14 de Setembro, "
    " a visualização sem anúncios não estará mais inclusa no Twitch Prime para novos "
    " membros. No entanto, membros com assinaturas anuais poderão desfrutar da "
    " visualização sem anúncios até o momento da renovação da assinatura. Aqueles com "
    " assinaturas mensais terão acesso à visualização sem anúncios até 15 de Outubro."
)
    
# Criar as expressões para correspondência
pattern1 = [{"LOWER": "amazon"}, {"IS_TITLE": True, "POS": "PROPN"}]
pattern2 = [{"POS": "NOUN"},{"LOWER": "sem"}, {"LOWER": "anúncios"}]

# Inicializar o Matcher e adicionar as expressões
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", [pattern1])
matcher.add("PATTERN2", [pattern2])

# Iterar nos resultados
for match_id, start, end in matcher(doc):
    # Imprimir o nome e texto da partição 
    print(doc.vocab.strings[match_id], doc[start:end].text)
