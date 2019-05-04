def test():
    assert (
        len(daysByMonth) == 12
    ), "daysByMonth should have a length of 12."
    assert len(monthByDays["31"]) == 7 and len(monthByDays["30"]) == 4, "Is the monthByDays dictionary correct?."
    __msg__.good("Well done!")
