from mininet.topo import Topo


class Topologia2(Topo):

    def __init__(self):
        Topo.__init__(self)
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')
        host7 = self.addHost('h7')
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(switch1, switch3)
        self.addLink(switch1, switch2)
        self.addLink(switch1, switch4)
        self.addLink(switch2, host5)
        self.addLink(switch2, host6)
        self.addLink(switch2, host7)
        self.addLink(switch2, switch3)
        self.addLink(switch2, switch5)
        self.addLink(switch4, switch5)
        self.addLink(switch4, host3)
        self.addLink(switch5, host4)


topos = {'topologia2': (lambda: Topologia2())}