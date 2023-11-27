import socket
import logging
class Peer:
    def __init__(pr,ip,port):
        pr.ip = ip
        pr.port = port
        pr.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        pr.live =False
    def connect(pr):
        try:
            pr.live = True
        except Exception as e:
            print(f"NO CONNECTION {pr.ip}")
            return False
        return  True
    def sent_message(pr,msg):
        try:
            pr.socket.sendto(msg,(pr.ip,pr.port))
        except Exception as e:
            pr.healthy = False
            logging.error("Failed to send to peer : %s" % e.__str__())