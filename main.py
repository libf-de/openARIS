from PyQt6 import QtWidgets
from ui.MainWindow import MainWindow
import os

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    
    if os.name == 'nt':
        import pywinstyles
        pywinstyles.apply_style(ui, 'win7')
    
    ui.show()
    
    sys.exit(app.exec())
