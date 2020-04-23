import sys
from PyQt5 import QtWidgets

from sample.model.MHasher import MHasher
from sample.view.VMainWinBefore import VMainWinBefore

if __name__ == '__main__':
    hasher = MHasher()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    w = VMainWinBefore(main_window,hasher)
    sys.exit(app.exec_())