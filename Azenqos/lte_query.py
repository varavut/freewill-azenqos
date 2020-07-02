from PyQt5.QtSql import QSqlQuery, QSqlDatabase


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
        self.openConnection()

        dataList = []
        condition = ""
        maxBearers = 8

        if self.timeFilter:
            condition = "WHERE time <= '%s'" % (self.timeFilter)
        dataList.append(["Time", self.timeFilter, "", "", ""])
        queryString = """SELECT time, lte_rlc_dl_tp_mbps, lte_rlc_dl_tp, lte_rlc_n_bearers
                        FROM lte_rlc_stats
                        %s
                        ORDER BY time DESC
                        LIMIT 1""" % (
            condition
        )
        query = QSqlQuery()
        query.exec_(queryString)
        if query.first():
            dataList.append(
                ["DL TP(Mbps)", query.value("lte_rlc_dl_tp_mbps") or "", "", "", ""]
            )
            dataList.append(
                ["DL TP(Kbps)", query.value("lte_rlc_dl_tp") or "", "", "", ""]
            )
            dataList.append(["Bearers:", "", "", "", ""])
            dataList.append(
                ["N Bearers", query.value("lte_rlc_n_bearers") or "", "", "", ""]
            )
        for bearer in range(1, maxBearers):
            bearerNo = bearer + 1
            queryString = """SELECT lte_rlc_per_rb_dl_rb_mode_%d, lte_rlc_per_rb_dl_rb_type_%d, lte_rlc_per_rb_dl_rb_id_%d, lte_rlc_per_rb_cfg_index_%d,
                            lte_rlc_per_rb_dl_tp_%d
                            FROM lte_rlc_stats
                            %s
                            ORDER BY time DESC
                            LIMIT 1""" % (
                bearerNo,
                bearerNo,
                bearerNo,
                bearerNo,
                bearerNo,
                condition,
            )
            query = QSqlQuery()
            query.exec_(queryString)
            while query.next():
                if bearerNo == 1:
                    dataList.append(["Mode", "Type", "RB-ID", "Index", "TP Mbps"])
                dataList.append(
                    [
                        query.value(0) or "",
                        query.value(1) or "",
                        query.value(2) or "",
                        query.value(3) or "",
                        query.value(4) or "",
                    ]
                )
        self.closeConnection()
        return dataList

    def getVolte(self):
        self.openConnection()
        dataList = []
        condition = ""
        volteFields = [
            "Time",
            "Codec:",
            "AMR SpeechCodec-RX",
            "AMR SpeechCodec-TX",
            "Delay interval avg:",
            "Audio Packet delay (ms.)",
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
        ]

        if self.timeFilter:
            condition = "WHERE lvs.time <= '%s'" % (self.timeFilter)

        queryString = """SELECT lvs.time, '' AS codec, vi.gsm_speechcodecrx, vi.gsm_speechcodectx, '' AS delay_interval,
                        vi.vocoder_amr_audio_packet_delay_avg, lvs.lte_volte_rtp_pkt_delay_avg, '' AS rtcp_sr_params,
                        lvs.lte_volte_rtp_round_trip_time, '' AS rtcp_jitter_dl, lvs.lte_volte_rtp_jitter_dl,
                        lvs.lte_volte_rtp_jitter_dl_millis, '' AS rtcp_jitter_ul, lte_volte_rtp_jitter_ul, lte_volte_rtp_jitter_ul_millis,
                        '' AS rtcp_sr_packet_loss, lte_volte_rtp_packet_loss_rate_dl, lte_volte_rtp_packet_loss_rate_ul
                        FROM lte_volte_stats AS lvs
                        LEFT JOIN vocoder_info vi ON lvs.time = vi.time
                        %s
                        ORDER BY lvs.time DESC
                        LIMIT 1""" % (
            condition
        )
        query = QSqlQuery()
        query.exec_(queryString)
        while query.next():
            for field in range(len(volteFields)):
                if field == 0:
                    dataList.append([volteFields[field], self.timeFilter])
                else:
                    if query.value(field):
                        dataList.append([volteFields[field], query.value(field)])
                    else:
                        dataList.append([volteFields[field], ""])
        if len(dataList) == 0:
            for field in range(len(volteFields)):
                if field == 0:
                    dataList.append([volteFields[field], self.timeFilter])
                else:
                    dataList.append([volteFields[field], ""])
        self.closeConnection()
        return dataList

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
