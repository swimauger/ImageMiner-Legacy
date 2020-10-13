import json

class API:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False
        self.listeners = {}
    
    def send(self, channel, message):
        returnVals = []
        for listener in self.listeners[channel]:
            returnVals.append(listener(json.loads(message)))
        return json.dumps(returnVals)

    def on(self, channel, callback):
        if channel not in self.listeners:
            self.listeners[channel] = []
        
        self.listeners[channel].append(callback)
