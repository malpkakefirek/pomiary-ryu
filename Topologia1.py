from mininet.topo import Topo


class Topologia1(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        self.addLink(host1, switch1)
        self.addLink(switch1, switch2)
        self.addLink(switch2, host2)


topos = {'Topologia1': (lambda: Topologia1())}
