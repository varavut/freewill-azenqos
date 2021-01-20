from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import pandas as pd
import params_disp_df
import global_config as gc


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


################################## df get functions


def get_wcdma_acive_monitored_df(dbcon, time_before):
    df_list = []

    cell_col_prefix_renamed = [
        "Cell ID",
        "Cell Name",
        "PSC",
        "Ec/Io",
        "RSCP ",
        "UARFCN",
    ]

    aset_col_prefix_sr = pd.Series(
        [
            "wcdma_aset_cellfile_matched_cellid_",
            "wcdma_aset_cellfile_matched_cellname_",
            "wcdma_aset_sc_",
            "wcdma_aset_ecio_",
            "wcdma_aset_rscp_",
            "wcdma_aset_cellfreq_",
        ]
    )
    aset_n_param = 3
    aset = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), aset_col_prefix_sr)),
            range(aset_n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        ("Time", ["time"]),
        (
            list(map(lambda x: "Aset{}".format(x + 1), range(aset_n_param))),
            aset,
            # list(map(lambda x: "wcdma_aset_cellfile_matched_cellid_{}".format(x+1), range(aset_n_param))) +
            # list(map(lambda x: "wcdma_aset_cellfile_matched_cellname_{}".format(x+1), range(aset_n_param))) +
            # list(map(lambda x: "wcdma_aset_sc_{}".format(x+1), range(aset_n_param))) +
            # list(map(lambda x: "wcdma_aset_ecio_{}".format(x+1), range(aset_n_param))) +
            # list(map(lambda x: "wcdma_aset_rscp_{}".format(x+1), range(aset_n_param))) +
            # list(map(lambda x: "wcdma_aset_cellfreq_{}".format(x+1), range(aset_n_param))),
            "wcdma_cell_meas",
        ),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="wcdma_cell_meas",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    # print("df.head():\n%s" % df.head())
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    # print("df.head():\n%s" % df.head())
    df_list.append(df)

    mset_col_prefix_sr = pd.Series(
        [
            "wcdma_mset_cellfile_matched_cellid_",
            "wcdma_mset_cellfile_matched_cellname_",
            "wcdma_mset_sc_",
            "wcdma_mset_ecio_",
            "wcdma_mset_rscp_",
            "wcdma_mset_cellfreq_",
        ]
    )
    mset_n_param = 6
    mset = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), mset_col_prefix_sr)),
            range(mset_n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        (
            list(map(lambda x: "Mset{}".format(x + 1), range(mset_n_param))),
            mset,
            "wcdma_cell_meas",
        ),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="wcdma_cell_meas",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    df_list.append(df)

    dset_col_prefix_sr = pd.Series(
        [
            "wcdma_dset_cellfile_matched_cellid_",
            "wcdma_dset_cellfile_matched_cellname_",
            "wcdma_dset_sc_",
            "wcdma_dset_ecio_",
            "wcdma_dset_rscp_",
            "wcdma_dset_cellfreq_",
        ]
    )
    dset_n_param = 4
    dset = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), dset_col_prefix_sr)),
            range(dset_n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        (
            list(map(lambda x: "Dset{}".format(x + 1), range(dset_n_param))),
            dset,
            "wcdma_cell_meas",
        ),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="wcdma_cell_meas",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df.columns = ["CellGroup"] + cell_col_prefix_renamed
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_wcdma_radio_params_disp_df(dbcon, time_before):
    parameter_to_columns_list = [
        (
            ["Time", "Tx Power", "Max Tx Power"],
            ["time," "wcdma_txagc", "wcdma_maxtxpwr",],
            "wcdma_tx_power",
        ),
        ("RSSI", ["wcdma_rssi"], "wcdma_rx_power"),
        ("SIR", ["wcdma_sir"], "wcdma_sir"),
        ("RRC State", ["wcdma_rrc_state"], "wcdma_rrc_state"),
        (
            ["Speech Codec TX", "Speech Codec RX"],
            ["gsm_speechcodectx", "gsm_speechcodecrx"],
            "vocoder_info",
        ),
        (
            ["Cell ID", "RNC ID"],
            ["android_cellid", "android_rnc_id"],
            "android_info_1sec",
        ),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_bler_sum_disp_df(dbcon, time_before):
    parameter_to_columns_list = [
        (
            [
                "Time",
                "BLER Average Percent",
                "BLER Calculation Window Size",
                "BLER N Transport Channels",
            ],
            [
                "time," "wcdma_bler_average_percent_all_channels",
                "wcdma_bler_calculation_window_size",
                "wcdma_bler_n_transport_channels",
            ],
            "wcdma_bler",
        ),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_wcdma_bler_transport_channel_df(dbcon, time_before):
    df_list = []

    cell_col_prefix_renamed = ["Transport Channel", "Percent", "Err", "Rcvd"]

    cell_col_prefix_sr = pd.Series(
        [
            "wcdma_bler_channel_",
            "wcdma_bler_percent_",
            "wcdma_bler_err_",
            "wcdma_bler_rcvd_",
        ]
    )
    n_param = 16
    bler = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), cell_col_prefix_sr)),
            range(n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        (list(map(lambda x: "{}".format(x + 1), range(n_param))), bler, "wcdma_bler"),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="wcdma_bler",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    # print("df.head():\n%s" % df.head())
    df.columns = ["Channel"] + cell_col_prefix_renamed
    # print("df.head():\n%s" % df.head())
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_wcdma_bearers_df(dbcon, time_before):
    df_list = []

    cell_col_prefix_renamed = ["Bearers ID", "Bearers Rate DL", "Bearers Rate UL"]

    cell_col_prefix_sr = pd.Series(
        [
            "data_wcdma_bearer_id_",
            "data_wcdma_bearer_rate_dl_",
            "data_wcdma_bearer_rate_ul_",
        ]
    )
    n_param = 10
    bearer = sum(
        map(
            lambda y: list(map(lambda x: x + "{}".format(y + 1), cell_col_prefix_sr)),
            range(n_param),
        ),
        [],
    )
    parameter_to_columns_list = [
        (
            list(map(lambda x: " {}".format(x + 1), range(n_param))),
            bearer,
            "wcdma_bearers",
        ),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="wcdma_bearers",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    # print("df.head():\n%s" % df.head())
    df.columns = ["Bearer"] + cell_col_prefix_renamed
    # print("df.head():\n%s" % df.head())
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df
