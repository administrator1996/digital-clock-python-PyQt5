from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
import sys




class dgtClock(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Digital Clock")
        self.setGeometry(200, 200, 400, 400)
        font = QFont('Open Sans', 50, QFont.Bold)

        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        clock = QTimer(self)
        clock.timeout.connect(self.showTime)
        clock.start(1000)

        self.showTime()

    def showTime(self):
        currTime = QTime.currentTime()

        displayText = currTime.toString('hh:mm:ss')
        print(displayText)

        self.label.setText(displayText)

app = QApplication(sys.argv)
window = dgtClock()
window.show()
app.exit(app.exec_())