# -*- coding: utf-8 -*-
"""
author : Minoru Akagi
begin  : 2015-09-16

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""
import os
from unittest import TestCase
from PyQt4.QtCore import QSize
from qgis.core import QgsRectangle

from Qgis2threejs.api import Exporter
from Qgis2threejs.pluginmanager import PluginManager
from utilities import dataPath, outputPath, loadProject


class TestPlugins(TestCase):

  def setUp(self):
    pass

  def test01_gsielevtile(self):
    """test exporting with GSI elevation tile plugin"""
    projectPath = dataPath("testproject1.qgs")
    mapSettings = loadProject(projectPath)

    # zoom
    mapSettings.setExtent(QgsRectangle(-51698, -75431, 21286, -20179))

    # output size
    width = 800
    height = width * mapSettings.extent().height() / mapSettings.extent().width()
    mapSettings.setOutputSize(QSize(width, height))

    exporter = Exporter(None, dataPath("gsielevtile.qto3settings"))
    exporter.settings.pluginManager = PluginManager(True)   # enables all plugins
    exporter.settings.setMapSettings(mapSettings)
    err = exporter.export(outputPath(os.path.join("testproject1", "gsielevtile.html")))
    assert err == Exporter.NO_ERROR, err

if __name__ == "__main__":
  import unittest
  unittest.main()
