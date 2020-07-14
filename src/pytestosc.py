from pythonosc import dispatcher, osc_server


class OSCTester():
    
    def __init__(self):
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ThreadingOSCUDPServer(ip, port), dispatcher)

    def map(self, address, handler):
        # Map dispatcher
        self.dispatcher.map(address, handler)
    
    def boot(self):
        self.server.serve_forever()
    
    def default_handlers(self):
        self.dispatcher.map("/msg", print)

