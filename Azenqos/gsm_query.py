from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class GsmDataQuery:
    def __init__(self, database, currentDateTimeString):
        self.timeFilter = ""
        self.azenqosDatabase = database
        if currentDateTimeString:
            self.timeFilter = currentDateTimeString

    def getRadioParameters(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {
                "name": "RxLev",
                "column": ["gsm_rxlev_full_dbm", "gsm_rxlev_sub_dbm"],
                "table": "gsm_cell_meas",
            },
            {
                "name": "RxQual",
                "column": ["gsm_rxqual_full", "gsm_rxqual_sub"],
                "table": "gsm_cell_meas",
            },
            {"name": "TA", "column": ["gsm_ta"], "table": "gsm_tx_meas",},
            {
                "name": "RLT (Max)",
                "column": ["gsm_radiolinktimeout_max"],
                "table": "gsm_rl_timeout_counter",
            },
            {
                "name": "RLT (Current)",
                "column": ["gsm_radiolinktimeout_current"],
                "table": "gsm_rlt_counter",
            },
            {
                "name": "DTX Used",
                "column": ["gsm_dtxused"],
                "table": "gsm_rr_measrep_params",
            },
            {"name": "TxPower", "column": ["gsm_txpower"], "table": "gsm_tx_meas",},
            {"name": "FER", "column": ["gsm_fer"], "table": "vocoder_info",},
        ]
        return elementDictList

    def getServingAndNeighbors(self):
        MAX_NEIGHBORS = 32
        elementDictList = [
            {
                "tableRow": 0,
                "tableCol": 0,
                "column": ["global_time"],
                "table": "global_time",
            },
            {"name": "Serving Cell:", "column": [], "table": "", "shiftRight": 1},
            {
                "name": "",
                "column": ["gsm_cellfile_matched_cellname"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 2,
                "column": ["gsm_lac"],
                "table": "gsm_serv_cell_info",
            },
            {
                "tableRow": 1,
                "tableCol": 3,
                "column": ["gsm_bsic"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 4,
                "column": ["gsm_arfcn_bcch"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 5,
                "column": ["gsm_rxlev_full_dbm"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 6,
                "column": ["gsm_c1"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 7,
                "column": ["gsm_c2"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 8,
                "column": ["gsm_c31"],
                "table": "gsm_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 9,
                "column": ["gsm_c32"],
                "table": "gsm_cell_meas",
            },
            {"name": "Neightbor Cells:", "column": [], "table": "", "shiftRight": 1},
        ]

        for n in range(MAX_NEIGHBORS):
            i = n + 1
            neighborRow = [
                {
                    "name": "#%d" % i,
                    "column": [
                        "gsm_cellfile_matched_neighbor_cellname",
                        "gsm_cellfile_matched_neighbor_lac_%d" % i,
                        "gsm_neighbor_bsic_%d" % i,
                        "gsm_neighbor_arfcn_%d" % i,
                        "gsm_neighbor_rxlev_dbm_%d" % i,
                        "gsm_neighbor_c1_%d" % i,
                        "gsm_neighbor_c2_%d" % i,
                        "gsm_neighbor_c31_%d" % i,
                        "gsm_neighbor_c32_%d" % i,
                    ],
                    "table": "gsm_cell_meas",
                },
            ]
            elementDictList += neighborRow

        return elementDictList

    def getCurrentChannel(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {
                "name": "Cellname",
                "column": ["gsm_cellfile_matched_cellname"],
                "table": "gsm_cell_meas",
            },
            {"name": "CGI", "column": ["gsm_cgi"], "table": "gsm_cell_meas",},
            {
                "name": "Channel type",
                "column": ["gsm_channeltype"],
                "table": "gsm_rr_chan_desc",
            },
            {
                "name": "Sub channel number",
                "column": ["gsm_subchannelnumber"],
                "table": "gsm_rr_subchan",
            },
            {
                "name": "Mobile Allocation Index Offset (MAIO)",
                "column": ["gsm_maio"],
                "table": "gsm_rr_chan_desc",
            },
            {
                "name": "Hopping Sequence Number (HSN)",
                "column": ["gsm_hsn"],
                "table": "gsm_rr_chan_desc",
            },
            {
                "name": "Cipering Algorithm",
                "column": ["gsm_cipheringalgorithm"],
                "table": "gsm_rr_cipher_alg",
            },
            {
                "name": "MS Power Control Level",
                "column": ["gsm_ms_powercontrollevel"],
                "table": "gsm_rr_power_ctrl",
            },
            {
                "name": "Channel Mode",
                "column": ["gsm_channelmode"],
                "table": "gsm_chan_mode",
            },
            {
                "name": "Speech Codec TX",
                "column": ["gsm_speechcodectx"],
                "table": "vocoder_info",
            },
            {
                "name": "Speech Codec RX",
                "column": ["gsm_speechcodecrx"],
                "table": "vocoder_info",
            },
            {
                "name": "Hopping Channel",
                "column": ["gsm_hoppingchannel"],
                "table": "gsm_rr_chan_desc",
            },
            {
                "name": "Hopping Frequencies",
                "column": ["gsm_hoppingfrequencies"],
                "table": "gsm_hopping_list",
            },
            {
                "name": "ARFCN BCCH",
                "column": ["gsm_arfcn_bcch"],
                "table": "gsm_cell_meas",
            },
            {
                "name": "ARFCN TCH",
                "column": ["gsm_arfcn_tch"],
                "table": "gsm_rr_chan_desc",
            },
            {
                "name": "Time slot",
                "column": ["gsm_timeslot"],
                "table": "gsm_rr_chan_desc",
            },
        ]

        return elementDictList

    def getCSlashI(self):
        maxUnits = 32
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
            {"name": "Worst", "column": ["gsm_coi_worst"], "table": "gsm_coi_per_chan"},
            {"name": "Avg", "column": ["gsm_coi_avg"], "table": "gsm_coi_per_chan"},
        ]

        for unit in range(0, maxUnits):
            unitNo = unit + 1
            unitRow = [
                {
                    "name": "#%d" % unitNo,
                    "column": ["gsm_coi_arfcn_%d" % unitNo, "gsm_coi_%d" % unitNo],
                    "table": "gsm_coi_per_chan",
                }
            ]
            elementDictList += unitRow
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
