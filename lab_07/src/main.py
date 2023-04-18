import sys
from PyQt5.QtWidgets import QApplication

from window import Window


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
