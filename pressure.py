#!/usr/bin/env python

import syslog
import weewx

from weewx.wxengine import StdService
from Adafruit_BME280 import *

class PressureService(StdService):
    def __init__(self, engine, config_dict):
        super(PressureService, self).__init__(engine, config_dict)
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.read_sensors)

    def read_sensors(self, event):
        sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        event.record['inTemp'] = float((degrees*9/5)+32)
        event.record['pressure'] = float(pascals * 0.00029530)
