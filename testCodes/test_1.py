def test_1():
    x = 10
    y = 20
    assert x != y


def test_2():
    name = "Orange"
    title = "Orange is a color"
    assert name in title


def test_3():
    name = "Jenkins"
    title = "Jenkins is CI server"
    assert name in title, "Title does no match"
