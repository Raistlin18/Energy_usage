from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(150, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.countryLabel = QtWidgets.QLabel(self.centralwidget)
        self.countryLabel.setGeometry(QtCore.QRect(520, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.yearLine = QtWidgets.QLineEdit(self.centralwidget)
        self.yearLine.setGeometry(QtCore.QRect(10, 100, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yearLine.setFont(font)
        self.yearLine.setAlignment(QtCore.Qt.AlignCenter)
        self.yearLine.setObjectName("yearLine")
        self.yearButton = QtWidgets.QPushButton(self.centralwidget)
        self.yearButton.setGeometry(QtCore.QRect(64, 150, 241, 31))
        self.yearButton.setObjectName("yearButton")
        self.countryButton = QtWidgets.QPushButton(self.centralwidget)
        self.countryButton.setGeometry(QtCore.QRect(490, 150, 241, 31))
        self.countryButton.setObjectName("countryButton")
        self.countryLine = QtWidgets.QLineEdit(self.centralwidget)
        self.countryLine.setGeometry(QtCore.QRect(440, 100, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.countryLine.setFont(font)
        self.countryLine.setAlignment(QtCore.Qt.AlignCenter)
        self.countryLine.setObjectName("countryLine")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 780, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.bothButton = QtWidgets.QPushButton(self.centralwidget)
        self.bothButton.setGeometry(QtCore.QRect(310, 150, 171, 31))
        self.bothButton.setObjectName("bothButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Primary energy consumption per capita (kWh/person)"))
        self.titleLabel.setText(_translate("MainWindow", "Primary energy consumption per capita (kWh/person)"))
        self.yearLabel.setText(_translate("MainWindow", "Year:"))
        self.countryLabel.setText(_translate("MainWindow", "Country/Region:"))
        self.yearLine.setPlaceholderText(_translate("MainWindow", "1965 - 2019"))
        self.yearButton.setText(_translate("MainWindow", "Search by year"))
        self.countryButton.setText(_translate("MainWindow", "Search by country"))
        self.countryLine.setPlaceholderText(_translate("MainWindow", "Select a country or a region"))
        self.bothButton.setText(_translate("MainWindow", "Year and contry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())