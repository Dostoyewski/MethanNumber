import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QTextEdit
from PyQt5.QtWidgets import QDoubleSpinBox


class App(QMainWindow):
    rs_signal = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self):
        super().__init__()
        self.title = 'MethanNumber Calc v0.1.1'
        # Labels for lineEdits
        self.btnCalc = QPushButton('Calculate', self)
        self.c1_t = QLabel('C1:', self)
        self.c2_t = QLabel('C2:', self)
        self.c3_t = QLabel('C3:', self)
        self.ic4_t = QLabel('iC4:', self)
        self.nc4_t = QLabel('nC4:', self)
        self.neo_c5_t = QLabel('neoC5:', self)
        self.ic5_t = QLabel('iC5:', self)
        self.nc5_t = QLabel('nC5:', self)
        self.c6_t = QLabel('C6+:', self)
        self.co2_t = QLabel('CO2:', self)
        self.n2_t = QLabel('N2:', self)
        self.n_t = QLabel('N mixes:', self)

        # SpinBoxes
        self.c1 = QDoubleSpinBox(self)
        self.c1.setRange(0, 100)
        self.c1.setValue(0)
        self.c1.setSingleStep(0.1)

        self.c2 = QDoubleSpinBox(self)
        self.c2.setRange(0, 100)
        self.c2.setValue(0)
        self.c2.setSingleStep(0.1)

        self.c3 = QDoubleSpinBox(self)
        self.c3.setRange(0, 100)
        self.c3.setValue(0)
        self.c3.setSingleStep(0.1)

        self.ic4 = QDoubleSpinBox(self)
        self.ic4.setRange(0, 100)
        self.ic4.setValue(0)
        self.ic4.setSingleStep(0.1)

        self.nc4 = QDoubleSpinBox(self)
        self.nc4.setRange(0, 100)
        self.nc4.setValue(0)
        self.nc4.setSingleStep(0.1)

        self.neo_c5 = QDoubleSpinBox(self)
        self.neo_c5.setRange(0, 100)
        self.neo_c5.setValue(0)
        self.neo_c5.setSingleStep(0.1)

        self.ic5 = QDoubleSpinBox(self)
        self.ic5.setRange(0, 100)
        self.ic5.setValue(0)
        self.ic5.setSingleStep(0.1)

        self.nc5 = QDoubleSpinBox(self)
        self.nc5.setRange(0, 100)
        self.nc5.setValue(0)
        self.nc5.setSingleStep(0.1)

        self.c6 = QDoubleSpinBox(self)
        self.c6.setRange(0, 100)
        self.c6.setValue(0)
        self.c6.setSingleStep(0.1)

        self.co2 = QDoubleSpinBox(self)
        self.co2.setRange(0, 100)
        self.co2.setValue(0)
        self.co2.setSingleStep(0.1)

        self.n2 = QDoubleSpinBox(self)
        self.n2.setRange(0, 100)
        self.n2.setValue(0)
        self.n2.setSingleStep(0.1)

        self.n = QComboBox(self)
        self.n.addItems(['3 mixes', '4 mixes'])

        self.mn_t = QLabel("MN:", self)
        self.mn = QLabel("---", self)
        self.info = QTextEdit(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(520, 480)

        self.c1_t.move(10, 10)
        self.c1.move(100, 10)

        self.c2_t.move(10, 60)
        self.c2.move(100, 60)

        self.c3_t.move(10, 110)
        self.c3.move(100, 110)

        self.ic4_t.move(10, 160)
        self.ic4.move(100, 160)

        self.nc4_t.move(10, 210)
        self.nc4.move(100, 210)

        self.neo_c5_t.move(10, 260)
        self.neo_c5.move(100, 260)

        self.ic5_t.move(300, 10)
        self.ic5.move(400, 10)

        self.nc5_t.move(300, 60)
        self.nc5.move(400, 60)

        self.c6_t.move(300, 110)
        self.c6.move(400, 110)

        self.co2_t.move(300, 160)
        self.co2.move(400, 160)

        self.n2_t.move(300, 210)
        self.n2.move(400, 210)

        self.n_t.move(300, 260)
        self.n.move(400, 260)

        self.btnCalc.resize(100, 35)
        self.btnCalc.move(400, 310)

        self.mn_t.move(10, 310)
        self.mn.move(100, 310)

        self.info.resize(490, 90)
        self.info.move(10, 370)
        self.info.setPlainText("Nothing to show")
        self.info.setReadOnly(True)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
