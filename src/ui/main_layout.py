from PyQt6.QtWidgets import QWidget


class MainLayout(QWidget):
    model = None

    def __init__(self, model):
        super().__init__()

        self.model = model
        self.initUI()

    def initUI(self):
        self.resize(1000, 650)

        self.setWindowTitle('AI Program')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())
