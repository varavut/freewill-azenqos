from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class WcdmaDataQuery:
    def __init__(self, database, currentDateTimeString):
        self.timeFilter = ""
        self.azenqosDatabase = database
        if currentDateTimeString:
            self.timeFilter = currentDateTimeString

    def getActiveMonitoredSets(self):
        maxUnits = 27
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
        ]
        for unit in range(maxUnits):
            unitNo = unit + 1
            unitRow = [
                {
                    "name": "#%d" % unitNo,
                    "table": "wcdma_cells_combined",
                    "column": [
                        "wcdma_cellfile_matched_cellname_%d" % unitNo,
                        "wcdma_celltype_%d" % unitNo,
                        "wcdma_sc_%d" % unitNo,
                        "wcdma_ecio_%d" % unitNo,
                        "wcdma_rscp_%d" % unitNo,
                        "wcdma_cellfreq_%d" % unitNo,
                    ],
                },
                {
                    "tableRow": 1 + unit,
                    "tableCol": 7,
                    "column": ["wcdma_prevmeasevent"],
                    "table": "wcdma_rrc_meas_events",
                },
            ]
            elementDictList += unitRow
        return elementDictList

    def getRadioParameters(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time"},
            {"name": "Tx Power", "column": ["wcdma_txagc"], "table": "wcdma_tx_power"},
            {
                "name": "Max Tx Power",
                "column": ["wcdma_maxtxpwr"],
                "table": "wcdma_tx_power",
            },
            {"name": "RSSI", "column": ["wcdma_rssi"], "table": "wcdma_rx_power"},
            {"name": "SIR", "column": ["wcdma_sir"], "table": "wcdma_sir"},
            {
                "name": "RRC State",
                "column": ["wcdma_rrc_state"],
                "table": "wcdma_rrc_state",
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
                "name": "Cell ID",
                "column": ["android_cellid"],
                "table": "android_info_1sec",
            },
            {
                "name": "RNC ID",
                "column": ["android_rnc_id"],
                "table": "android_info_1sec",
            },
        ]
        return elementDictList

    def getActiveSetList(self):
        maxUnits = 3
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
        ]

        for unit in range(maxUnits):
            unitNo = unit + 1
            unitRow = [
                {
                    "name": "#%d" % unitNo,
                    "column": ["wcdma_aset_cellfreq_%d" % unitNo],
                    "table": "wcdma_cell_meas",
                },
                {
                    "tableRow": 1 + unit,
                    "tableCol": 2,
                    "column": ["wcdma_activeset_psc_%d" % unitNo],
                    "table": "wcdma_aset_full_list",
                },
                {
                    "tableRow": 1 + unit,
                    "tableCol": 3,
                    "column": ["wcdma_activeset_cellposition_%d" % unitNo],
                    "table": "wcdma_aset_full_list",
                },
                {
                    "tableRow": 1 + unit,
                    "tableCol": 4,
                    "column": ["wcdma_activeset_celltpc_%d" % unitNo],
                    "table": "wcdma_aset_full_list",
                },
                {
                    "tableRow": 1 + unit,
                    "tableCol": 5,
                    "column": ["wcdma_activeset_diversity_%d" % unitNo],
                    "table": "wcdma_aset_full_list",
                },
            ]
            elementDictList += unitRow

        return elementDictList

    def getMonitoredSetList(self):
        maxUnits = 32
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
        ]
        for unit in range(maxUnits):
            unitNo = unit + 1
            unitRow = [
                {
                    "name": "#%d" % unitNo,
                    "column": [
                        "wcdma_neighborset_downlinkfreq_%d" % unitNo,
                        "wcdma_neighborset_psc_%d" % unitNo,
                        "wcdma_neighborset_cellposition_%d" % unitNo,
                        "wcdma_neighborset_diversity_%d" % unitNo,
                    ],
                    "table": "wcdma_nset_full_list",
                },
            ]
            elementDictList += unitRow
        return elementDictList

    def getBlerSummary(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time"},
            {
                "name": "BLER Average Percent",
                "column": ["wcdma_bler_average_percent_all_channels"],
                "table": "wcdma_bler",
            },
            {
                "name": "BLER Calculation Window Size",
                "column": ["wcdma_bler_calculation_window_size"],
                "table": "wcdma_bler",
            },
            {
                "name": "BLER N Transport Channels",
                "column": ["wcdma_bler_n_transport_channels"],
                "table": "wcdma_bler",
            },
        ]
        return elementDictList

    def getBLER_TransportChannel(self):
        elementDictList = []
        maxChannel = 16

        for channel in range(maxChannel):
            channelNo = channel + 1
            channelRow = [
                {
                    "name": "",
                    "column": [
                        "wcdma_bler_channel_%d" % channelNo,
                        "wcdma_bler_percent_%d" % channelNo,
                        "wcdma_bler_err_%d" % channelNo,
                        "wcdma_bler_rcvd_%d" % channelNo,
                    ],
                    "table": "wcdma_bler",
                    "shiftLeft": 1,
                }
            ]
            elementDictList += channelRow

        return elementDictList

    def getBearers(self):
        maxBearers = 10
        elementDictList = []

        for bearers in range(maxBearers):
            bearerNo = bearers + 1
            bearerRow = [
                {
                    "name": "#%d" % bearerNo,
                    "column": [
                        "data_wcdma_bearer_id_%d" % bearerNo,
                        "data_wcdma_bearer_rate_dl_%d" % bearerNo,
                        "data_wcdma_bearer_rate_ul_%d" % bearerNo,
                    ],
                    "table": "wcdma_bearers",
                }
            ]
            elementDictList += bearerRow

        return elementDictList

    def getPilotPolutingCells(self):
        maxPollution = 32
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
        ]
        for pollution in range(maxPollution):
            pollutionNo = pollution + 1
            pollutionRow = [
                {
                    "name": "#%d" % pollutionNo,
                    "column": [
                        "wcdma_pilot_polluting_cell_sc_%d" % pollutionNo,
                        "wcdma_pilot_polluting_cell_rscp_%d" % pollutionNo,
                        "wcdma_pilot_polluting_cell_ecio_%d" % pollutionNo,
                    ],
                    "table": "wcdma_pilot_pollution",
                    "shiftRight": 1,
                }
            ]
            elementDictList += pollutionRow

        return elementDictList

    def getActiveMonitoredBar(self):
        maxItem = 27
        elementDictList = []

        for item in range(maxItem):
            itemNo = item + 1
            itemRow = [
                {
                    "name": "",
                    "column": [
                        "wcdma_celltype_%d" % itemNo,
                        "wcdma_ecio_%d" % itemNo,
                        "wcdma_rscp_%d" % itemNo,
                    ],
                    "table": "wcdma_cells_combined",
                    "shiftLeft": 1,
                }
            ]
            elementDictList += itemRow

        return elementDictList

    def getCmGsmCells(self):
        elementDictList = [
            {
                "name": "Time",
                "column": ["global_time"],
                "table": "global_time",
                "shiftLeft": 1,
            },
            {
                "tableRow": 0,
                "tableCol": 1,
                "column": ["wcdma_cm_gsm_meas_arfcn"],
                "table": "wcdma_cm_gsm_meas",
            },
            {
                "tableRow": 0,
                "tableCol": 2,
                "column": ["wcdma_cm_gsm_meas_rxlev"],
                "table": "wcdma_cm_gsm_meas",
            },
            {
                "tableRow": 0,
                "tableCol": 3,
                "column": ["wcdma_cm_gsm_meas_bsic"],
                "table": "wcdma_cm_gsm_meas",
            },
            {
                "tableRow": 0,
                "tableCol": 4,
                "column": ["wcdma_cm_gsm_meas_cell_measure_state"],
                "table": "wcdma_cm_gsm_meas",
            },
        ]

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
