class API:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False
        self.listeners = {}
    
    def send(self, channel, message):
        for listener in self.listeners[channel]:
            listener(message)

    def on(self, channel, callback):
        if channel not in self.listeners:
            self.listeners[channel] = []
        
        self.listeners[channel].append(callback)
