from twisted.internet import reactor   # responsible for running the event loop
from twisted.internet.protocol import DatagramProtocol  # UDP Protocols

class StopAndWaitProtocol(DatagramProtocol):

    def startProtocol(self):
        self.transport.connect('localhost', 8000) # set destination

    def datagramReceived(self, datagram: bytes, addr):
        print(f"Received {datagram.decode()}")

    def sendData(self, data):
        self.transport.write(data.encode())

# Create instance of stop and wait protocol
protocol = StopAndWaitProtocol()

reactor.callLater(2, protocol.sendData, 'Hello world')
reactor.callLater(4, protocol.sendData, 'How are you?')
reactor.callLater(6, protocol.sendData, 'Bye!')