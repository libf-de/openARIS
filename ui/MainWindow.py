# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
