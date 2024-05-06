from PyQt6.QtWidgets import QApplication, QWidget
import sys

# create the QApplication
app = QApplication(sys.argv)

# create the main window
window = QWidget(windowTitle='Hello World')
window.show()

# start the event loop
app.exec()

