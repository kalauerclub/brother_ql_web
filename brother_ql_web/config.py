"""
This are the default settings. (DONT CHANGE THIS FILE)
Adjust your settings in 'instance/application.py'
"""

import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    LOG_LEVEL = logging.INFO

    SERVER_PORT = 8013
    SERVER_HOST = '0.0.0.0'

    PRINTER_MODEL = 'QL-800'
    PRINTER_PRINTER = 'usb://0x04f9:0x209b/000F1Z401759'

    LABEL_DEFAULT_ORIENTATION = 'standard'
    LABEL_DEFAULT_SIZE = 'd24'
    LABEL_DEFAULT_FONT_SIZE = 50
    LABEL_DEFAULT_QR_SIZE = 8
    LABEL_DEFAULT_LINE_SPACING = 120
    LABEL_DEFAULT_FONT_FAMILY = 'Arial'
    LABEL_DEFAULT_FONT_STYLE = 'Regular'
    LABEL_DEFAULT_IMAGE_MODE = 'grayscale'
    LABEL_DEFAULT_BW_THRESHOLD = 70

    FONT_FOLDER = ''
