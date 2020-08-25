from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import re
import sqlite3
import pandas as pd
import global_config as gc
import params_disp_df


class NrDataQuery:
    def __init__(self, database, currentDateTimeString):
        self.timeFilter = ""
        self.azenqosDatabase = database
        if currentDateTimeString:
            self.timeFilter = currentDateTimeString

    def getRadioParameters(self):
        # self.openConnection()
        # dataList = []

        MAX_SERVING = 8

        elementDictList = [
            {
                "name": "Beam ID",
                "column": [
                    "nr_servingbeam_ssb_index_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "Band",
                "column": [
                    "nr_band_%d" % (serveNo + 1) for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "Band Type",
                "column": [
                    "nr_band_type_%d" % (serveNo + 1) for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "ARFCN",
                "column": [
                    "nr_dl_arfcn_%d" % (serveNo + 1) for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "Frequency",
                "column": [
                    "nr_dl_frequency_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "PCI",
                "column": [
                    "nr_servingbeam_pci_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "RSRP",
                "column": [
                    "nr_servingbeam_ss_rsrp_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "RSRQ",
                "column": [
                    "nr_servingbeam_ss_rsrq_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "SINR",
                "column": [
                    "nr_servingbeam_ss_sinr_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "Bandwidth",
                "column": [
                    "nr_bw_%d" % (serveNo + 1) for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "SSB SCS",
                "column": [
                    "nr_ssb_scs_%d" % (serveNo + 1) for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "Numerology SCS",
                "column": [
                    "nr_numerology_scs_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "PUSCH Power",
                "column": [
                    "nr_pusch_tx_power_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "PUCCH Power",
                "column": [
                    "nr_pucch_tx_power_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
            {
                "name": "SRS Power",
                "column": [
                    "nr_srs_tx_power_%d" % (serveNo + 1)
                    for serveNo in range(MAX_SERVING)
                ],
                "table": "nr_cell_meas",
            },
        ]

        # queryString = """
        # SELECT
        # *
        # FROM
        # nr_cell_meas
        # WHERE
        # time <= '%s'
        # ORDER BY time DESC
        # LIMIT 1
        # """ % (
        #     self.timeFilter
        # )

        # query = QSqlQuery()

        # query.exec_(queryString)
        # record = query.record()
        # if query.first():
        #     for i in range(len(PARAMS)):
        #         (label, prefix) = PARAMS[i]
        #         row = [""] * (MAX_SERVING + 1)
        #         row[0] = label
        #         for arg in range(1, MAX_SERVING + 1):
        #             field_name = prefix + str(arg)
        #             filed_index = record.indexOf(field_name)
        #             if filed_index >= 0:
        #                 value = query.value(filed_index)
        #                 row[arg] = str(value or "")
        #         dataList.append(row)

        # self.closeConnection()
        return elementDictList

    def getServingAndNeighbors(self):
        MAX_SERVING = 8
        MAX_DETECTED = 10

        elementDictList = [
            {"name": "Serving:", "column": [], "table": "nr_cell_meas",},
        ]

        for serving in range(MAX_SERVING):
            servingNo = serving + 1
            servingElement = {
                "name": "",
                "column": [
                    "nr_servingbeam_pci_%d" % servingNo,
                    "nr_servingbeam_ssb_index_%d" % servingNo,
                    "nr_servingbeam_ss_rsrp_%d" % servingNo,
                    "nr_servingbeam_ss_rsrq_%d" % servingNo,
                    "nr_servingbeam_ss_sinr_%d" % servingNo,
                    "nr_band_%d" % servingNo,
                    "nr_band_type_%d" % servingNo,
                    "nr_bw_%d" % servingNo,
                    "nr_ssb_scs_%d" % servingNo,
                    "nr_dl_frequency_%d" % servingNo,
                    "nr_dl_arfcn_%d" % servingNo,
                    "nr_numerology_scs_%d" % servingNo,
                ],
                "table": "nr_cell_meas",
            }
            elementDictList.append(servingElement)

        elementDictList.append(
            {"name": "Detected:", "column": [], "table": "nr_cell_meas",}
        )
    
        for detected in range(MAX_DETECTED):
            detectedNo = detected + 1
            detectedElement = {
                "name": "",
                "column": [
                    "nr_detectedbeam%d_pci_1" % detectedNo,
                    "nr_detectedbeam%d_ssb_index_1" % detectedNo,
                    "nr_detectedbeam%d_ss_rsrp_1" % detectedNo,
                    "nr_detectedbeam%d_ss_rsrq_1" % detectedNo,
                    "nr_detectedbeam%d_ss_sinr_1" % detectedNo,
                ],
                "table": "nr_cell_meas",
            }
            elementDictList.append(detectedElement)

    ]
    dcell_df = params_disp_df.get(dbcon, dparameter_to_columns_list, time_before, default_table="nr_cell_meas", not_null_first_col=True, custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS)
    #print("0dcell_df.head():\n%s" % dcell_df.head())
    dcell_df.columns = ["CellGroup"]+dcell_col_renamed
    #print("dcell_df.head():\n%s" % dcell_df.head())
    df_list.append(dcell_df)

        # DET_PARAMS = [
        #     (COL_PCI, re.compile(r"nr_detectedbeam(\d+)_pci(?:_1)")),
        #     (COL_BEAM_ID, re.compile(r"nr_detectedbeam(\d+)_ssb_index(?:_1)")),
        #     (COL_RSRP, re.compile(r"nr_detectedbeam(\d+)_ss_rsrp(?:_1)")),
        #     (COL_RSRQ, re.compile(r"nr_detectedbeam(\d+)_ss_rsrq(?:_1)")),
        #     (COL_SINR, re.compile(r"nr_detectedbeam(\d+)_ss_sinr(?:_1)")),
        # ]

        return elementDictList

    def try_to_set_field_value(self, field_name, value, params_tuple, result_list):
        for param in params_tuple:
            (field_index, param_test) = param
            m = param_test.match(field_name)
            if m:
                arg = int(m.group(1)) - 1
                row = result_list[arg]
                row[field_index] = str(value or "")
                return True
        return False

    def defaultData(self, fieldsList, dataList):
        fieldCount = len(fieldsList)
        if fieldCount > 0:
            for index in range(fieldCount):
                columnName = fieldsList[index]
                dataList.append([columnName, "", "", ""])
            return dataList

    def openConnection(self):
        if self.azenqosDatabase is not None:
            self.azenqosDatabase.open()

    def closeConnection(self):
        self.azenqosDatabase.close()
