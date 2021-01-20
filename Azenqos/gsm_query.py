from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import pandas as pd
import params_disp_df
import global_config as gc


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


################################## df get functions


def get_gsm_radio_params_disp_df(dbcon, time_before):
    df_list = []
    parameter_to_columns_list = [
        (
            ["Time", "RxLev Full", "RxLev Sub", "RxQual Full", "RxQual Sub",],
            [
                "time," "gsm_rxlev_full_dbm",
                "gsm_rxlev_sub_dbm",
                "gsm_rxqual_full",
                "gsm_rxqual_sub",
            ],
            "gsm_cell_meas",
        ),
        ("TA", ["gsm_ta"], "gsm_tx_meas"),
        ("RLT (Max)", ["gsm_radiolinktimeout_max"], "gsm_rl_timeout_counter"),
        ("RLT (Current)", ["gsm_radiolinktimeout_current"], "gsm_rlt_counter"),
        ("DTX Used", ["gsm_dtxused"], "gsm_rr_measrep_params"),
        ("TxPower", ["gsm_txpower"], "gsm_tx_meas"),
        ("FER", ["gsm_fer"], "vocoder_info"),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["Parameter", "Value"]
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_gsm_serv_and_neigh__df(dbcon, time_before):
    df_list = []

    cell_col_prefix_renamed = [
        "Cell Name",
        "BSIC",
        "ARFCN ",
        "RxLev",
        "C1",
        "C2",
        "C31",
        "C32",
    ]
    serv_col_prefix_sr = pd.Series(
        [
            "gsm_cellfile_matched_cellname",
            "gsm_bsic",
            "gsm_arfcn_bcch",
            "gsm_rxlev_sub_dbm",
            "gsm_c1",
            "gsm_c2",
            "gsm_c31",
            "gsm_c32",
        ]
    )
    parameter_to_columns_list = [
        ("serv", list(serv_col_prefix_sr),),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="gsm_cell_meas",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    df_list.append(df)

    lac_col_prefix_sr = pd.Series(["gsm_lac",])
    parameter_to_columns_list = [
        ("serv", list(lac_col_prefix_sr),),
    ]
    df2 = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="gsm_serv_cell_info",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df2.columns = ["CellGroup", "LAC"]
    df.insert(2, "LAC", df2["LAC"])

    neigh_col_prefix_sr = pd.Series(
        [
            "gsm_cellfile_matched_neighbor_cellname",
            "gsm_cellfile_matched_neighbor_lac_",
            "gsm_neighbor_bsic_",
            "gsm_neighbor_arfcn_",
            "gsm_neighbor_rxlev_dbm_",
            "gsm_neighbor_c1_",
            "gsm_neighbor_c2_",
            "gsm_neighbor_c31_",
            "gsm_neighbor_c32_",
        ]
    )
    neigh_n_param = 32

    def name_map(x, y):
        if x == "gsm_cellfile_matched_neighbor_cellname":
            if y == 0:
                return "gsm_cellfile_matched_neighbor_cellname"
            else:
                return '"" as unsed_{}'.format(y + 1)
        return x + "{}".format(y + 1)

    neigh = sum(
        map(
            lambda y: list(map(lambda x: name_map(x, y), neigh_col_prefix_sr)),
            range(neigh_n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        (list(map(lambda x: "neigh{}".format(x + 1), range(neigh_n_param))), neigh,),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="gsm_cell_meas",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = [
        "CellGroup",
        "Cell Name",
        "LAC",
        "BSIC",
        "ARFCN ",
        "RxLev",
        "C1",
        "C2",
        "C31",
        "C32",
    ]
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_gsm_current_channel_disp_df(dbcon, time_before):
    df_list = []
    parameter_to_columns_list = [
        (
            ["Time", "Cellname", "CGI",],
            ["time," "gsm_cellfile_matched_cellname", "gsm_cgi",],
            "gsm_cell_meas",
        ),
        ("Channel Type", ["gsm_channeltype"], "gsm_rr_chan_desc"),
        ("Sub Channel Number", ["gsm_subchannelnumber"], "gsm_rr_subchan"),
        (
            ["Mobile Allocation Index Offset (MAIO)", "Hopping Sequence Number (HSN)"],
            ["gsm_maio", "gsm_hsn"],
            "gsm_rr_chan_desc",
        ),
        ("Cipering Algorithm", ["gsm_cipheringalgorithm"], "gsm_rr_cipher_alg"),
        ("MS Power Control Level", ["gsm_ms_powercontrollevel"], "gsm_rr_power_ctrl"),
        ("Channel Mode", ["gsm_channelmode"], "gsm_chan_mode"),
        (
            ["Speech Codec TX", "Speech Codec RX"],
            ["gsm_speechcodectx", "gsm_speechcodecrx"],
            "vocoder_info",
        ),
        ("Hopping Frequencies", ["gsm_hoppingfrequencies"], "gsm_hopping_list"),
        ("ARFCN BCCH", ["gsm_arfcn_bcch"], "gsm_cell_meas"),
        ("ARFCN TCH", ["gsm_arfcn_tch"], "gsm_rr_chan_desc"),
        ("Time Slot", ["gsm_timeslot"], "gsm_rr_chan_desc"),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["Parameter", "Value"]
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_coi_df(dbcon, time_before):
    df_list = []

    cell_col_prefix_renamed = ["ARFCN", "VALUE"]
    worst_col_prefix_sr = pd.Series(["gsm_coi_worst_arfcn_1", "gsm_coi_worst"])
    parameter_to_columns_list = [
        ("Time", ["time"]),
        ("Worst", list(worst_col_prefix_sr),),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="gsm_coi_per_chan",
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    df_list.append(df)

    avg_col_prefix_sr = pd.Series(["gsm_coi_arfcn_", "gsm_coi_"])
    avg_n_param = 32

    avg = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), avg_col_prefix_sr)),
            range(avg_n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        ("Avg", ['""']),
        (list(map(lambda x: "", range(avg_n_param))), avg,),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="gsm_coi_per_chan",
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df
