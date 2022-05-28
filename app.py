from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.setup_ui()
    ui.show()
    ui.update_list(5)
    app.exec()
if __name__ == "__main__":
    main()
