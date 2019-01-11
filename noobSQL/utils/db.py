import yaml
from sqlalchemy import create_engine


class yamlSection:

    SECTION_NAME = 'section'

    @classmethod
    def from_yaml(cls, path):
        with open(path, 'r') as f:
            cfg = yaml.load(f)
        return cls(cfg[cls.SECTION_NAME])

    def to_yaml(self, path):
        with open(path, 'a') as f:
            dump = yaml.dump({self.SECTION_NAME: vars(self)},
                             default_flow_style=False)
            f.write(dump)


class Connection(yamlSection):

    SECTION_NAME = 'connection'

    def __init__(self, cfg):
        self.dialect = cfg['dialect']
        self.user = cfg['user']
        self.password = cfg['password']
        self.host = cfg['host']
        self.port = cfg['port']
        self.database = cfg['database']

    def get_db_url(self):
        if self.password != '':
            db_url = '{}://{}:{}@{}:{}/{}'.format(
                self.dialect,
                self.user,
                self.password,
                self.host,
                self.port,
                self.database)
        else:
            db_url = '{}:///{}'.format(
                self.dialect,
                self.database)
        return db_url

    def get_engine(self):
        return create_engine(self.get_db_url())


class Naming(yamlSection):

    SECTION_NAME = 'naming'

    def __init__(self, cfg):
        self.columns = cfg['columns']
        self.table = cfg['table']
