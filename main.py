import time


class Messenger:
    db = []
    requested_count = 0

    def send_message(self, name, text):
        timestamp = time.asctime()
        self.db.append({
            'name': name,
            'text': text,
            'timestamp': timestamp,
        })

    def get_message(self):
        return self.db

    def get_new_message(self):
        new_message = self.db[self.requested_count:]
        self.requested_count += len(new_message)
        return self.db



messenger = Messenger()
messenger.send_message('Jack', 'adb')
messenger.send_message('Jack', 'bsd')
messenger.send_message('Tonny', 'hello')
print(messenger.get_message())
print(messenger.get_new_message())

messenger.send_message('Jack', 'bsd2')
messenger.send_message('Tonny', 'hello2')
print(messenger.get_new_message())