def test():
    assert (
        len(pattern1) == 2
    ), "Die Anzahl der Tokens im pattern1 passt nicht zu der tatsächlichen Anzahl an Tokens im String."
    assert (
        len(pattern2) == 4
    ), "Die Anzahl der Tokens im pattern2 passt nicht zu der tatsächlichen Anzahl an Tokens im String."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "Der erste Token im pattern1 sollte ein Attribut enthalten."
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "Überprüfe das Attribut und seinen Wert im ersten Token von pattern1."
    assert (
        len(pattern1[1]) == 2
    ), "Der zweite Token von pattern1 sollte zwei Attribute enthalten."
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Überprüfe die Attribute und Werte des zweiten Tokens von pattern1."
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Überprüfe die Attribute und Werte des zweiten Tokens in pattern1."

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "Überprüfe die Attribute und Werte des ersten Tokens von pattern2."
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "Überprüfe die Attribute und Werte des dritten Tokens von pattern2."
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Überprüfe die Attribute und Werte des vierten Tokens von pattern2."
    assert len(matcher(doc)) == 6, "Leider die falsche Anzahl an Resultaten – erwartet sind 6."

    __msg__.good(
        "Gut gemacht! Um den Token '-' zu finden, kannst du das Attribut 'TEXT', "
        "'LOWER' oder sogar 'SHAPE' verwenden. Alle sind korrekt. Wie du sehen "
        "kannst ist es sehr wichtig, besonderes Augenmerk auf die Tokenisierung "
        "zu richten, wenn du mit dem Token-basierten Matcher arbeitest. Manchmal "
        "ist es einfacher, stattdessen nur exakte Strings zu suchen und den "
        "PhraseMatcher zu verwenden. Diesen schauen wir uns in der nächsten "
        "Übung an."
    )
