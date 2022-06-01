from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
from GtfReader import GtfReader
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.add_gtf_reader(GtfReader())
    ui.setup_ui()
    ui.show()
    app.exec()
if __name__ == "__main__":
    main()
