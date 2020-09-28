import twitterapi

def test_results():
    assert twitterapi.choose_username("realmadrid") == 0


if __name__ == "__main__":
    test_results()
