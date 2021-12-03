import sys
from PyQt5.QtWidgets import QWidget,QTextEdit,QMainWindow,QSystemTrayIcon,QDockWidget,QStackedWidget,QListWidget,QApplication,QGridLayout,QRadioButton,QVBoxLayout,QTabWidget,QFormLayout,QLabel,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
class DockWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('demo')
        self.setGeometry(300,300,300,200)
                 # Set the system tray icon, get the tray, set the tray icon
        tuopan=QSystemTrayIcon(self)
        tuopan.setIcon(QIcon('new.png'))
        tuopan.setToolTip('1111')
        tuopan.show()
 
        dockwidget=QDockWidget('dockdemo',self)
        
 
        list=QListWidget()
        list.insertItem (0, 'first')
        list.insertItem (1, 'second')
        list.insertItem (2, 'third')
        list.insertItem (3, 'fourth')
 
        dockwidget.setWidget(list)
 
                 # Set QDockWidget can be float
        # dockwidget.setFloating(True)
                 # Set the central control for qtextedit
        text=QTextEdit()
        self.setCentralWidget(text)
 
                 # Setupwidget placed on the right
        self.addDockWidget(Qt.RightDockWidgetArea,dockwidget)
         
 
 
 
if __name__=='__main__':
    app=QApplication(sys.argv)
     
    demo=DockWidget()
    demo.show()
    sys.exit(app.exec_())