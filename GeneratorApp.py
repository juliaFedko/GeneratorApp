import sys
import os

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QApplication, QFileDialog, QGridLayout, QDoubleSpinBox, \
    QSpinBox, QLabel, QVBoxLayout, QTableWidget, QMessageBox
import Waves as waves


class GeneratorApp(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        self.left = 700
        self.top = 100
        self.width = 700
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.title = 'Generator'
        self.setWindowTitle(self.title)



# MENUBAR

        self.save = QAction('Save', self)
        self.save.triggered.connect(self.fileSaving)
        self.exit = QAction('Exit', self)
        self.exit.triggered.connect(self.programExit)
        self.sine = QAction("Sine", self)
        self.sine.triggered.connect(self.sine_clicked)
        self.square = QAction("Square", self)
        self.sawtooth = QAction("Sawtooth", self)
        self.triangle = QAction("Triangle", self)
        self.whitenoise = QAction("White Noise", self)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(self.save)
        fileMenu.addAction(self.exit)
        helpMenu = menuBar.addMenu('Calculate')
        helpMenu.addAction(self.sine)
        helpMenu.addAction(self.square)
        helpMenu.addAction(self.sawtooth)
        helpMenu.addAction(self.triangle)
        helpMenu.addAction(self.whitenoise)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(QVBoxLayout())
        self.setCentralWidget(self.mainWidget)

#BOXES AND THE TIME RANGE

        boxes = QWidget()
        boxes.setLayout(QGridLayout())

        self.time = QDoubleSpinBox(self)
        self.time.setRange(1, 60)
        self.time.setValue(5)
        self.time.setSingleStep(1)

        self.steps = QSpinBox(self)
        self.steps.setRange(40000, 50000)
        self.steps.setValue(44100)
        self.steps.setSingleStep(100)

        self.A = QDoubleSpinBox(self)
        self.A.setRange(0, 50)
        self.A.setValue(1)
        self.A.setSingleStep(0.1)

        self.f = QSpinBox(self)
        self.f.setRange(0, 2000)
        self.f.setValue(440)
        self.f.setSingleStep(10)

        self.label1 = QLabel("Time [s]:")
        self.label2 = QLabel("Steps:")
        self.label3 = QLabel("Amplitude:")
        self.label4 = QLabel("Frequency:")

        self.x = np.linspace(0, self.time.value(), self.steps.value())

        boxes.layout().addWidget(self.label1, 0, 0)
        boxes.layout().addWidget(self.label2, 0, 1)
        boxes.layout().addWidget(self.label3, 0, 2)
        boxes.layout().addWidget(self.label4, 0, 3)
        boxes.layout().addWidget(self.time, 1, 0)
        boxes.layout().addWidget(self.steps, 1, 1)
        boxes.layout().addWidget(self.A, 1, 2)
        boxes.layout().addWidget(self.f, 1, 3)

        self.mainWidget.layout().addWidget(boxes)

#TABLE

        table = QWidget()
        table.setLayout(QVBoxLayout())

        self.values = QTableWidget(self)

        table.layout().addWidget(self.values)

        self.values.setColumnCount(2)
        row = self.steps.value()
        self.values.setRowCount(row)
        self.values.setHorizontalHeaderLabels(["Time progress", "Acceleration [m/s^2]"])
        self.values.setColumnWidth(0, 300)
        self.values.setColumnWidth(1, 300)

        self.mainWidget.layout().addWidget(table)

        self.show()

    def sine_clicked(self):
        print("")

    def fileSaving(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileName()", "", options=options)
        file = open(fileName, 'w')
        text = "Zawartość pliku"
        file.write(text)
        file.close()

    def programExit(self):
        print('Kończy działanie aplikacji')
        os._exit(0)

    def showDialogBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Coś poszło nie tak.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


app = QApplication(sys.argv)
ex = GeneratorApp()
app.exec_()