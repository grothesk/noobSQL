import os
from noobSQL.utils.db import db_config_url


HERE = os.path.dirname(__file__)


def test_db_config_url():
    db_params = dict(dialect='postgresql',
                     user='malte',
                     password='1234',
                     host='localhost',
                     port='5432',
                     database='database')

    url_from_params = db_config_url(db_params)
    url_from_config_file = db_config_url(os.path.join(HERE, 'test_db.ini'),
                                         'test_config')

    assert url_from_params == url_from_config_file
    assert url_from_params == \
           'postgresql://malte:1234@localhost:5432/database'