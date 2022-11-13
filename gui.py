import sqlite3
from anzeige.frm_main import Ui_startfenster
from PySide6 import QtSql, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from datetime import date
import sys
#app = QApplication()
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("db/database.db")
class Start_Fenster(QMainWindow, Ui_startfenster):
    def __init__(self):
        super(Start_Fenster, self).__init__()
        self.setupUi(self)
        self.pb_todo_eintragen.clicked.connect(self.todo_eintragen)
        self.todo_aktualisieren()
        self.tv_todo.setColumnWidth(0, 70)
        self.tv_todo.setColumnWidth(1, 600)
        self.tv_todo.setColumnWidth(2, 80)
        self.tv_todo.setColumnWidth(3, 80)
        self.tv_todo.setColumnWidth(4, 80)
        self.tv_todo.setColumnWidth(5, 70)
        self.tv_todo.setHorizontalHeaderLabels(("Datum", "Zu erledigen", "Bis wann", "Dringend", "Erledigt"))
        self.pb_Projekte.clicked.connect(self.todo_aendern)

    def todo_eintragen(self):
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        sql = "INSERT INTO todo_liste (Datum, [zu erledigen], bis_Datum, Dringlichkeit, Erledigt) VALUES (?, ?, ?, ?, '0')"
        cursor.execute(sql, (date.today().strftime('%d.%m.%Y'), self.input_text_todo.text(), self.date_end_todo.date().toString(("dd.MM.yyyy")), self.cb_dringlichkeit.currentText(),))
        conn.commit()
        conn.close()
        self.input_text_todo.setText("")
        self.todo_aktualisieren()
    def todo_aktualisieren(self):
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        sqlquery = "SELECT * FROM todo_liste WHERE Erledigt <> 1"
        rowcount = 1
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tv_todo.setRowCount(rowcount)
            self.tv_todo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tv_todo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tv_todo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tv_todo.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tv_todo.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))

            rowcount+=1
            tablerow+=1
        conn.close()
    def todo_aendern(self):
        for i in self.tv_todo.selectedItems():
            print(i.text())
        for i in self.tv_todo.selectedIndexes():
            print(i.row())
            print(i.column())

    # def test_funktionen(self):
    #     print(self.cb_dringlichkeit.currentText())

app = QApplication(sys.argv)
start_fenster = Start_Fenster()

start_fenster.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")

