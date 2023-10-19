from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

# Define the Star Topology server
class StarServer(Protocol):
    def __init__(self, factory):
        self.factory = factory

    # Called when a new connection is made
    def connectionMade(self):
        self.factory.clients.append(self)
        print("New client connected")

    # Called when a connection is lost
    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        print("Client disconnected")

    # Called when data is received
    def dataReceived(self, data):
        print("Received data: ", data.decode('utf-8'))
        for client in self.factory.clients:
            if client != self:
                client.transport.write(data)

# Define the Star Topology factory
class StarFactory(Factory):
    def __init__(self):
        self.clients = []

    def buildProtocol(self, addr):
        return StarServer(self)

# Start the Star Topology server
reactor.listenTCP(8000, StarFactory())
print("Star Topology server started")
reactor.run()
