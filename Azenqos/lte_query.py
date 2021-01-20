from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import pandas as pd
import params_disp_df
import global_config as gc


class LteDataQuery:
    def __init__(self, database, currentDateTimeString):
        self.timeFilter = ""
        self.azenqosDatabase = database
        if currentDateTimeString:
            self.timeFilter = currentDateTimeString

    def getRadioParameters(self):

        # add Time for first row
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {
                "name": "Band",
                "column": ["lte_band_1", "lte_band_2", "lte_band_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "E-ARFCN",
                "column": ["lte_earfcn_1", "lte_earfcn_2", "lte_earfcn_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving PCI",
                "column": [
                    "lte_physical_cell_id_1",
                    "lte_physical_cell_id_2",
                    "lte_physical_cell_id_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRP[0]",
                "column": [
                    "lte_inst_rsrp_rx0_1",
                    "lte_inst_rsrp_rx0_2",
                    "lte_inst_rsrp_rx0_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRP[1]",
                "column": [
                    "lte_inst_rsrp_rx1_1",
                    "lte_inst_rsrp_rx1_2",
                    "lte_inst_rsrp_rx1_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRP",
                "column": ["lte_inst_rsrp_1", "lte_inst_rsrp_2", "lte_inst_rsrp_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRQ[0]",
                "column": [
                    "lte_inst_rsrq_rx0_1",
                    "lte_inst_rsrq_rx0_2",
                    "lte_inst_rsrq_rx0_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRQ[1]",
                "column": [
                    "lte_inst_rsrq_rx1_1",
                    "lte_inst_rsrq_rx1_2",
                    "lte_inst_rsrq_rx1_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "Serving RSRQ",
                "column": ["lte_inst_rsrq_1", "lte_inst_rsrq_2", "lte_inst_rsrq_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "SINR Rx[0]",
                "column": ["lte_sinr_rx0_1", "lte_sinr_rx0_2", "lte_sinr_rx0_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "SINR Rx[1]",
                "column": ["lte_sinr_rx1_1", "lte_sinr_rx1_2", "lte_sinr_rx1_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "SINR",
                "column": ["lte_sinr_1", "lte_sinr_2", "lte_sinr_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "RSSI Rx[0]",
                "column": [
                    "lte_inst_rssi_rx0_1",
                    "lte_inst_rssi_rx0_2",
                    "lte_inst_rssi_rx0_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "RSSI Rx[1]",
                "column": [
                    "lte_inst_rssi_rx1_1",
                    "lte_inst_rssi_rx1_2",
                    "lte_inst_rssi_rx1_3",
                ],
                "table": "lte_cell_meas",
            },
            {
                "name": "RSSI",
                "column": ["lte_inst_rssi_1", "lte_inst_rssi_2", "lte_inst_rssi_3"],
                "table": "lte_cell_meas",
            },
            {
                "name": "BLER",
                "column": ["lte_bler_1", "lte_bler_2", "lte_bler_3"],
                "table": "lte_l1_dl_tp",
            },
            {
                "name": "CQI CW[0]",
                "column": ["lte_cqi_cw0_1", "lte_cqi_cw0_2", "lte_cqi_cw0_3"],
                "table": "lte_cqi",
            },
            {
                "name": "CQI CW[1]",
                "column": ["lte_cqi_cw1_1", "lte_cqi_cw1_2", "lte_cqi_cw1_3"],
                "table": "lte_cqi",
            },
            {"name": "Tx Power", "column": ["lte_tx_power"], "table": "lte_tx_power",},
            {
                "name": "PUCCH TxPower (dBm)",
                "column": ["lte_pucch_tx_power"],
                "table": "lte_pucch_tx_info",
            },
            {
                "name": "PUSCH TxPower (dBm)",
                "column": ["lte_pusch_tx_power"],
                "table": "lte_pusch_tx_info",
            },
            {
                "name": "TimingAdvance",
                "column": ["lte_ta"],
                "table": "lte_frame_timing",
            },
            {
                "name": "Transmission Mode (RRC-tm)",
                "column": ["lte_transmission_mode_l3"],
                "table": "lte_rrc_transmode_info",
            },
            {
                "name": "LTE RRC State",
                "column": ["lte_rrc_state"],
                "table": "lte_rrc_state",
            },
            {
                "name": "LTE EMM State",
                "column": ["lte_emm_state"],
                "table": "lte_emm_state",
            },
            {
                "name": "LTE EMM Substate",
                "column": ["lte_emm_substate"],
                "table": "lte_emm_state",
            },
            {
                "name": "Modem ServCellInfo",
                "column": [],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "Allowed Access",
                "column": ["lte_serv_cell_info_allowed_access"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "MCC",
                "column": ["lte_serv_cell_info_mcc"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "MNC",
                "column": ["lte_serv_cell_info_mnc"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "TAC",
                "column": ["lte_serv_cell_info_tac"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "Cell ID (ECI)",
                "column": ["lte_serv_cell_info_eci"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "eNodeB ID",
                "column": ["lte_serv_cell_info_enb_id"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "LCI",
                "column": ["lte_scc_derived_lci"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "PCI",
                "column": ["lte_serv_cell_info_pci"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "Derived SCC ECI",
                "column": ["lte_scc_derived_eci"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "Derived SCC eNodeB ID",
                "column": ["lte_scc_derived_enb_id"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "Derived SCC LCI",
                "column": ["lte_scc_derived_lci"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "DL EARFCN",
                "column": ["lte_serv_cell_info_dl_freq"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "UL EARFCN",
                "column": ["lte_serv_cell_info_ul_freq"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "DL Bandwidth (Mhz)",
                "column": ["lte_serv_cell_info_dl_bandwidth_mhz"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "UL Bandwidth (Mhz)",
                "column": ["lte_serv_cell_info_ul_bandwidth_mhz"],
                "table": "lte_serv_cell_info",
            },
            {
                "name": "SCC DL Bandwidth (Mhz)",
                "column": ["lte_scc_dl_bandwidth_1"],
                "table": "lte_serv_cell_info",
            },
            {"name": "SIB1 info:", "column": [], "table": "lte_serv_cell_info",},
            {"name": "sib1 MCC", "column": ["lte_sib1_mcc"], "table": "lte_sib1_info",},
            {"name": "sib1 MNC", "column": ["lte_sib1_mnc"], "table": "lte_sib1_info",},
            {"name": "sib1 TAC", "column": ["lte_sib1_tac"], "table": "lte_sib1_info",},
            {"name": "sib1 ECI", "column": ["lte_sib1_eci"], "table": "lte_sib1_info",},
            {
                "name": "sib1 eNBid",
                "column": ["lte_sib1_enb_id"],
                "table": "lte_sib1_info",
            },
            {
                "name": "sib1 LCI",
                "column": ["lte_sib1_local_cell_id"],
                "table": "lte_sib1_info",
            },
            {"name": "TDD Config:", "column": [], "table": "lte_sib1_info",},
            {
                "name": "SubframeAssignment",
                "column": ["lte_tdd_config_subframe_assignment"],
                "table": "lte_tdd_config",
            },
            {
                "name": "SpclSubframePattern",
                "column": ["lte_tdd_config_special_subframe_pattern"],
                "table": "lte_tdd_config",
            },
            {
                "name": "DedBearer QCI",
                "column": ["lte_ded_eps_bearer_qci"],
                "table": "activate_dedicated_eps_bearer_context_request_params",
            },
        ]

        return elementDictList

    def getRrcSibStates(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time"},
            {"name": "SIB1 MCC", "column": ["lte_sib1_mcc"], "table": "lte_sib1_info"},
            {"name": "SIB1 MNC", "column": ["lte_sib1_mnc"], "table": "lte_sib1_info"},
            {"name": "SIB1 TAC", "column": ["lte_sib1_tac"], "table": "lte_sib1_info"},
            {
                "name": "SIB1 ECI (Cell ID)",
                "column": ["lte_sib1_eci"],
                "table": "lte_sib1_info",
            },
            {
                "name": "SIB1 eNodeB ID",
                "column": ["lte_sib1_enb_id"],
                "table": "lte_sib1_info",
            },
            {
                "name": "SIB1 LCI",
                "column": ["lte_sib1_local_cell_id"],
                "table": "lte_sib1_info",
            },
            {
                "name": "Transmission Mode (RRC-tm)",
                "column": ["lte_transmission_mode_l3"],
                "table": "lte_rrc_transmode_info",
            },
            {
                "name": "RRC State",
                "column": ["lte_rrc_state"],
                "table": "lte_rrc_state",
            },
        ]
        return elementDictList

    def get_rrc_sib_states():
        with sqlite3.connect(gc.databasePath) as dbcon:
            return get_nr_radio_params_disp_df(dbcon, self.timeFilter)

    def getServingAndNeighbors(self):
        MAX_NEIGHBORS = 16
        elementDictList = [
            {
                "tableRow": 0,
                "tableCol": 0,
                "column": ["global_time"],
                "table": "global_time",
            },
            {"name": "Serving Cell:", "column": [], "table": "", "shiftRight": 1},
            {"name": "", "column": ["lte_earfcn_1"], "table": "lte_cell_meas",},
            {
                "tableRow": 1,
                "tableCol": 2,
                "column": ["lte_serv_cell_info_band"],
                "table": "lte_serv_cell_info",
            },
            {
                "tableRow": 1,
                "tableCol": 3,
                "column": ["lte_serv_cell_info_pci"],
                "table": "lte_serv_cell_info",
            },
            {
                "tableRow": 1,
                "tableCol": 4,
                "column": ["lte_inst_rsrp_1"],
                "table": "lte_cell_meas",
            },
            {
                "tableRow": 1,
                "tableCol": 5,
                "column": ["lte_inst_rsrq_1"],
                "table": "lte_cell_meas",
            },
            {"name": "Neightbor Cells:", "column": [], "table": "", "shiftRight": 1},
        ]

        for n in range(MAX_NEIGHBORS):
            i = n + 1
            neighborRow = [
                {
                    "name": "#%d" % i,
                    "column": [
                        "lte_neigh_earfcn_%d" % i,
                        "lte_neigh_band_%d" % i,
                        "lte_neigh_physical_cell_id_%d" % i,
                        "lte_neigh_rsrp_%d" % i,
                        "lte_neigh_rsrq_%d" % i,
                    ],
                    "table": "lte_neigh_meas",
                },
            ]
            elementDictList += neighborRow

        return elementDictList

    def getPucchPdschParameters(self):
        elementDictList = [
            {"name": "---- PUCCH ----", "column": [], "table": ""},
            {"name": "CQI CW 0", "column": ["lte_cqi_cw0_1"], "table": "lte_cqi"},
            {"name": "CQI CW 1", "column": ["lte_cqi_cw1_1"], "table": "lte_cqi"},
            {
                "name": "CQI N Sub-bands",
                "column": ["lte_cqi_n_subbands_1"],
                "table": "lte_cqi",
            },
            {
                "name": "Rank Indicator",
                "column": ["lte_rank_indication_1"],
                "table": "lte_cqi",
            },
            {"name": "---- PDSCH ----", "column": [], "table": ""},
            {
                "name": "PDSCH Serving Cell ID",
                "column": ["lte_pdsch_serving_cell_id_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH RNTI ID",
                "column": ["lte_pdsch_rnti_id_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH RNTI Type",
                "column": ["lte_pdsch_rnti_type_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Serving N Tx Antennas",
                "column": ["lte_pdsch_serving_n_tx_antennas_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Serving N Rx Antennas",
                "column": ["lte_pdsch_serving_n_rx_antennas_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Transmission Mode Current",
                "column": ["lte_pdsch_transmission_mode_current_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Spatial Rank",
                "column": ["lte_pdsch_spatial_rank_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Rb Allocation Slot 0",
                "column": ["lte_pdsch_rb_allocation_slot0_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Rb Allocation Slot 1",
                "column": ["lte_pdsch_rb_allocation_slot1_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH PMI Type",
                "column": ["lte_pdsch_pmi_type_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH PMI Index",
                "column": ["lte_pdsch_pmi_index_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Stream[0] Block Size",
                "column": ["lte_pdsch_stream0_transport_block_size_bits_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Stream[0] Modulation",
                "column": ["lte_pdsch_stream0_modulation_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Traffic To Pilot Ratio",
                "column": ["lte_pdsch_traffic_to_pilot_ratio_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Stream[1] Block Size",
                "column": ["lte_pdsch_stream1_transport_block_size_bits_1"],
                "table": "lte_pdsch_meas",
            },
            {
                "name": "PDSCH Stream[1] Modulation",
                "column": ["lte_pdsch_stream1_modulation_1"],
                "table": "lte_pdsch_meas",
            },
        ]
        return elementDictList

    def getRlc(self):

        dataList = []
        condition = ""
        maxBearers = 8

        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {
                "name": "DL TP(Mbps)",
                "column": ["lte_rlc_dl_tp_mbps"],
                "table": "lte_rlc_stats",
            },
            {
                "name": "DL TP(Kbps)",
                "column": ["lte_rlc_dl_tp"],
                "table": "lte_rlc_stats",
            },
            {
                "name": "N Bearers",
                "column": ["lte_rlc_n_bearers"],
                "table": "lte_rlc_stats",
            },
            {"name": "Mode", "column": [], "table": ""},
            {"tableRow": 4, "tableCol": 1, "name": "Type",},
            {"tableRow": 4, "tableCol": 2, "name": "RB-ID",},
            {"tableRow": 4, "tableCol": 3, "name": "Index",},
            {"tableRow": 4, "tableCol": 4, "name": "TP Mbps",},
        ]

        for bearer in range(0, maxBearers):
            bearerNo = bearer + 1
            bearerElement = [
                {
                    "name": "",
                    "column": ["lte_rlc_per_rb_dl_rb_mode_%d" % bearerNo],
                    "table": "lte_rlc_stats",
                    "shiftLeft": 1,
                },
                {
                    "tableRow": 5 + bearer,
                    "tableCol": 1,
                    "column": ["lte_rlc_per_rb_dl_rb_type_%d" % bearerNo],
                    "table": "lte_rlc_stats",
                },
                {
                    "tableRow": 5 + bearer,
                    "tableCol": 2,
                    "column": ["lte_rlc_per_rb_dl_rb_id_%d" % bearerNo],
                    "table": "lte_rlc_stats",
                },
                {
                    "tableRow": 5 + bearer,
                    "tableCol": 3,
                    "column": ["lte_rlc_per_rb_cfg_index_%d" % bearerNo],
                    "table": "lte_rlc_stats",
                },
                {
                    "tableRow": 5 + bearer,
                    "tableCol": 4,
                    "column": ["lte_rlc_per_rb_dl_tp_%d" % bearerNo],
                    "table": "lte_rlc_stats",
                },
            ]
            elementDictList += bearerElement

        return elementDictList

    def getVolte(self):
        elementDictList = [
            {"name": "Time", "column": ["global_time"], "table": "global_time",},
            {"name": "Codec:", "column": [], "table": "",},
            {
                "name": "AMR SpeechCodec-RX",
                "column": ["gsm_speechcodecrx"],
                "table": "vocoder_info",
            },
            {
                "name": "AMR SpeechCodec-TX",
                "column": ["gsm_speechcodectx"],
                "table": "vocoder_info",
            },
            {"name": "Delay interval avg:", "column": [], "table": "",},
            {
                "name": "Audio Packet delay (ms.)",
                "column": ["vocoder_amr_audio_packet_delay_avg"],
                "table": "vocoder_info",
            },
            {
                "name": "RTP Packet delay (ms.)",
                "column": ["lte_volte_rtp_pkt_delay_avg"],
                "table": "lte_volte_stats",
            },
            {"name": "RTCP SR Params:", "column": [], "table": "",},
            {
                "name": "RTCP Round trip time (ms.)",
                "column": ["lte_volte_rtp_round_trip_time"],
                "table": "lte_volte_stats",
            },
            {"name": "RTCP SR Params - Jitter DL:", "column": [], "table": "",},
            {
                "name": "RTCP SR Jitter DL (ts unit)",
                "column": ["lte_volte_rtp_jitter_dl"],
                "table": "lte_volte_stats",
            },
            {
                "name": "RTCP SR Jitter DL (ms.)",
                "column": ["lte_volte_rtp_jitter_dl_millis"],
                "table": "lte_volte_stats",
            },
            {"name": "RTCP SR Params - Jitter UL:", "column": [], "table": "",},
            {
                "name": "RTCP SR Jitter UL (ts unit)",
                "column": ["lte_volte_rtp_jitter_ul"],
                "table": "lte_volte_stats",
            },
            {
                "name": "RTCP SR Jitter UL (ms.)",
                "column": ["lte_volte_rtp_jitter_ul_millis"],
                "table": "lte_volte_stats",
            },
            {"name": "RTCP SR Params - Packet loss rate:", "column": [], "table": "",},
            {
                "name": "RTCP SR Packet loss DL (%)",
                "column": ["lte_volte_rtp_packet_loss_rate_dl"],
                "table": "lte_volte_stats",
            },
            {
                "name": "RTCP SR Packet loss UL (%)",
                "column": ["lte_volte_rtp_packet_loss_rate_ul"],
                "table": "lte_volte_stats",
            },
        ]
        return elementDictList

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


################################## df get functions


def get_lte_rrc_sib_states_df(dbcon, time_before):
    parameter_to_columns_list = [
        (
            [
                "Time",
                "SIB1 MCC",
                "SIB1 MNC",
                "SIB1 TAC",
                "SIB1 ECI (Cell ID)",
                "SIB1 eNodeB ID",
                "SIB1 LCI",
            ],
            [
                "time",
                "lte_sib1_mcc",
                "lte_sib1_mnc",
                "lte_sib1_tac",
                "lte_sib1_eci",
                "lte_sib1_enb_id",
                "lte_sib1_local_cell_id",
            ],
            "lte_sib1_info",
        ),
        (
            ["Time", "Transmission Mode (RRC-tm)"],
            ["time", "lte_transmission_mode_l3",],
            "lte_rrc_transmode_info",
        ),
        (["Time", "RRC State"], ["time", "lte_rrc_state",], "lte_rrc_state"),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=True,
        custom_lookback_dur_millis=24 * 3600,
    )


def get_lte_radio_params_disp_df(dbcon, time_before):
    n_param_args = 4
    parameter_to_columns_list = [
        ("Time", ["time"], "lte_cell_meas"),
        (  # these params below come together so query them all in one query
            ["Band", "EARFCN", "PCI", "RSRP", "RSRQ", "SINR", "RSSI"],
            list(map(lambda x: "lte_band_{}".format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_earfcn_{}".format(x + 1), range(n_param_args)))
            + list(
                map(
                    lambda x: "lte_physical_cell_id_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(map(lambda x: "lte_inst_rsrp_{}".format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_inst_rsrq_{}".format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_sinr_{}".format(x + 1), range(n_param_args)))
            + list(
                map(lambda x: "lte_inst_rssi_{}".format(x + 1), range(n_param_args))
            ),
            "lte_cell_meas",
        ),
        (["TxPower",], ["lte_tx_power",], "lte_tx_power"),
        (["PUSCH TxPower"], ["lte_pusch_tx_power",], "lte_pusch_tx_info"),
        (["PUCCH TxPower"], ["lte_pucch_tx_power",], "lte_pucch_tx_info"),
        (["TA"], ["lte_ta",], "lte_frame_timing"),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_lte_serv_and_neigh_disp_df(dbcon, time_before):
    df_list = []

    pcell_scell_col_prefix_sr = pd.Series(
        [
            "lte_earfcn_",
            "lte_physical_cell_id_",
            "lte_inst_rsrp_",
            "lte_inst_rsrq_",
            "lte_sinr_",
        ]
    )
    pcell_scell_col_prefix_renamed = ["EARFCN", "PCI", "RSRP", "RSRQ", "SINR"]
    parameter_to_columns_list = [
        ("Time", ["time"]),
        (
            ["PCell", "SCell1", "SCell2", "SCell3"],
            list(pcell_scell_col_prefix_sr + "1")
            + list(pcell_scell_col_prefix_sr + "2")
            + list(pcell_scell_col_prefix_sr + "3")
            + list(pcell_scell_col_prefix_sr + "4"),
            "lte_cell_meas",
        ),
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="lte_cell_meas",
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    # print("df.head():\n%s" % df.head())
    df.columns = ["CellGroup"] + pcell_scell_col_prefix_renamed
    # print("df.head():\n%s" % df.head())
    df_list.append(df)

    # neigh
    pcell_scell_col_prefix_sr = pd.Series(
        [
            "lte_neigh_earfcn_",
            "lte_neigh_physical_cell_id_",
            "lte_neigh_rsrp_",
            "lte_neigh_rsrq_",
        ]
    )
    pcell_scell_col_prefix_renamed = ["ARFCN", "PCI", "RSRP", "RSRQ"]
    parameter_to_columns_list = [
        (
            [
                "Neigh1",
                "Neigh2",
                "Neigh3",
                "Neigh4",
                "Neigh5",
                "Neigh6",
                "Neigh7",
                "Neigh8",
            ],
            list(pcell_scell_col_prefix_sr + "1")
            + list(pcell_scell_col_prefix_sr + "2")
            + list(pcell_scell_col_prefix_sr + "3")
            + list(pcell_scell_col_prefix_sr + "4")
            + list(pcell_scell_col_prefix_sr + "5")
            + list(pcell_scell_col_prefix_sr + "6")
            + list(pcell_scell_col_prefix_sr + "7")
            + list(pcell_scell_col_prefix_sr + "8"),
            "lte_neigh_meas",
        )
    ]
    df = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    # print("df.head():\n%s" % df.head())
    df.columns = ["CellGroup"] + pcell_scell_col_prefix_renamed
    # print("df.head():\n%s" % df.head())
    df_list.append(df)

    final_df = pd.concat(df_list, sort=False)
    return final_df


def get_lte_rlc_disp_df(dbcon, time_before):
    n_param_args = 4
    parameter_to_columns_list = [
        (
            ["Time", "DL TP(Mbps)", "DL TP(Kbps)", "N Bearers"],
            ["time", "lte_rlc_dl_tp_mbps", "lte_rlc_dl_tp", "lte_rlc_n_bearers"],
            "lte_rlc_stats",
        ),
        (  # these params below come together so query them all in one query
            ["Mode", "Type", "RB-ID", "Index", "TP Mbps",],
            list(
                map(
                    lambda x: "lte_rlc_per_rb_dl_rb_mode_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_rlc_per_rb_dl_rb_type_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_rlc_per_rb_dl_rb_id_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_rlc_per_rb_cfg_index_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_rlc_per_rb_dl_tp_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_rlc_stats",
        ),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=True,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_lte_pucch_pdsch_disp_df(dbcon, time_before):
    n_param_args = 4
    parameter_to_columns_list = [
        (
            [
                "---- PUCCH ----",
                "CQI CW 0",
                "CQI CW 1",
                "CQI N Sub-bands",
                "Rank Indicator",
            ],
            list(map(lambda x: '"" as unused_{}'.format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_cqi_cw0_{}".format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_cqi_cw1_{}".format(x + 1), range(n_param_args)))
            + list(
                map(
                    lambda x: "lte_cqi_n_subbands_{}".format(x + 1), range(n_param_args)
                )
            )
            + list(
                map(
                    lambda x: "lte_rank_indication_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_cqi",
        ),
        (
            [
                "---- PDSCH ----",
                "PDSCH Serving Cell ID",
                "PDSCH RNTI ID",
                "PDSCH RNTI Type",
                "PDSCH Serving N Tx Antennas",
                "PDSCH Serving N Rx Antennas",
                "PDSCH Transmission Mode Current",
                "PDSCH Spatial Rank",
                "PDSCH Rb Allocation Slot 0",
                "PDSCH Rb Allocation Slot 1",
                "PDSCH PMI Type",
                "PDSCH PMI Index",
                "PDSCH Stream[0] Block Size",
                "PDSCH Stream[0] Modulation",
                "PDSCH Traffic To Pilot Ratio",
                "PDSCH Stream[1] Block Size",
                "PDSCH Stream[1] Modulation",
            ],
            list(map(lambda x: '"" as unused_{}'.format(x + 1), range(n_param_args)))
            + list(
                map(
                    lambda x: "lte_pdsch_serving_cell_id_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(lambda x: "lte_pdsch_rnti_id_{}".format(x + 1), range(n_param_args))
            )
            + list(
                map(
                    lambda x: "lte_pdsch_rnti_type_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_serving_n_tx_antennas_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_serving_n_rx_antennas_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_transmission_mode_current_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_spatial_rank_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_rb_allocation_slot0_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_rb_allocation_slot1_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_pmi_type_{}".format(x + 1), range(n_param_args)
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_pmi_index_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream0_transport_block_size_bits_{}".format(
                        x + 1
                    ),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream0_modulation_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_traffic_to_pilot_ratio_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream1_transport_block_size_bits_{}".format(
                        x + 1
                    ),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream1_modulation_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_volte_disp_df(dbcon, time_before):
    n_param_args = 4
    parameter_to_columns_list = [
        ("Time", ["time"], "lte_volte_stats"),
        (
            [
                "Codec:",
                "AMR SpeechCodec-RX",
                "AMR SpeechCodec-TX",
                "Delay interval avg:",
                "Audio Packet delay (ms.)",
            ],
            [
                '"" as unused0',
                "gsm_speechcodecrx",
                "gsm_speechcodectx",
                '"" as unused1',
                "vocoder_amr_audio_packet_delay_avg",
            ],
            "vocoder_info",
        ),
        (
            [
                "RTP Packet delay (ms.)",
                "RTCP SR Params:",
                "RTCP Round trip time (ms.)",
                "RTCP SR Params - Jitter DL:",
                "RTCP SR Jitter DL (ts unit)",
                "RTCP SR Jitter DL (ms.)",
                "RTCP SR Params - Jitter UL:",
                "RTCP SR Jitter UL (ts unit)",
                "RTCP SR Jitter UL (ms.)",
                "RTCP SR Params - Packet loss rate:",
                "RTCP SR Packet loss DL (%)",
                "RTCP SR Packet loss UL (%)",
            ],
            [
                "lte_volte_rtp_pkt_delay_avg",
                '"" as unused2',
                "lte_volte_rtp_round_trip_time",
                '"" as unused3',
                "lte_volte_rtp_jitter_dl",
                "lte_volte_rtp_jitter_dl_millis",
                '"" as unused4',
                "lte_volte_rtp_jitter_ul",
                "lte_volte_rtp_jitter_ul_millis",
                '"" as unused5',
                "lte_volte_rtp_packet_loss_rate_dl",
                "lte_volte_rtp_packet_loss_rate_ul",
            ],
            "lte_volte_stats",
        ),
    ]
    return params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )


def get_lte_data_disp_df(dbcon, time_before):
    n_param_args = 4
    df_list = []
    parameter_to_columns_list = [
        (["RRC State",], ["lte_rrc_state",], "lte_rrc_state"),
    ]
    df_rrc = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        default_table="lte_rrc_state",
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df_list.append(df_rrc)

    parameter_to_columns_list = [
        (
            ["L1 Combined (Mbps)", "L1 Combined (Kbps)",],
            [
                "lte_l1_dl_throughput_all_carriers_mbps",
                "lte_l1_dl_throughput_all_carriers",
            ],
            "lte_l1_dl_tp",
        ),
        (
            ["L1 Combined (Mbps)", "L1 Combined (Kbps)",],
            [
                "lte_l1_ul_throughput_all_carriers_mbps_1",
                "lte_l1_ul_throughput_all_carriers_1",
            ],
            "lte_l1_ul_tp",
        ),
    ]
    df_tp = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )

    df_t = pd.DataFrame(columns=["param", 1, 2])
    df_t.loc[0] = ["Throughput", "DL", "UL"]
    df_t.loc[1] = ["L1 Combined (Mbps)", df_tp.iloc[0, 1], df_tp.iloc[2, 1]]
    df_t.loc[2] = ["L1 Combined (kbps)", df_tp.iloc[1, 1], df_tp.iloc[3, 1]]
    df_list.append(df_t)

    parameter_to_columns_list = [
        (
            ["PDCP (Mbps)", "PDCP (kbps)",],
            [
                "lte_pdcp_dl_throughput_mbps",
                "lte_pdcp_ul_throughput_mbps",
                "lte_pdcp_dl_throughput",
                "lte_pdcp_ul_throughput",
            ],
            "lte_pdcp_stats",
        ),
        (
            ["RLC (Mbps)", "RLC (kbps)",],
            [
                "lte_rlc_dl_tp_mbps",
                "lte_rlc_ul_tp_mbps",
                "lte_rlc_dl_tp",
                "lte_rlc_ul_tp",
            ],
            "lte_rlc_stats",
        ),
        (["MAC (Kbps)",], ["lte_mac_dl_tp", "lte_mac_ul_tp",], "lte_mac_ul_tx_stat"),
    ]
    df_pdcp = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df_list.append(df_pdcp)

    parameter_to_columns_list = [
        (
            ["TransMode RRC tm",],
            ["lte_transmission_mode_l3",],
            "lte_rrc_transmode_info",
        ),
    ]
    df_tran = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df_list.append(df_tran)

    df_cell = pd.DataFrame(columns=["param", 1, 2, 3, 4])
    df_cell.loc[1] = ["", "PCC", "SCC0", "SCC1", "SCC2"]
    df_list.append(df_cell)

    parameter_to_columns_list = [
        (
            ["L1 DL TP (Mbps)",],
            list(
                map(
                    lambda x: "lte_l1_throughput_mbps_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_l1_dl_tp",
        ),
        (
            ["L1 UL TP (Mbps)",],
            list(
                map(
                    lambda x: "lte_l1_ul_throughput_mbps_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_l1_ul_tp",
        ),
        (
            ["TransMode Cur",],
            list(
                map(
                    lambda x: "lte_pdsch_transmission_mode_current_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
        (
            ["EARFCN",],
            list(map(lambda x: "lte_earfcn_{}".format(x + 1), range(n_param_args))),
            "lte_cell_meas",
        ),
        (
            ["PCI",],
            list(
                map(
                    lambda x: "lte_pdsch_serving_cell_id_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
        (
            [
                "PUSCH Stats:",
                "PRB Alloc UL",
                "MCS Index UL",
                "Modulation UL",
                "L1 UL Bler",
            ],
            list(map(lambda x: '"" as unused_{}'.format(x + 1), range(n_param_args)))
            + list(
                map(lambda x: "lte_l1_ul_n_rbs_{}".format(x + 1), range(n_param_args))
            )
            + list(
                map(lambda x: "lte_ul_mcs_index_{}".format(x + 1), range(n_param_args))
            )
            + list(
                map(
                    lambda x: "lte_pusch_modulation_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(lambda x: "lte_l1_ul_bler_{}".format(x + 1), range(n_param_args))
            ),
            "lte_l1_ul_tp",
        ),
        (
            ["DCI",],
            list(map(lambda x: "lte_pdcch_dci_{}".format(x + 1), range(n_param_args))),
            "lte_pdcch_dec_result",
        ),
        (
            ["PDSCH Stats:", "BLER",],
            list(map(lambda x: '"" as unused_{}'.format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_bler_{}".format(x + 1), range(n_param_args))),
            "lte_l1_dl_tp",
        ),
        (
            ["Serv N Tx Ant", "Serv N Tx Ant", "Spatial Rank"],
            list(
                map(
                    lambda x: "lte_pdsch_serving_n_tx_antennas_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_serving_n_rx_antennas_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_spatial_rank_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
        (
            ["Rank Ind", "CQI CW0", "CQI CW1"],
            list(
                map(
                    lambda x: "lte_rank_indication_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(map(lambda x: "lte_cqi_cw0_{}".format(x + 1), range(n_param_args)))
            + list(map(lambda x: "lte_cqi_cw1_{}".format(x + 1), range(n_param_args))),
            "lte_cqi",
        ),
        (
            ["PRB Alloc"],
            list(
                map(
                    lambda x: "lte_pdsch_n_rb_allocated_latest_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
        (
            ["PRB Ma"],
            list(
                map(lambda x: "lte_mib_max_n_rb_{}".format(x + 1), range(n_param_args))
            ),
            "lte_mib_info",
        ),
        (
            ["PRB Util (alloc/bw) %"],
            list(
                map(
                    lambda x: "lte_prb_alloc_in_bandwidth_percent_latest_{}".format(
                        x + 1
                    ),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
        (
            ["DL Bandwidth (MHz)"],
            list(
                map(
                    lambda x: "lte_mib_dl_bandwidth_mhz_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_mib_info",
        ),
        (["PCC UL Bw (Mhz)"], ["lte_sib2_ul_bandwidth_mhz"], "lte_sib2_info"),
        (
            ["Time Scheduled %", "MCS Index"],
            list(
                map(
                    lambda x: "lte_pdsch_sched_percent_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(lambda x: "lte_mcs_index_{}".format(x + 1), range(n_param_args))
            ),
            "lte_l1_dl_tp",
        ),
        (
            [
                "BlockSizeBits[0]",
                "Modulation[0]",
                "BlockSizeBits[1]",
                "Modulation[1]",
                "TrafficToPilot Ratio",
                "RNTI Type",
                "RNTI ID",
                "PMI Type",
                "PMI Index",
            ],
            list(
                map(
                    lambda x: "lte_pdsch_stream0_transport_block_size_bits_{}".format(
                        x + 1
                    ),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream0_modulation_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream1_transport_block_size_bits_{}".format(
                        x + 1
                    ),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_stream1_modulation_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_traffic_to_pilot_ratio_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_rnti_type_{}".format(x + 1),
                    range(n_param_args),
                )
            )
            + list(
                map(lambda x: "lte_pdsch_rnti_id_{}".format(x + 1), range(n_param_args))
            )
            + list(
                map(
                    lambda x: "lte_pdsch_pmi_type_{}".format(x + 1), range(n_param_args)
                )
            )
            + list(
                map(
                    lambda x: "lte_pdsch_pmi_index_{}".format(x + 1),
                    range(n_param_args),
                )
            ),
            "lte_pdsch_meas",
        ),
    ]
    df_tran = params_disp_df.get(
        dbcon,
        parameter_to_columns_list,
        time_before,
        not_null_first_col=False,
        custom_lookback_dur_millis=gc.DEFAULT_LOOKBACK_DUR_MILLIS,
    )
    df_list.append(df_tran)

    final_df = pd.concat(df_list, sort=False)
    return final_df
