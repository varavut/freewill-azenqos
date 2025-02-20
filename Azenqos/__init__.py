# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Azenqos
                                 A QGIS plugin
 Azenqos Plugin
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-03-18
        copyright            : Copyright (C) 2019-2020 Freewill FX Co., Ltd. All rights reserved
        email                : gritmanoch@longdo.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Azenqos class from file Azenqos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .azenqos_plugin import Azenqos

    return Azenqos(iface)
