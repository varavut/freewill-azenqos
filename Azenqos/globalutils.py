from PyQt5.QtSql import QSql, QSqlDatabase, QSqlQuery
import csv, inspect, os, sys, datetime, json, io
from zipfile import ZipFile
import shutil

# Adding folder path
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
import global_config as gc

db = None
elementData = []


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


# todo: ใช้ข้อมูลจาก csv อ้างอิงชื่อแต่ละ element
class ElementInfo:
    data = []

    def __init__(self):
        global elementData
        reader = csv.DictReader(open("element_info_list.csv"))
        for row in reader:
            if row["name"]:
                rowdict = {
                    "name": row["name"],
                    "column_name": row["var_name"],
                    "db_table": row["db_table"],
                }
                elementData.append(rowdict)

    def getTableAttr(self, name: str):
        for obj in elementData:
            if obj["name"] == name:
                source = [obj["column_name"], obj["db_table"]]
                query = Query(source[0], source[1], "").query()
                table = Table()
                table.row.setSource(source)
                table.row.setDatarow(query)
                table.printdata()

    def checkCsv(self):
        print(elementData)

    def searchName(self, name: str, obj_list: list):
        for obj in obj_list:
            if name in obj["name"]:
                return obj

    def addDatabase(self):
        databasePath = "/Users/Maxorz/Desktop/DB_Test/ARGazqdata.db"
        global db
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(databasePath)


class Row:
    source = []
    datarow = []

    def setSource(self, source):
        self.source = source

    def setDatarow(self, datarow):
        self.datarow = datarow


class Table:
    row = Row()

    def setTableModel(self):
        return False

    def printdata(self):
        print([self.row.source, self.row.datarow])


class Query(object):
    def __init__(self, column_name: str, table_name: str, condition: str):
        self.column_name = column_name
        self.table_name = table_name

    def query(self):
        condition = ""
        result = []
        # inputdata = ['table','value','row',column']
        # if self.globalTime:
        #     condition = 'WHERE time <= \'%s\'' % (self.globalTime)
        if not db.isOpen():
            db.open()
        query = QSqlQuery()
        queryString = "SELECT %s FROM %s WHERE %s IS NOT NULL LIMIT 1" % (
            self.column_name,
            self.table_name,
            self.column_name,
        )
        query.exec_(queryString)
        while query.next():
            result.append(query.value(0))
        db.close()
        return result


class Utils:
    def __init__(self):
        super().__init__()

    def unzipToFile(self, currentPath, filePath):
        gc.logPath = currentPath + "/file/" + str(os.getpid())
        try:
            if not os.path.exists(currentPath + "/file"):
                os.mkdir(currentPath + "/file")
            if not os.path.exists(gc.logPath):
                os.mkdir(gc.logPath)
            else:
                shutil.rmtree(gc.logPath)
                os.mkdir(gc.logPath)
            if len(os.listdir(gc.logPath)) == 0:
                with ZipFile(filePath, "r") as zip_obj:
                    filesContain = zip_obj.namelist()
                    for fileName in filesContain:
                        zip_obj.extract(fileName, gc.logPath)
                db_file_path = gc.logPath + "/azqdata.db"
                return db_file_path
        except Exception as e:
            print(e)

    def cleanupFile(self, currentPath):
        # gc.logPath = currentPath + "/" + os.path.basename(filePath)
        file_list = os.listdir(gc.logPath)
        try:
            if len(file_list) > 0:
                for f in file_list:
                    os.remove(gc.logPath + "/" + f)
        except:
            return False

        return True

    def openConnection(self, db: QSqlDatabase):
        print("%s: openConnection" % os.path.basename(__file__))
        if db:
            if not db.isOpen():
                db.open()

    def closeConnection(self, db: QSqlDatabase):
        print("%s: closeConnection" % os.path.basename(__file__))
        if db:
            if db.isOpen():
                db.close()

    def datetimeStringtoTimestamp(self, datetimeString: str):
        # print("%s: datetimestringtotimestamp" % os.path.basename(__file__))
        try:
            element = datetime.datetime.strptime(datetimeString, "%Y-%m-%d %H:%M:%S.%f")
            timestamp = datetime.datetime.timestamp(element)
            return timestamp
        except Exception as ex:
            print(ex)
            return False
