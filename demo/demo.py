from noobSQL.utils.db import Connection, Naming
from noobSQL.bi.bio import BIResponder


if __name__ == '__main__':
    file = 'demo.yml'
    connection = Connection.from_yaml(file)
    naming = Naming.from_yaml(file)

    bir = BIResponder(connection, naming)
    dau, query = bir.daily_active_user()

    print(query)
    print(dau)