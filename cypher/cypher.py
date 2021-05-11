import string


class Cypher:
    """An object-oriented implementation of a Caesar Cypher.
    This class will receive a start letter in the initialization
    and shift the whole alphabet (capital letters included).

    Parameters
    ----------
    start_letter: str
        letter where the shift begins, can be capital.

    Example
    -------
    This is how you can use the Cypher:

        >>> c = Cypher("b")
        >>> encrypted = c.encrypt("This is my name")
        >>> print(encrypted)
        Uijt jt nz obnf
        >>> decrypted = c.decrypt(encrypted)
        >>> print(decrypted)
        This is my name
    """

    def __init__(self, start_letter):
        self.start_letter = start_letter
        self._alphabet = self._generate_alphabet()
        self._foward = self._mapping()
        self._reverse = self._mapping(reverse=True)

    def encrypt(self, phrase):
        """A method for encrypting the given phrase to a Cypher.

        Parameters
        ----------
        phrase: str
            a string to be encryped.

        Returns
        -------
        str
            the phrase encrypted.
        """
        return phrase.translate(self._foward)

    def decrypt(self, phrase):
        """A method for decrypting the given phrase using the Cypher.

        Parameters
        ----------
        phrase: str
            a string to be descrypted.

        Returns
        -------
        str
            the phrase decrypted.
        """
        return phrase.translate(self._reverse)

    def _generate_alphabet(self):
        idx = string.ascii_letters.index(self.start_letter)
        return string.ascii_letters[idx:] + string.ascii_letters[:idx]

    def _mapping(self, reverse=False):
        if reverse:
            return str.maketrans(self._alphabet, string.ascii_letters)
        return str.maketrans(string.ascii_letters, self._alphabet)
