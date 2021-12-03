import sys
from PyQt5.QtWidgets import QWidget,QStackedWidget,QListWidget,QApplication,QGridLayout,QRadioButton,QVBoxLayout,QTabWidget,QFormLayout,QLabel,QLineEdit
 
class Stacked(QStackedWidget):
    def __init__(self):
        super().__init__()
 
        self.area1=QWidget()
        self.area2=QWidget()
        self.area3=QWidget()
        self.addWidget(self.area1)
        self.addWidget(self.area2)
        self.addWidget(self.area3)
 
        self.area1UI()
        self.area2UI()
 
    def area1UI(self):
        layout=QFormLayout()
        self.area1.setLayout(layout)
        layout.addRow('name',QLineEdit())
    def area2UI(self):
        layout=QFormLayout()
        self.area2.setLayout(layout)
        layout.addRow('password',QLineEdit())
 
class StackedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('demo')
        self.setGeometry(300,300,300,200)
 
                   #Form layout
        layout=QFormLayout()
        self.setLayout(layout)
 
        self.widget=Stacked()
        layout.addRow(self.widget)
 
        list=QListWidget()
        list.insertItem(0,'first1')
        list.insertItem(1,'second')
        list.insertItem(2,'three')
        layout.addRow(list)
        list.currentRowChanged.connect(self.showArea)
 
        
 
    def showArea(self,i):
        self.widget.setCurrentIndex(i)
 
 
 
 
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=StackedWidget()
    demo.show()
    sys.exit(app.exec_())