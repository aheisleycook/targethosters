from tkinter import Listbox

from net import NetLogger, Interface, socket
import tkinter as tk
networkInterface = Interface()


class NetTester(tk.Tk):

    lstAdress: Listbox

    def __init__(self) -> object:
        self.targetLog = self.targetsystem.TestTarget(self.testhost)
        self.targetsystem = networkInterface()
        self.testhost = self.txtport.split()
        self.lblAddresses = tk.Label(self, text="address")
        self.lblAddress.pack()
        self.txtAdresses = tk.Entry(self)
        self.txtAdresses.pack()
        self.lblport = tk.Label(self, text="port")
        self.lblport.pack()
        self.txtport = tk.Entry(self)
        self.txtport.pack()
        self.btnTest = tk.Button(self, text="test", command=self.TestHost)
        self.btnTest.pack()
        self.lstAdress = tk.Listbox(self)
        self.lstAdress.pack()

    def testHost(self):
        self.targetsystem.port = self.txtport.get()
        for self.targetTest in self.targetLog:
            self.lstAdress.insert(self.targetTest, 0)


root = tk.Tk()
netTester = NetTester().maxsize(100,100)
NetTester().mainloop()
