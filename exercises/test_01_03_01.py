def test():
    assert "cost = bananaPrice * numberOfBanana" in __solution__ or "cost = bananaPrice *numberOfBanana" in __solution__, "Did you forget to check how many bananas you bought?"
    __msg__.good("Nicely done!")
