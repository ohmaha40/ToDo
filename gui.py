import sqlite3
from anzeige.frm_main import Ui_startfenster
from PySide6 import QtSql, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from datetime import date
app = QApplication()
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("db/database.db")
class Start_Fenster(QMainWindow, Ui_startfenster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mod_todo = QtSql.QSqlRelationalTableModel()
        self.mod_todo.setTable("todo_liste")
        self.pb_todo_eintragen.clicked.connect(self.todo_eintragen)
        self.todo_aktualisieren()
        self.tv_todo.setColumnWidth(0, 20)
        self.tv_todo.setColumnWidth(1, 80)
        self.tv_todo.setColumnWidth(2, 640)
        self.tv_todo.setColumnWidth(3, 80)
        self.tv_todo.setColumnWidth(4, 80)
        #self.test_funktionen()("Datum", "Zu erledigen", "Bis wann", "Dringend")

    def todo_eintragen(self):
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        sql = "INSERT INTO todo_liste (Datum, [zu erledigen], bis_Datum, Dringlichkeit) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (date.today().strftime('%d.%m.%Y'), self.input_text_todo.text(), self.date_end_todo.date().toString(("dd.MM.yyyy")), self.cb_dringlichkeit.currentText(),))
        conn.commit()
        conn.close()
        self.input_text_todo.setText("")
        self.todo_aktualisieren()
    def todo_aktualisieren(self):
        model = self.mod_todo
        sqlquery = "SELECT * FROM todo_liste"
        model.itemData(sqlquery)
        self.tv_todo.setModel(model)
        # conn = sqlite3.connect("db/database.db")
        # cursor = conn.cursor()
        # sqlquery = "SELECT * FROM todo_liste"
        # tablerow = 0
        # for row in cursor.execute(sqlquery):
        #     self.tv_todo.(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
        #
        #     tablerow+=1
        #     print(row)
        # model = self.mod_todo
        # model.selectRow()ct()
        # self.tv_todo.setModel(model)
    # def test_funktionen(self):
    #     print(self.cb_dringlichkeit.currentText())


start_fenster = Start_Fenster()
start_fenster.show()
app.exec()
