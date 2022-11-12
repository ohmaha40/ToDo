import sqlite3

from anzeige.frm_main import Ui_startfenster
from PySide6 import QtSql
from PySide6.QtWidgets import QApplication, QMainWindow
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


    def todo_eintragen(self):
        text = self.input_text_todo.text()
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        sql = "INSERT INTO todo_liste (Datum, [zu erledigen]) VALUES ('16.11.2022', ?)"
        cursor.execute(sql, (text,))
        conn.commit()
        conn.close()
        self.input_text_todo.setText("")
        self.todo_aktualisieren()



    def todo_aktualisieren(self):
        model = self.mod_todo
        model.select()
        self.tv_todo.setModel(model)


start_fenster = Start_Fenster()
start_fenster.show()
app.exec()
