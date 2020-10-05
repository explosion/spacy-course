TRAINING_DATA = [
    (
        "去年アスムテルダムに行った。運河がきれいだった。",
        {"entities": [(2, 9, "TOURIST_DESTINATION")]},
    ),
    (
        "人生で一度はパリに行くべきだけど、エッフェル塔はちょっとつまらないな。",
        {"entities": [(6, 8, "TOURIST_DESTINATION")]},
    ),
    ("アーカンソーにもパリはあるｗ", {"entities": []}),
    (
        "ベルリンは夏が最高！公園がたくさんあって、夜遊びが充実していて、ビールが安い！",
        {"entities": [(0, 4, "TOURIST_DESTINATION")]},
    ),
]
