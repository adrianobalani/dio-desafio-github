import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QRadioButton,QVBoxLayout,QTabWidget,QFormLayout,QLabel,QLineEdit
 
class Tab(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
 
        self.addTab(self.tab1,'tab1')
        self.addTab(self.tab2,'tab2')
        self.addTab(self.tab3,'tab3')
 
        self.tab1UI()
        self.tab2UI()
 
    def tab1UI(self):
        tab1_lay=QGridLayout()
        self.tab1.setLayout(tab1_lay)
 
        self.setTabText (0, 'Information Page')
        Label = QLabel ('Name: Tom')
        tab1_lay.addWidget(Label,0,0)
 
    def tab2UI(self):
        tab2_lay=QGridLayout()
        self.tab2.setLayout(tab2_lay)
 
        self.setTabText (1, 'Page 2')
        Label = QLabel ('Name: Tom')
        tab2_lay.addWidget(Label,0,0)
         
 
 
class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('demo')
        self.setGeometry(300,300,300,200)
 
                 #Form layout
        layout=QFormLayout()
        self.setLayout(layout)
 
        layout.addRow (QRadioButton ('Men'))
        layout.addRow (QRadioButton ('Female'))
 
        tabwidget=Tab()
        layout.addRow(tabwidget)
     
 
 
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TabWidget()
    demo.show()
    sys.exit(app.exec_())