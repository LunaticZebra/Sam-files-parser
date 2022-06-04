from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
from GtfReader import GtfReader
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
<<<<<<< HEAD
    ui.add_gtf_reader(GtfReader())
    ui.setup_ui()
    ui.show()
    app.exec()
if __name__ == "__main__":
    main()
=======
    ui.show()
    sys.exit(app.exec())


main()
>>>>>>> 90ee2b36135b94a35a8283af7966ffd8c721a2b4
