import datafunctions as dfn


def test_increment():
    assert dfn.increment(2) == 3


def test_strip_punctuation_1():
    mystring = 'Lets see what. this does, to my sentence!'
    correctedstring = 'Lets see what this does to my sentence'
    assert dfn.strip_punctuation(mystring) == correctedstring


def test_bag_of_words_1():
    mystring = 'Lets see what. this does, to my sentence!'
    test_set = {'Lets', 'does', 'my', 'see', 'sentence', 'this', 'to', 'what'}
    assert dfn.bag_of_words(mystring) == test_set
