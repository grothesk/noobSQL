from random import randrange, choice
import datetime as dt
import pandas as pd
import numpy as np
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

def event_list(n_events):
    """
    This function will return a list of n events, in which the order of the events matters:
    The required events A, B and C have to be executed in this order, before the other events can take place
    """
    required_events = ['required_event_A', 'required_event_B', 'required_event_C']
    additional_events = ['event_1', 'event_2', 'event_3']
    if len(required_events) > n_events:
        return required_events[:n_events]
    else:
        event_name = required_events
        count = len(required_events)
        while count < n_events:
            event_name += [choice(additional_events)]
            count += 1
        return(event_name)


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
        event_name += event_list(n_events)
        event_time_rnd = [random_timestamp(start_ts, end_ts) for ind in range(n_events)]
        event_time_rnd.sort()
        event_time += event_time_rnd

    df = pd.DataFrame({'id': id, 'user_id': user_id, 'event_name': event_name,
                       'event_time': event_time})

    df = df.sort_index(by=['event_time'])
    df.to_csv('demo_data.csv', index=False)




