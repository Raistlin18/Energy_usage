from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys
from file_handler import get_dicts_from_csv

data = get_dicts_from_csv('energy.csv')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.yearButton.clicked.connect(self.search_by_year)
        self.ui.countryButton.clicked.connect(self.search_by_country)
        self.ui.bothButton.clicked.connect(self.search_by_both)
        self.ui.tableWidget.itemSelectionChanged.connect(self.show_selected)


        self.tables()

    def tables(self):

        entities = []
        for i in data:
            entities.append({'Country': i['Entity'], 'Year': i['Year'], 'Value': i['Primary energy consumption per capita (kWh/person)']})

        self.ui.tableWidget.setRowCount(len(entities))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Country", "Year", "Value"])
        self.ui.tableWidget.setColumnWidth(0, 310)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setStyleSheet("QTableWidget {font-size: 12pt; font-family: Arial; padding: 5px;} QHeaderView::section {background-color: #e0e0e0; font-size: 12pt; font-family: Arial; alignment: center;}")
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.ui.tableWidget.setSortingEnabled(True)

        for entity in entities:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(entity['Country']))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(entity['Year']))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(entity['Value']))

    def search_by_year(self):
        year = self.ui.yearLine.text()
        self.ui.tableWidget.setRowCount(0)
        for i in data:
            if i['Year'] == year:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i['Entity']))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i['Year']))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(i['Primary energy consumption per capita (kWh/person)']))

    def search_by_country(self):
        country = self.ui.countryLine.text()
        self.ui.tableWidget.setRowCount(0)
        for i in data:
            if i['Entity'].lower() == country.lower():
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i['Entity']))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i['Year']))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(i['Primary energy consumption per capita (kWh/person)']))

    def search_by_both(self):
        country = self.ui.countryLine.text()
        year = self.ui.yearLine.text()
        self.ui.tableWidget.setRowCount(0)
        for i in data:
            if i['Entity'].lower() == country.lower() and i['Year'] == year:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i['Entity']))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(i['Year']))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(i['Primary energy consumption per capita (kWh/person)']))

    def show_selected(self):
        selected = self.ui.tableWidget.selectedItems()
        self.ui.countryLine.setText(selected[0].text())
        self.ui.yearLine.setText(selected[1].text())

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_app()

