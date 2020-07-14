TRAINING_DATA = [
    (
        "je suis allé à amsterdem l'an dernier et les canaux étaient magnifiques",
        {"entities": [(15, 24, "TOURIST_DESTINATION")]},
    ),
    (
        "Tu devrais visiter Paris au moins une fois dans ta vie, mais la Tour Eiffel ce n'est pas terrible",
        {"entities": [(19, 24, "TOURIST_DESTINATION")]},
    ),
    ("Il y a aussi un Paris dans l'Arkansas, lol", {"entities": []}),
    (
        "Berlin est la destination parfaite pour les vacances d'été : beaucoup de parcs, une vie nocturne trépidante et de la bière pas chère !",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
