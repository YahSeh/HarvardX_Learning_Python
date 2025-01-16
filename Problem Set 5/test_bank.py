from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()
    test_place()

def test_zero() :
    assert value('Hello') == 0
    assert value('Hello there') == 0
    assert value('HeLlO tHeRe') == 0

def test_twenty() :
    assert value('Hey') == 20
    assert value('hi') == 20
    assert value('Howdy there') == 20
    assert value('HeY tHeRe') == 20

def test_hundred() :
    assert value("Salutations") == 100
    assert value("plop") == 100
    assert value("What's up") == 100

'''def test_place() :
    assert value('Well hello') == 0
    assert value('Hello there') == 0
    assert value('Hey there') == 20
    assert value('Well hey') == 100
'''

if __name__ == "__main__":
    main()
