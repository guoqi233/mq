from __future__ import absolute_import, unicode_literals

from kombu.pools import producers
from task_queue_example.queues import task_exchange

priority_to_routing_key = {
    'high': 'hipri',
    'mid': 'midpri',
    'low': 'lopri',
}


def send_as_task(connection, fun, args, kwargs, priority='mid'):
    payload = {'fun': fun, 'args': args, 'kwargs': kwargs}
    routing_key = priority_to_routing_key[priority]

    with producers[connection].acquire(block=True) as producer:
        producer.publish(payload,
                         serializer='pickle',
                         compression='bzip2',
                         exchange=task_exchange,
                         declare=[task_exchange],
                         routing_key=routing_key)


if __name__ == '__main__':
    from kombu import Connection
    from task_queue_example.tasks import hello_task
    import pickle
    print("#######")
    print(pickle.dumps(hello_task))
    print("#######")
    print(hello_task)
    with Connection('amqp://admin:guoqi123456@localhost:5672//') as con:
        send_as_task(con, fun=hello_task, args=('Kombu',), kwargs=dict(), priority='high')
