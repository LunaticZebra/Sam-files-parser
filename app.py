from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
from GtfReader import GtfReader
from SamReader import SamReader
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.setup_ui()
    ui.show()
    ui.add_gtf_reader(GtfReader())
    ui.add_sam_reader(SamReader())
    app.exec()
if __name__ == "__main__":
    main()