# -*- coding: UTF-8 -*-from tool.client import *if __name__ == '__main__':    HOST = '127.0.0.1'    PORT = 9090    ADDR = (HOST, PORT)    Handler =""    Clnt = Client(ADDR, Handler)    buf = Clnt.receive()    print "Client Receive %s" % buf    pass