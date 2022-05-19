from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import urllib.request

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)


class Tray():
    def __init__(self):
        self.maketray()

    def maketray(self):
        icon = QIcon('spartanheadnobg.png')
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        menu = QMenu()

        lunch = QAction("Lunch")
        lunch.triggered.connect(lambda: self.lunchwidget())
        menu.addAction(lunch)

        schedule = QAction("Schedule")
        schedule.triggered.connect(lambda: self.schedulewidget())
        menu.addAction(schedule)

        quit = QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)

        tray.setContextMenu(menu)
        sys.exit(app.exec_())

    def lunchwidget(self):
        self.lw = LunchWidget()
        self.lw.show()

    def schedulewidget(self):
        self.sw = ScheduleWidget()
        self.sw.show()
    

class LunchWidget(QWidget):
    def __init__(self):
        super(LunchWidget, self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        url = 'https://resources.finalsite.net/images/f_auto,q_auto,t_image_size_2/v1644185966/webbschoolorg/tvbdwvpm7d58cwyfdnnj/UpperSchoolMenu.jpg'
        data = urllib.request.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)

        lbl = QLabel(self)
        lbl.setPixmap(QtGui.QPixmap(image))

        hbox.addWidget(lbl)
        self.setLayout(hbox)


class ScheduleWidget(QWidget):
    def __init__(self):
        super(ScheduleWidget, self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        url = 'https://lh3.googleusercontent.com/lw5RfA3-onghcJUrwTpApiTmV2U0GZ9cH4x97laKCLrG8adSuqp2vszyED758m_rZtUYQSRtlZK4aYGLuKrwnVppi9A90mxHGaxfa-dcGW8zGg2YrXZzCL-INVETmC5tgHtAeYAe3w=w2400'
        data = urllib.request.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)
        pixmap = QPixmap(image)
        pix2 = pixmap.scaledToWidth(514)

        lbl = QLabel(self)
        lbl.setPixmap(pix2)

        hbox.addWidget(lbl)
        self.setLayout(hbox)


if __name__ == '__main__':
    tray = Tray()
    sys.exit(app.exec_())
