# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_fenster.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QHeaderView, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_startfenster(object):
    def setupUi(self, startfenster):
        if not startfenster.objectName():
            startfenster.setObjectName(u"startfenster")
        startfenster.resize(1000, 600)
        startfenster.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(startfenster)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_text_todo = QLineEdit(self.centralwidget)
        self.input_text_todo.setObjectName(u"input_text_todo")
        self.input_text_todo.setGeometry(QRect(30, 60, 351, 51))
        self.date_end_todo = QDateEdit(self.centralwidget)
        self.date_end_todo.setObjectName(u"date_end_todo")
        self.date_end_todo.setGeometry(QRect(390, 60, 110, 22))
        self.date_end_todo.setFocusPolicy(Qt.WheelFocus)
        self.date_end_todo.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.date_end_todo.setLayoutDirection(Qt.LeftToRight)
        self.date_end_todo.setAlignment(Qt.AlignCenter)
        self.date_end_todo.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date_end_todo.setDateTime(QDateTime(QDate(2022, 10, 13), QTime(12, 0, 0)))
        self.date_end_todo.setMinimumDate(QDate(2022, 10, 11))
        self.date_end_todo.setCalendarPopup(True)
        self.cb_dringlichkeit = QComboBox(self.centralwidget)
        self.cb_dringlichkeit.addItem("")
        self.cb_dringlichkeit.addItem("")
        self.cb_dringlichkeit.addItem("")
        self.cb_dringlichkeit.setObjectName(u"cb_dringlichkeit")
        self.cb_dringlichkeit.setGeometry(QRect(390, 90, 111, 22))
        self.cb_dringlichkeit.setEditable(True)
        self.pb_todo_eintragen = QPushButton(self.centralwidget)
        self.pb_todo_eintragen.setObjectName(u"pb_todo_eintragen")
        self.pb_todo_eintragen.setGeometry(QRect(30, 120, 351, 24))
        self.pb_Projekte = QPushButton(self.centralwidget)
        self.pb_Projekte.setObjectName(u"pb_Projekte")
        self.pb_Projekte.setGeometry(QRect(550, 70, 411, 24))
        self.tv_todo = QTableWidget(self.centralwidget)
        if (self.tv_todo.columnCount() < 5):
            self.tv_todo.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tv_todo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tv_todo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tv_todo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tv_todo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tv_todo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tv_todo.setObjectName(u"tv_todo")
        self.tv_todo.setGeometry(QRect(30, 160, 931, 391))
        startfenster.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(startfenster)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        startfenster.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(startfenster)
        self.statusbar.setObjectName(u"statusbar")
        startfenster.setStatusBar(self.statusbar)

        self.retranslateUi(startfenster)

        QMetaObject.connectSlotsByName(startfenster)
    # setupUi

    def retranslateUi(self, startfenster):
        startfenster.setWindowTitle(QCoreApplication.translate("startfenster", u"MainWindow", None))
        self.cb_dringlichkeit.setItemText(0, QCoreApplication.translate("startfenster", u"hoch", None))
        self.cb_dringlichkeit.setItemText(1, QCoreApplication.translate("startfenster", u"mittel", None))
        self.cb_dringlichkeit.setItemText(2, QCoreApplication.translate("startfenster", u"niedrig", None))

        self.pb_todo_eintragen.setText(QCoreApplication.translate("startfenster", u"Todo eintragen", None))
        self.pb_Projekte.setText(QCoreApplication.translate("startfenster", u"Projekte", None))
        ___qtablewidgetitem = self.tv_todo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("startfenster", u"spalte 1", None));
        ___qtablewidgetitem1 = self.tv_todo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("startfenster", u"spalte 2", None));
        ___qtablewidgetitem2 = self.tv_todo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("startfenster", u"spalte 3", None));
        ___qtablewidgetitem3 = self.tv_todo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("startfenster", u"spalte 4", None));
        ___qtablewidgetitem4 = self.tv_todo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("startfenster", u"spalte 5", None));
    # retranslateUi

