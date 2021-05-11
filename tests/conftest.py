import pytest

from cypher import Cypher


@pytest.fixture
def cypher():
    return Cypher("b")
