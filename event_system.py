# start these scripts via a pipe as a "python3 event_source.py | python3 event_system.py"

# the whole system is loosely based on the observer pattern (OOP) System -> event emitters -> event listeners(handlers)
# the System class reads from standard input, parses messages, and notifies registered event emitters
# event emitters in turn receive the parsed message, form an event object from it and notify
# registered event listeners by calling their specified functions with the event object as an argument
# this code merely exists as a mental model for reasoning about other event handling solutions


class System:

    messages_buffer = []
    all_emitters = []

    def notify_emitters(self, message):
        for emitter in self.all_emitters:
            if emitter.x == message[1] and emitter.y == message[2]:
                print(emitter.name, ' <--- received message --->', message)
                emitter.receive(message)
                break
        else:
            print('message received, but no event emitter exists at specified GUI location')

    def add_emitter(self, emitter):
        self.all_emitters.append(emitter)

    def handle_message(self, message):
        self.messages_buffer.append(message)

    def parse_message(self, message):
        return message.split(':')

    def listen_to_events(self):
        while 1:
            event = input()
            parsed = self.parse_message(event)
            self.notify_emitters(parsed)


class EventEmitter:

    # determine which event emitter should receive the system message by inspecting their x,y coordinates
    def __init__(self, system_object, name, type_, x, y):
        self.type = type_
        self.name = name
        self.x = x
        self.y = y
        self.event_listeners = {'click': [], 'hover': [], 'close': [], 'open': []}
        system_object.add_emitter(self)

    def add_event_listener(self, event_type, function_):
        self.event_listeners[event_type].append(function_)

    def receive(self, message):
        self.emit_event(message)

    def emit_event(self, message):

        event_data = [self.name, message[0], message[1], message[2]]

        for event_handler in self.event_listeners[message[0]]:
            event_handler(event_data)


"""
-----
test/API below
-----
"""
system = System()

div1 = EventEmitter(system, name='div1', type_='not_specified', x='10', y='20')
div2 = EventEmitter(system, name='div2', type_='not_specified', x='5', y='2')
div3 = EventEmitter(system, name='div3', type_='not_specified', x='7', y='3')

div1.add_event_listener('click', lambda event_data: print('event_listener_fired', event_data))
div2.add_event_listener('open', lambda event_data: print('event_listener_fired', event_data))
div2.add_event_listener('hover', lambda event_data: print('event_listener_fired', event_data))
div3.add_event_listener('close', lambda event_data: print('event_listener_fired', event_data))
div3.add_event_listener('hover', lambda event_data: print('event_listener_fired', event_data))

system.listen_to_events()
