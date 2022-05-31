from PyQt6.QtWidgets import QApplication
from my_gui import UiMainWindow
from GtfReader import GtfReader
import sys

class Obiekt:
    def __init__(self):
        self.filepath = ""
    def main(self):
        app = QApplication(sys.argv)
        ui = UiMainWindow()
        ui.setup_ui()
        ui.show()
        ui.update_list(5)
        gtf_r = GtfReader()
        gtf_r.set_filepath()
        ui.set_gtf_path_reader()
        app.exec()
if __name__ == "__main__":
    ob = Obiekt()
    ob.main()
    print(ob.filepath)
