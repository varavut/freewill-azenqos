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
<<<<<<< HEAD
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

        # SER_PARAMS = [
        #     (COL_PCI, re.compile(r"nr_servingbeam_pci_(\d+)")),
        #     (COL_BEAM_ID, re.compile(r"nr_servingbeam_ssb_index_(\d+)")),
        #     (COL_RSRP, re.compile(r"nr_servingbeam_ss_rsrp_(\d+)")),
        #     (COL_RSRQ, re.compile(r"nr_servingbeam_ss_rsrq_(\d+)")),
        #     (COL_SINR, re.compile(r"nr_servingbeam_ss_sinr_(\d+)")),
        #     (COL_BAND, re.compile(r"nr_band_(\d+)")),
        #     (COL_BAND_TYPE, re.compile(r"nr_band_type_(\d+)")),
        #     (COL_BANDWIDTH, re.compile(r"nr_bw_(\d+)")),
        #     (COL_SSB_SCS, re.compile(r"nr_ssb_scs_(\d+)")),
        #     (COL_DL_FREQ, re.compile(r"nr_dl_frequency_(\d+)")),
        #     (COL_DL_ARFCN, re.compile(r"nr_dl_arfcn_(\d+)")),
        #     (COL_SCS, re.compile(r"nr_numerology_scs_(\d+)")),
        # ]

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

=======
        with sqlite3.connect(gc.databasePath) as dbcon:
            return get_nr_radio_params_disp_df(dbcon, self.timeFilter)
    
    def getServingAndNeighbors(self):
        with sqlite3.connect(gc.databasePath) as dbcon:
            return get_nr_serv_and_neigh_disp_df(dbcon, self.timeFilter)
        
>>>>>>> master
    def defaultData(self, fieldsList, dataList):
        fieldCount = len(fieldsList)
        if fieldCount > 0:
            for index in range(fieldCount):
                columnName = fieldsList[index]
                dataList.append([columnName, "", "", ""])
            return dataList


################################## df get functions


def get_nr_radio_params_disp_df(dbcon, time_before):
    n_param_args = 8
    parameter_to_columns_list = [
        ("Time", ["time"] ),            
        (  # these params below come together so query them all in one query
            [
                "Band",
                "ARFCN",
                "PCI",
                "RSRP",
                "RSRQ",
                "SINR"
            ],
            list(map(lambda x: "nr_band_{}".format(x+1), range(n_param_args))) +
            list(map(lambda x: "nr_dl_arfcn_{}".format(x+1), range(n_param_args))) +
            list(map(lambda x: "nr_servingbeam_pci_{}".format(x+1), range(n_param_args))) +
            list(map(lambda x: "nr_servingbeam_ss_rsrp_{}".format(x+1), range(n_param_args))) +
            list(map(lambda x: "nr_servingbeam_ss_rsrq_{}".format(x+1), range(n_param_args))) +
            list(map(lambda x: "nr_servingbeam_ss_sinr_{}".format(x+1), range(n_param_args)))
        ),
        (  # these params below come together but not same row with rsrp etc above so query them all in their own set below
            [
                "PUSCH TxPower",
                "PUCCH TxPower",
                "SRS TxPower"
            ],
            list(map(lambda x: "nr_pusch_tx_power_{}".format(x+1), range(n_param_args)))+
            list(map(lambda x: "nr_pucch_tx_power_{}".format(x+1), range(n_param_args)))+
            list(map(lambda x: "nr_srs_tx_power_{}".format(x+1), range(n_param_args)))
        )
    ]            
    return params_disp_df.get(dbcon, parameter_to_columns_list, time_before, default_table="nr_cell_meas", not_null_first_col=True, custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS)


def get_nr_serv_and_neigh_disp_df(dbcon, time_before):
    df_list = []

    pcell_scell_col_prefix_sr = pd.Series(["nr_dl_arfcn_", "nr_servingbeam_pci_", "nr_servingbeam_ss_rsrp_", "nr_servingbeam_ss_rsrq_", "nr_servingbeam_ss_sinr_"])
    pcell_scell_col_prefix_renamed = ["ARFCN","PCI", "RSRP","RSRQ","SINR"]
    parameter_to_columns_list = [
        ("Time", ["time"] ),
        (
            ["PCell","SCell1","SCell2","SCell3","SCell4","SCell5","SCell6","SCell7"],
            list(pcell_scell_col_prefix_sr+"1")+list(pcell_scell_col_prefix_sr+"2")+list(pcell_scell_col_prefix_sr+"3")+list(pcell_scell_col_prefix_sr+"4")+list(pcell_scell_col_prefix_sr+"5")+list(pcell_scell_col_prefix_sr+"6")+list(pcell_scell_col_prefix_sr+"7")+list(pcell_scell_col_prefix_sr+"8"),
        )
    ]
    df = params_disp_df.get(dbcon, parameter_to_columns_list, time_before, default_table="nr_cell_meas", not_null_first_col=True, custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS)
    #print("df.head():\n%s" % df.head())
    df.columns = ["CellGroup"]+pcell_scell_col_prefix_renamed
    #print("df.head():\n%s" % df.head())
    df_list.append(df)

    dcell_col_suffix_sr = pd.Series(["_pci_1", "_ss_rsrp_1", "_ss_rsrq_1", "_ss_sinr_1"])  # a mistake during elm sheets made this unnecessary _1 required
    dcell_col_renamed = ["PCI", "RSRP","RSRQ","SINR"]
    dparameter_to_columns_list = [
        (
            ["DCell1","DCell2","DCell3","DCell4"],
            list("nr_detectedbeam1"+dcell_col_suffix_sr) + list("nr_detectedbeam2"+dcell_col_suffix_sr) + list("nr_detectedbeam3"+dcell_col_suffix_sr) + list("nr_detectedbeam4"+dcell_col_suffix_sr),
        )

    ]
    dcell_df = params_disp_df.get(dbcon, dparameter_to_columns_list, time_before, default_table="nr_cell_meas", not_null_first_col=True, custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS)
    dcell_df.columns = ["CellGroup"]+dcell_col_renamed
    #print("dcell_df.head():\n%s" % dcell_df.head())
    df_list.append(dcell_df)

    final_df = pd.concat(df_list, sort=False)
    return final_df
