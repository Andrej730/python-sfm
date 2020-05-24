# Initial Script after SFM started up, and the main window got focus
from PySide import QtCore
from PySide import QtGui
from PySide import shiboken
import time
import sfmApp
import re

def initiate_autosave():
    saveInterval = 300 #seconds
    save_delay = 0.5*1000
    addTimestamp = True # True creates new files for each save, False overwrites the original .dmx

    class AutoSaveWindow(QtGui.QWidget):
        def __init__(self, filename = 'test'):
            super(AutoSaveWindow, self ).__init__()
            self.filename = filename
            self.setAttribute(QtCore.Qt.WidgetAttribute.WA_ShowWithoutActivating)
            self.initUI()
            QtCore.QTimer.singleShot(save_delay, self.close)

        def initUI(self):
            # qApp = QtGui.QApplication.instance()
            # screenGeometry = qApp.desktop().availableGeometry()
            # screenGeo = screenGeometry.bottomRight()

            # windowGeometry = self.frameGeometry()
            # windowGeometry.moveBottomRight(screenGeo)
            # self.move(windowGeometry.topLeft())

            self.resize(240,100)
            self.setWindowTitle("Autosave")

            grid = QtGui.QGridLayout()
            grid.setSpacing(12)
            grid.setColumnMinimumWidth(0,72)

            # Create the text entry
            messageLabel = QtGui.QLabel()
            messageLabel.setText('Autosaved as "%s"' % (self.filename))
            grid.addWidget(messageLabel, 0, 0, 1, 1)

            # Create the apply button
            btnSave = QtGui.QPushButton()
            btnSave.setText("OK")
            btnSave.clicked.connect(self.close)
            grid.addWidget(btnSave, 1, 0, 1, 1)

            # Display the window
            self.setLayout(grid)

    def saveDocument():
        if not sfmApp.HasDocument():
            return

        name = str(sfmApp.GetMovie().name)
        currentTime = time.strftime("%Y %m %d - %H %M %S")
        filename = name + currentTime + '.dmx'

        print "saving", name
        print "time:", currentTime

        filename = re.sub(r'[\/:*?"<>|]', '', filename)

        if addTimestamp:
            sfmApp.SaveDocument('usermod/elements/sessions/autosaves/%s' % (filename))
        else:
            sfmApp.SaveDocument()

        global asw
        asw = AutoSaveWindow(filename)
        asw.show()

    saveTimer = QtCore.QTimer()
    saveTimer.timeout.connect(saveDocument)

    QtCore.QCoreApplication.instance().aboutToQuit.connect(lambda: shiboken.delete(saveTimer))

    print "Starting autosave script. Saving every", saveInterval, "seconds."
    saveTimer.start(saveInterval*1000)

    QtGui.QMessageBox.information(
        None, 'Info - Autosave activated',
        'Autosave script activated. Session will be saved every %s mins %s' % \
        (round(saveInterval/60., 2), 'in separated files.' if addTimestamp else '.')
    )

print "PLATFORM: Python initial startup complete"
print 'Python sfm_init.py'
initiate_autosave()
