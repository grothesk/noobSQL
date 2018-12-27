from random import randrange
import datetime as dt
import pandas as pd
import uuid

DB = 'user_activity'


def random_timestamp(start_ts, end_ts):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    t_delta = end_ts - start_ts
    t_delta_int = (t_delta.days * 24 * 60 * 60) + t_delta.seconds
    random_second = randrange(t_delta_int)
    return start_ts + dt.timedelta(seconds=random_second)


if __name__ == '__main__':
    start_ts = dt.datetime(2018, 1, 1)
    end_ts = dt.datetime(2018, 1, 31)

    n_user = 30

    id = []
    user_id = []
    event_name = []
    event_time = []

    for ind in range(n_user):
        n_events = randrange(100)
        user = uuid.uuid4().hex
        start_ts = dt.datetime(2018, 1, ind+1)

        id += [uuid.uuid4().hex for ind in range(n_events)]
        user_id += [user for ind in range(n_events)]
        event_name += ['DoSomething' for ind in range(n_events)]
        event_time += [random_timestamp(start_ts, end_ts) for ind in range(n_events)]

    df = pd.DataFrame({'id': id, 'user_id': user_id, 'event_name': event_name,
                       'event_time': event_time})

    df = df.sort_index(by=['event_time'])
    df.to_csv('demo_data.csv', index=False)




