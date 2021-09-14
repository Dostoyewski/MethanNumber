import sys
import threading
import time

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QTextEdit, QLineEdit
from PyQt5.QtWidgets import QDoubleSpinBox

from gas import Gas


class App(QMainWindow):
    rs_signal = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self):
        super().__init__()
        self.title = 'MethanNumber Calc v0.1.2'
        self.gas = None
        # Labels for lineEdits
        self.btnCalc = QPushButton('Вычислить', self)
        self.btnStop = QPushButton('Стоп', self)

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
        self.c1.setRange(40, 99.97)
        self.c1.setValue(40)
        self.c1.setSingleStep(0.1)
        self.c1.setDecimals(4)

        self.c2 = QDoubleSpinBox(self)
        self.c2.setRange(0.001, 15)
        self.c2.setValue(0.001)
        self.c2.setSingleStep(0.1)
        self.c2.setDecimals(4)

        self.c3 = QDoubleSpinBox(self)
        self.c3.setRange(0.001, 6)
        self.c3.setValue(0.001)
        self.c3.setSingleStep(0.1)
        self.c3.setDecimals(4)

        self.ic4 = QDoubleSpinBox(self)
        self.ic4.setRange(0.001, 4)
        self.ic4.setValue(0.001)
        self.ic4.setSingleStep(0.1)
        self.ic4.setDecimals(4)

        self.nc4 = QDoubleSpinBox(self)
        self.nc4.setRange(0.001, 4)
        self.nc4.setValue(0.001)
        self.nc4.setSingleStep(0.1)
        self.nc4.setDecimals(4)

        self.neo_c5 = QDoubleSpinBox(self)
        self.neo_c5.setRange(0.001, 0.05)
        self.neo_c5.setValue(0.001)
        self.neo_c5.setSingleStep(0.1)
        self.neo_c5.setDecimals(4)

        self.ic5 = QDoubleSpinBox(self)
        self.ic5.setRange(0.001, 2)
        self.ic5.setValue(0.001)
        self.ic5.setSingleStep(0.1)
        self.ic5.setDecimals(4)

        self.nc5 = QDoubleSpinBox(self)
        self.nc5.setRange(0.001, 2)
        self.nc5.setValue(0.001)
        self.nc5.setSingleStep(0.1)
        self.nc5.setDecimals(4)

        self.c6 = QDoubleSpinBox(self)
        self.c6.setRange(0.001, 1.5)
        self.c6.setValue(0.001)
        self.c6.setSingleStep(0.1)
        self.c6.setDecimals(4)

        self.co2 = QDoubleSpinBox(self)
        self.co2.setRange(0.005, 10)
        self.co2.setValue(0.005)
        self.co2.setSingleStep(0.1)
        self.co2.setDecimals(4)

        self.n2 = QDoubleSpinBox(self)
        self.n2.setRange(0.005, 15)
        self.n2.setValue(0.005)
        self.n2.setSingleStep(0.1)
        self.n2.setDecimals(4)

        self.n = QComboBox(self)
        self.n.addItems(['3 смеси', '4 смеси'])

        self.mn_t = QLabel("MN:", self)
        self.mn = QLineEdit("---", self)
        self.info = QTextEdit(self)

        self.btnCalc.clicked.connect(self.start_calculation)
        self.btnStop.clicked.connect(self.stop_calculation)

        self.initUI()

    def start_calculation(self):
        now = time.time()
        self.mn.setText("В процессе")
        try:
            self.g = Gas(float(self.c1.value()),
                         float(self.c2.value()),
                         float(self.c3.value()),
                         float(self.ic4.value()),
                         float(self.nc4.value()),
                         float(self.neo_c5.value()),
                         float(self.ic5.value()),
                         float(self.nc5.value()),
                         float(self.c6.value()),
                         float(self.co2.value()),
                         float(self.n2.value()),
                         int(self.n.currentText().split(sep=' ')[0]))
            job_thread = threading.Thread(target=self.process_MN)
            job_thread.start()
            self.info.setPlainText(self.g.construct_docstr())
        except ZeroDivisionError:
            self.info.setPlainText("Проверьте входные данные!")
            self.mn.setText("Ошибка!")
        # with open("out.txt", "w") as output:
        #     output.write(str(g))

    def process_MN(self):
        self.g.calc_MN()
        if self.g.run_calculation:
            self.mn.setText(str(round(self.g.MN, 4)))

    def stop_calculation(self):
        try:
            self.g.run_calculation = False
            self.info.setPlainText("Вычисления остановлены!")
            self.mn.setText("Остановлено")
        except AttributeError:
            self.info.setPlainText("Пожалуйста, укажите газовый состав")
            self.mn.setText("Ошибка!")

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

        self.btnStop.resize(100, 35)
        self.btnStop.move(250, 310)

        self.mn_t.move(10, 310)
        self.mn.move(100, 310)
        self.mn.setReadOnly(True)

        self.info.resize(490, 90)
        self.info.move(10, 370)
        self.info.setPlainText(
            "Введите молярные доли исходной многокомпонентной смеси и укажите количество упрощенных смесей.")
        self.info.setReadOnly(True)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
