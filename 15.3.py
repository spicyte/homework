CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_channel_index = N - 1
        return self.current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def exists(self, N_or_name):
        if isinstance(N_or_name, int):
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        elif isinstance(N_or_name, str):
            return "Yes" if N_or_name in self.channels else "No"
        else:
            return "No"

controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.exists(4) == "No")
print(controller.exists("BBC") == "Yes")
