#!/usr/bin/env python

#It uses PyQt4 to display hello world
import sys
from PyQt4 import QtCore, QtGui

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        
        #widgets
        self.label = QtGui.QLabel("Hello World!")
        self.button = QtGui.QPushButton("OK")
        
        #signals
        self.button.clicked.connect(self.accept)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setMinimumSize(200,150)
        self.setWindowTitle("Hello World")
        
        #pergunta pelo nome:
        text, ok = QtGui.QInputDialog.getText(self, "What is your name?",
                      "Name: ", QtGui.QLineEdit.Normal)
        if ok and text != '':
            self.label.setText("Hello, " + text + "!")
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
