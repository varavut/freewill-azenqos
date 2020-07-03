from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class CdmaEvdoQuery:
    def __init__(self, database, currentDateTimeString):
        self.timeFilter = ""
        self.azenqosDatabase = database
        if currentDateTimeString:
            self.timeFilter = currentDateTimeString

    def getRadioParameters(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {
                "name": "Active PN (Best)",
                "column": ["cdma_cell_pn_1"],
                "table": "cdma",
            },
            {"name": "Ec/Io", "column": ["cdma_ecio_1"], "table": "cdma",},
            {"name": "RX Power", "column": ["cdma_rx_power"], "table": "cdma",},
            {"name": "TX Power", "column": ["cdma_tx_power"], "table": "cdma",},
            {"name": "FER", "column": ["cdma_fer"], "table": "cdma",},
            {"name": "Channel", "column": ["cdma_channel"], "table": "cdma",},
            {"name": "Band class", "column": ["cdma_band_class"], "table": "cdma",},
            {
                "name": "N Active Set Cells",
                "column": ["cdma_n_aset_cells"],
                "table": "cdma",
            },
        ]

        return elementDictList

    def getServingAndNeighbors(self):
        MAX_NEIGHBORS = 32

        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
        ]

        for n in range(MAX_NEIGHBORS):
            i = n + 1
            neighborRow = [
                {
                    "name": "#%d" % i,
                    "column": [
                        "cdma_cell_pn_%d" % i,
                        "cdma_ecio_%d" % i,
                        "cdma_cell_type_%d" % i,
                    ],
                    "table": "cdma",
                },
            ]
            elementDictList += neighborRow

        return elementDictList

    def getEvdoParameters(self):
        MAX_EVDO = 6

        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {"name": "DRC", "column": ["cdma_evdo_drc"], "table": "cdma",},
            {"name": "PER", "column": ["cdma_evdo_per"], "table": "cdma",},
            {"name": "", "column": [], "table": "cdma",},
            {"name": "SINR Per PN:", "column": [], "table": "cdma",},
            {"name": "PN", "column": [], "table": "cdma",},
            {"tableRow": 5, "tableCol": 1, "name": "SINR"},
        ]
        for index in range(MAX_EVDO):
            i = index + 1
            evdoRow = [
                {
                    "name": "#%d" % i,
                    "column": ["cdma_evdo_pn_%d" % i, "cdma_evdo_sinr_%d" % i,],
                    "table": "cdma",
                    "shiftLeft": 1,
                },
            ]
            elementDictList += evdoRow

        return elementDictList

    def openConnection(self):
        if self.azenqosDatabase is not None:
            self.azenqosDatabase.open()

    def closeConnection(self):
        self.azenqosDatabase.close()

    def defaultData(self, fieldsList):
        fieldCount = len(fieldsList)
        if fieldCount > 0:
            dataList = []
            for index in range(fieldCount):
                columnName = fieldsList[index]
                value = ""
                dataList.append([columnName, value, "", ""])
            return dataList
