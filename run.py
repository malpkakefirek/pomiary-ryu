#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

from Topologia2 import Topologia2 

def run_project():
    setLogLevel('info')

    topo = Topologia2()
    
    net = Mininet(topo=topo,
                  controller=RemoteController,
                  switch=OVSKernelSwitch,
                  link=TCLink)

    net.start()

    hosts = ['h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    
    for h_name in hosts:
        h = net.get(h_name)
        h.cmd('iperf -s &')
        h.cmd('iperf -s -u &')

    CLI(net)

    net.stop()

if __name__ == '__main__':
    run_project()