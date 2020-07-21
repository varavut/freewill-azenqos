import os
from PyQt5.QtCore import *

maxColumns = 50
maxRows = 1000
schemaList = []
activeLayers = []
mostFeaturesLayer = None
azenqosDatabase = None
minTimeValue = None
maxTimeValue = None
fastForwardValue = 1
slowDownValue = 1
currentTimestamp = None
currentDateTimeString = None
recentDateTimeString = ""
clickedLatLon = {"lat": 0, "lon": 0}
sliderLength = 0
openedWindows = []
timeSlider = None
isSliderPlay = False
allLayers = []
tableList = []
h_list = []
linechartWindowname = [
    "GSM_GSM Line Chart",
    "WCDMA_Line Chart",
    "LTE_LTE Line Chart",
    "Data_GSM Data Line Chart",
    "Data_WCDMA Data Line Chart",
    "Data_LTE Data Line Chart",
    "Data_5G NR Data Line Chart",
]
threadpool = QThreadPool()
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
graduatedFeatures = {
    # 4G Section
    "lte_inst_rsrp_1": {
        "expression": "lte_inst_rsrp_1",
        "range": [
            {"from": -150, "to": -124, "color": "#C0C0C0"},
            {"from": -124, "to": -116, "color": "#FF00FF"},
            {"from": -116, "to": -110, "color": "#FFA500"},
            {"from": -110, "to": -100, "color": "#FFFF00"},
            {"from": -100, "to": -95, "color": "#00FF00"},
            {"from": -95, "to": -90, "color": "#008000"},
            {"from": -90, "to": -80, "color": "#00FFFF"},
            {"from": -80, "to": 0, "color": "#0000FF"},
        ],
    },
    "lte_inst_rsrq_1": {
        "expression": "lte_inst_rsrq_1",
        "range": [
            {"from": -20, "to": -14, "color": "#FF00FF"},
            {"from": -14, "to": -11, "color": "#FFA500"},
            {"from": -11, "to": -9, "color": "#FFFF00"},
            {"from": -9, "to": -6, "color": "#008000"},
            {"from": -6, "to": 0, "color": "#0000FF"},
        ],
    },
    "lte_sinr_1": {
        "expression": "lte_sinr_1",
        "range": [
            {"from": -50, "to": 0, "color": "#FF00FF"},
            {"from": 0, "to": 5, "color": "#FFA500"},
            {"from": 5, "to": 10, "color": "#FFFF00"},
            {"from": 10, "to": 15, "color": "#00FF00"},
            {"from": 15, "to": 20, "color": "#008000"},
            {"from": 20, "to": 50, "color": "#0000FF"},
        ],
    },
    "lte_physical_cell_id_1": {"expression": "lte_physical_cell_id_1", "range": []},
    "lte_cqi_cw0_1": {
        "expression": "lte_cqi_cw0_1",
        "range": [
            {"from": 0, "to": 6, "color": "#FF0000"},
            {"from": 6, "to": 10, "color": "#FFFF00"},
            {"from": 10, "to": 16, "color": "#0000FF"},
        ],
    },
    "lte_l1_dl_throughput_all_carriers": {
        "expression": "lte_l1_dl_throughput_all_carriers",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 5000, "color": "#FF00FF"},
            {"from": 5000, "to": 10000, "color": "#FFA500"},
            {"from": 10000, "to": 15000, "color": "#FFFF00"},
            {"from": 15000, "to": 20000, "color": "#00FF00"},
            {"from": 20000, "to": 30000, "color": "#008000"},
            {"from": 30000, "to": 42000, "color": "#00FFFF"},
            {"from": 42000, "to": 60000, "color": "#0000FF"},
            {"from": 60000, "to": 100000, "color": "#351C75"},
        ],
    },
    "lte_l1_ul_throughput_all_carriers_1": {
        "expression": "lte_l1_ul_throughput_all_carriers_1",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 56, "color": "#FF00FF"},
            {"from": 56, "to": 153, "color": "#800000"},
            {"from": 153, "to": 384, "color": "#FF0000"},
            {"from": 384, "to": 900, "color": "#FFA500"},
            {"from": 900, "to": 1600, "color": "#FFFF00"},
            {"from": 1600, "to": 3300, "color": "#00FF00"},
            {"from": 3300, "to": 4000, "color": "#008000"},
            {"from": 4000, "to": 6000, "color": "#00FFFF"},
            {"from": 6000, "to": 300000, "color": "#0000FF"},
        ],
    },
    # 3G Section
    "wcdma_aset_rscp_1": {
        "expression": "wcdma_aset_rscp_1",
        "range": [
            {"from": -150, "to": -103, "color": "#FF00FF"},
            {"from": -103, "to": -95, "color": "#FF0000"},
            {"from": -95, "to": -90, "color": "#FFA500"},
            {"from": -90, "to": -85, "color": "#FFFF00"},
            {"from": -85, "to": -80, "color": "#00FF00"},
            {"from": -80, "to": -75, "color": "#008000"},
            {"from": -75, "to": -65, "color": "#00FFFF"},
            {"from": -65, "to": 0, "color": "#0000FF"},
        ],
    },
    "wcdma_aset_ecio_1": {
        "expression": "wcdma_aset_ecio_1",
        "range": [
            {"from": -30, "to": -18, "color": "#FF00FF"},
            {"from": -18, "to": -16, "color": "#FF0000"},
            {"from": -16, "to": -14, "color": "#FFA500"},
            {"from": -14, "to": -12, "color": "#FFFF00"},
            {"from": -12, "to": -9, "color": "#00FF00"},
            {"from": -9, "to": -6, "color": "#008000"},
            {"from": -6, "to": 0, "color": "#0000FF"},
        ],
    },
    "wcdma_aset_sc_1": {"expression": "wcdma_aset_sc_1", "range": []},
    "wcdma_n_aset_cells": {
        "expression": "wcdma_n_aset_cells",
        "range": [
            {"from": 1, "to": 2, "color": "#0000FF"},
            {"from": 2, "to": 3, "color": "#FFFF00"},
            {"from": 3, "to": 4, "color": "#FF0000"},
        ],
    },
    "data_hsdpa_thoughput": {
        "expression": "data_hsdpa_thoughput",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 64, "color": "#FF00FF"},
            {"from": 64, "to": 128, "color": "#800000"},
            {"from": 128, "to": 384, "color": "#FF0000"},
            {"from": 384, "to": 900, "color": "#FFA500"},
            {"from": 900, "to": 1300, "color": "#FFFF00"},
            {"from": 1300, "to": 3000, "color": "#00FF00"},
            {"from": 3000, "to": 5500, "color": "#008000"},
            {"from": 5500, "to": 7000, "color": "#00FFFF"},
            {"from": 7000, "to": 42000, "color": "#0000FF"},
            {"from": 42000, "to": 100000, "color": "#351C75"},
        ],
    },
    "data_hsupa_total_e_dpdch_throughput": {
        "expression": "data_hsupa_total_e_dpdch_throughput",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 56, "color": "#FF00FF"},
            {"from": 56, "to": 153, "color": "#800000"},
            {"from": 153, "to": 384, "color": "#FF0000"},
            {"from": 384, "to": 900, "color": "#FFA500"},
            {"from": 900, "to": 1600, "color": "#FFFF00"},
            {"from": 1600, "to": 3300, "color": "#00FF00"},
            {"from": 3300, "to": 4000, "color": "#008000"},
            {"from": 4000, "to": 6000, "color": "#00FFFF"},
            {"from": 6000, "to": 100000, "color": "#0000FF"},
        ],
    },
    # 2G Section
    "gsm_rxlev_full_dbm": {
        "expression": "gsm_rxlev_full_dbm",
        "range": [
            {"from": -120, "to": -92, "color": "#FF0000"},
            {"from": -92, "to": -82, "color": "#FFFF00"},
            {"from": -82, "to": -74, "color": "#00FF00"},
            {"from": -74, "to": -65, "color": "#00FFFF"},
            {"from": -65, "to": 0, "color": "#0000FF"},
        ],
    },
    "gsm_rxlev_sub_dbm": {
        "expression": "gsm_rxlev_sub_dbm",
        "range": [
            {"from": -120, "to": -92, "color": "#FF0000"},
            {"from": -92, "to": -82, "color": "#FFFF00"},
            {"from": -82, "to": -74, "color": "#00FF00"},
            {"from": -74, "to": -65, "color": "#00FFFF"},
            {"from": -65, "to": 0, "color": "#0000FF"},
        ],
    },
    "gsm_rxqual_full": {
        "expression": "gsm_rxqual_full",
        "range": [
            {"from": 0, "to": 4, "color": "#0000FF"},
            {"from": 4, "to": 6, "color": "#FFFF00"},
            {"from": 6, "to": 10, "color": "#FF0000"},
        ],
    },
    "gsm_rxqual_sub": {
        "expression": "gsm_rxqual_sub",
        "range": [
            {"from": 0, "to": 4, "color": "#0000FF"},
            {"from": 4, "to": 6, "color": "#FFFF00"},
            {"from": 6, "to": 10, "color": "#FF0000"},
        ],
    },
    "gsm_coi_worst": {
        "expression": "gsm_coi_worst",
        "range": [
            {"from": 0, "to": 6, "color": "#FF0000"},
            {"from": 6, "to": 8, "color": "#FFFF00"},
            {"from": 8, "to": 10, "color": "#00FF00"},
            {"from": 10, "to": 12, "color": "#00FFFF"},
            {"from": 12, "to": 30, "color": "#0000FF"},
        ],
    },
    "gsm_arfcn_bcch": {"expression": "gsm_arfcn_bcch", "range": []},
    "data_gsm_rlc_dl_throughput": {
        "expression": "data_gsm_rlc_dl_throughput",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 32, "color": "#FF0000"},
            {"from": 32, "to": 128, "color": "#FFFF00"},
            {"from": 128, "to": 1000, "color": "#00FF00"},
        ],
    },
    "data_gsm_rlc_ul_throughput": {
        "expression": "data_gsm_rlc_ul_throughput",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 32, "color": "#FF0000"},
            {"from": 32, "to": 64, "color": "#FFFF00"},
            {"from": 64, "to": 1000, "color": "#00FF00"},
        ],
    },
    # Others
    "data_trafficstat_dl": {
        "expression": "data_trafficstat_dl",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 5000, "color": "#FF00FF"},
            {"from": 5000, "to": 10000, "color": "#FFA500"},
            {"from": 10000, "to": 15000, "color": "#FFFF00"},
            {"from": 15000, "to": 20000, "color": "#00FF00"},
            {"from": 20000, "to": 30000, "color": "#008000"},
            {"from": 30000, "to": 42000, "color": "#00FFFF"},
            {"from": 42000, "to": 60000, "color": "#0000FF"},
            {"from": 60000, "to": 100000, "color": "#351C75"},
        ],
    },
    "data_trafficstat_ul": {
        "expression": "data_trafficstat_ul",
        "range": [
            {"from": -1, "to": 0, "color": "#C0C0C0"},
            {"from": 0, "to": 56, "color": "#FF00FF"},
            {"from": 56, "to": 153, "color": "#800000"},
            {"from": 153, "to": 384, "color": "#FF0000"},
            {"from": 384, "to": 900, "color": "#FFA500"},
            {"from": 900, "to": 1600, "color": "#FFFF00"},
            {"from": 1600, "to": 3300, "color": "#00FF00"},
            {"from": 3300, "to": 4000, "color": "#008000"},
            {"from": 4000, "to": 6000, "color": "#00FFFF"},
            {"from": 6000, "to": 300000, "color": "#0000FF"},
        ],
    },
    "polqa_mos": {
        "expression": "polqa_mos",
        "range": [
            {"from": 0, "to": 1, "color": "#C0C0C0"},
            {"from": 1, "to": 2, "color": "#FF0000"},
            {"from": 2, "to": 3, "color": "#FFFF00"},
            {"from": 3, "to": 4, "color": "#00FF00"},
            {"from": 4, "to": 5, "color": "#0000FF"},
        ],
    },
}
