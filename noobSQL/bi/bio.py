import pandas as pd

from noobSQL.bi.queries import q_daily_active_user


class BIResponder:

    def __init__(self, connection, naming):
        self.connection = connection
        self.naming = naming

    def df_from_query(self, query):
        return pd.read_sql(query, con=self.connection.get_engine())

    def daily_active_user(self):
        query = q_daily_active_user(self.naming.table, self.naming.columns)
        return self.df_from_query(query), query
