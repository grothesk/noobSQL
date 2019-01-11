def q_daily_active_user(table, columns):
    query = 'SELECT {timestamp}::date AS t, ' \
            'COUNT(DISTINCT {user_id}) AS cnt ' \
            'FROM {table} ' \
            'GROUP BY t ' \
            'ORDER BY t'.format(
        timestamp=columns['timestamp'],
        user_id=columns['user_id'],
        table=table)

    return query