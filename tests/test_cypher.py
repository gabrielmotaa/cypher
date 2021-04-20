def test_encrypt(cypher):
    original, expected = "this is my name", "uijt jt nz obnf"
    assert cypher.encrypt(original) == expected


def test_decrypt(cypher):
    original, expected = "uijt jt nz obnf", "this is my name"
    assert cypher.decrypt(original) == expected
