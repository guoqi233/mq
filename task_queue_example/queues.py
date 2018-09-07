from __future__ import absolute_import, unicode_literals

from kombu import Exchange, Queue

task_exchange = Exchange(b"task", type=b"direct")
task_queues = [
    Queue(name=b"hipri", exchange=task_exchange, routing_key=b"hipri"),
    Queue(name=b"midpri", exchange=task_exchange, routing_key=b"midpri"),
    Queue(name=b"lopri", exchange=task_exchange, routing_key=b"lopri"),
]
