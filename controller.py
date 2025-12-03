from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.app import simple_switch_stp_13 # Spanning Tree Protocol, bo nam się pętla tam poburzy

class ProjectController(simple_switch_stp_13.SimpleSwitch13):
    def __init__(self, *args, **kwargs):
        super(ProjectController, self).__init__(*args, **kwargs)