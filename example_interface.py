import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *

#from fileDataRead import readDataFile

class MonitoringApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        self.totalData = {} #Данные метеостанций
        self.data = [] #Данные по текщей метеостанции
        self.listStations = set()
        self.selectedItemListWidget = None

        self.navTab = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnalizeTab.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredictTab.clicked.connect(self.navigate), 4],
            'Мониторинг': [self.btnMonitoringTab.clicked.connect(self.navigate), 5],
            'Эксперт': [self.btnExportTab.clicked.connect(self.navigate), None]



        }



        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnMonitoringtab.clicked.connect(self.homeGo)

    def navigate(self):
        print(self.sender().text(), self.navTab[self.sender().text()][1])
        self.tabWidget.setCurrentIndex(self.navTab[self.sender().text()][1])


    def homeGo(self):
        self.tabWidget.setCurrentIndex(0)


app = QApplication(sys.argv)
ex = MonitoringApp()
ex.show()
sys.exit(app.exec())
