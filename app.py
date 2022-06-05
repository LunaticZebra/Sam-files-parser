from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
