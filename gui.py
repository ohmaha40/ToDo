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
        self.pb_todo_eintragen.clicked.connect(self.todo_eintragen())
        self.todo_aktualisieren()


    def todo_eintragen(self):
        model = self.mod_todo
        # query = QtSql.QSqlQuery()
        # test = """ insert into todo_liste set
        # Datum = 20.11.2022,
        # [zu erledigen] = testes aus programm,
        # bis_Datum = 21.11.2022"""
        # query.exec(test)
        # model.select()
        # self.tv_todo.setModel(model)


    def todo_aktualisieren(self):
        model = self.mod_todo
        # query = QtSql.QSqlQuery()
        # abfrage = """update todo_liste set
        # xxx = YYYY,
        # XXX = YYYY
        # query.exec(abfrage)
        model.select()
        self.tv_todo.setModel(model)


start_fenster = Start_Fenster()
start_fenster.show()
app.exec()
