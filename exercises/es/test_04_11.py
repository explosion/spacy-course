def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("Venecie", "LOC")
    ], "Revisa las entidades en el primer ejemplo."
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ('Madrid', 'LOC'), ('museo prado', 'LOC')
    ], "Revisa las entidades en el segundo ejemplo."
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ('Madrid', 'LOC'),
        ('Colombia', 'LOC')
    ], "Revisa las entidades en el tercer ejemplo."
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ('Berlín', 'LOC')
    ], "Revisa las entidades en el cuarto ejemplo."

    __msg__.good(
        "¡Excelente trabajo! Una vez que el modelo obtiene buenos resultados "
        "en la detección de entidades de tipo LOC en entities in the opiniones "
        "de viajeros, podrías agregar un componente basado en reglas para "
        "determinar si es que la entidad es un destino turístico en este "
        "contexto. Por ejemplo, podrías resolver los tipos de entidades de "
        "regreso a una base de conocimiento o buscarlos en un wiki de viajes"
    )
