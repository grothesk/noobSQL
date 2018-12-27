import os
from configparser import ConfigParser


def db_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             filename))

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {} not found in the {} file'.format(
            section, filename))  # todo: add specific exception class

    return db


def db_config_url(*args):
    if len(args) == 1:
        db_params = args[0]

    elif len(args) == 2:
        config_file = args[0]
        section = args[1]
        db_params = db_config(filename=config_file, section=section)

    else:
        raise TypeError('Too many input arguments!')

    if 'password' in db_params:
        db_url = '{}://{}:{}@{}:{}/{}'.format(db_params['dialect'],
                                              db_params['user'],
                                              db_params['password'],
                                              db_params['host'],
                                              db_params['port'],
                                              db_params['database'])
    else:
        db_url = '{}:///{}'.format(db_params['dialect'], db_params['database'])

    return db_url
