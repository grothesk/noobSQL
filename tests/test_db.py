import os

from noobSQL.utils.db import Connection, Naming


HERE = os.path.dirname(__file__)
YML = 'test.yml'


def test_connection():
    connection = Connection.from_yaml(os.path.join(HERE, YML))
    assert connection.dialect == 'postgresql'
    assert connection.user == 'pgdocker'
    assert connection.password == 'docker'
    assert connection.host == 'localhost'
    assert connection.port == 5432
    assert connection.database == 'demo'


def test_naming():
    naming = Naming.from_yaml(os.path.join(HERE, YML))
    assert True


def test_will_not_fail():
    assert True