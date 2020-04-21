TRAINING_DATA = [
    (
        "ich war letztes jahr in amsterdem und die kanäle warn superschön",
        {"entities": [(24, 33, "TOURISTENZIEL")]},
    ),
    (
        "Du solltest einmal im Leben Paris besuchen, aber der Eiffelturm ist relativ langweilig",
        {"entities": [(28, 33, "TOURISTENZIEL")]},
    ),
    ("Es gibt auch ein Paris in Arkansas lol", {"entities": []}),
    (
        "Berlin ist perfekt für einen Sommerurlaub: viele Parks, tolles Nachleben, günstiges Bier!",
        {"entities": [(0, 6, "TOURISTENZIEL")]},
    ),
]
