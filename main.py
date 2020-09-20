from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 

from PIL import ImageGrab, ImageQt, Image
import threading
from time import sleep

class Window(QMainWindow): 
  
  
    def __init__(self): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("Semi Transparent Overlay")

        # set the icon
        self.setWindowIcon(QIcon('icon.png'))

        # set start opacity
        self.setOpacity(0.5)
  
  
        # setting  the geometry of window 
        self.setGeometry(60, 60, 100, 100) 
  
        # creating a label widget 
        self.label_1 = QLabel("what", self) 
        # moving position 
        self.label_1.move(0, 0)

        buttonOpacity1 = QPushButton("Opacity: 1", self)
        buttonOpacity1.move(0, 0)
        buttonOpacity1.clicked.connect(lambda: self.setOpacity(1))
        
        buttonOpacityPoint3 = QPushButton("Opacity: 0.3", self)
        buttonOpacityPoint3.move(0, 30)
        buttonOpacityPoint3.clicked.connect(lambda: self.setOpacity(0.3))
        
        
        buttonOpacityPoint5 = QPushButton("Opacity: 0.5", self)
        buttonOpacityPoint5.move(0, 60)
        buttonOpacityPoint5.clicked.connect(lambda: self.setOpacity(0.5))
        
        buttonOpacityPoint7 = QPushButton("Opacity: 0.7", self)
        buttonOpacityPoint7.move(0, 90)
        buttonOpacityPoint7.clicked.connect(lambda: self.setOpacity(0.7))
        
        buttonOpacity0 = QPushButton("Opacity: 0", self)
        buttonOpacity0.move(0, 120)
        buttonOpacity0.clicked.connect(lambda: self.setOpacity(0))
 
        im = Image.new('RGB', (100, 100))
        qimage = ImageQt.ImageQt(im)
        pixmap1 = QPixmap.fromImage(qimage)
        self.label_1.setPixmap(pixmap1.copy())
        
        #self.grabImage()
        
        # show all the widgets 
        self.show()
        self.resize(100, 100)

    def setOpacity(self, opacity):
        self.opacity = opacity
        self.setWindowOpacity(opacity)

    def checkOpacity(self):
        if self.opacity == 0:
            self.setOpacity(0.7)

    def grabImage(self):
        im = ImageGrab.grabclipboard()
        if im == None:
            return
        width, height = im.size

        self.resize(width, height)
        self.label_1.resize(width,height)
        qimage = ImageQt.ImageQt(im)
        pixmap1 = QPixmap.fromImage(qimage)
        self.label_1.setPixmap(pixmap1.copy())



  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 

def do():
    while True:
        window.grabImage()
        window.checkOpacity()
        sleep(5)

window.grabImage()
threading.Thread(target=do).start()
    
# start the app 
sys.exit(App.exec())


