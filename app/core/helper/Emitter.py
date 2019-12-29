class Emitter:
    """ Helper class for emitting values """

    def __init__(self, default_subscriber=None):
        self.subscribers = []

        if default_subscriber is not None:
            self.subscribe(default_subscriber)

    def subscribe(self, subscriber):
        """ Registers new subscriber """

        self.subscribers.append(subscriber)

    def emit(self, value):
        """ Emits new value to all subscribers """

        for subscriber in self.subscribers:
            subscriber(value)
