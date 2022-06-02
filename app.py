from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
from GtfReader import GtfReader
from SamReader import SamReader
import asyncio
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec())

main()