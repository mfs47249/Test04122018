'''
Created on 17.05.2018

@author: mf
'''

from java.awt import Color
from javax.swing import JFrame, JPanel, BorderFactory, WindowConstants
from javax.swing import JButton
from javax.swing import JLabel
from java.awt.event import ActionListener
from javax.swing import BorderFactory



class window (JPanel):
    outtext = ""

    def actionPerformed(self, e):
        self.cmdstring = e.getActionCommand()
        print self.cmdstring
        if ("add" == self.cmdstring):
            self.outtext += "add "
            self.text.setText(self.outtext)
        if ("delete" == self.cmdstring):
            self.outtext += "delete "
            self.text.setText(self.outtext)
        if ("quit" == self.cmdstring):
            print ("Quit button pressed.")
            self.frame.dispose()

    def __init__(self, title):
        self.frame = JFrame (title, defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE)
        self.frame.setSize(1024, 768)
        self.frame.setLocationRelativeTo(None)
        self.frame.setLayout(None)
        self.pane = self.frame.getContentPane()
        self.pane.setBackground(Color(255,255,225))

        self.btn = JButton("Add", actionPerformed = self.actionPerformed, bounds = (20,20,100,20))
        self.btn.setActionCommand("add")
        self.pane.add(self.btn)

        self.btn2 = JButton("Delete", actionPerformed = self.actionPerformed)
        self.btn2.setActionCommand("delete")
        self.btn2.setBounds(20, 50,100,20)
        self.pane.add(self.btn2)

        self.quitbtn = JButton("Quit", actionPerformed = self.actionPerformed)
        self.quitbtn.setActionCommand("quit")
        self.quitbtn.setBounds(20, 80, 100, 20)
        self.pane.add(self.quitbtn)


        self.b = BorderFactory.createLineBorder(Color(0,0,0), 1)
        self.text = JLabel("")
        self.text.setBounds(20,110,200,20)
        self.text.setBorder(self.b)
        self.pane.add(self.text)

        self.frame.visible = True


print ("test")
w = window("Hello World")
print ("done")

if __name__ == '__main__':
    pass
