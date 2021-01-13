import  socket
import logging


class NetLogger(logging.Logger):
    def __init__(self):
        pass
    def logInvalid(self,msg):
        self.root.info(msg)
    
        
        


class Interface(socket.socket):
    def __init__(self):
        self.port = 80
        self.net = (socket.AF_INET6, socket.AF_INET6)
    def TestTarget(self,*targets):
        for target in targets:
            try:
                self.connect_ex((target,self.port))
            except Exception as e:
                netlogger = NetLogger()
                netlogger.logInvalid(str(e))
                
