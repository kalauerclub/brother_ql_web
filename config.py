"""
This are the default settings. (DONT CHANGE THIS FILE)
Adjust your settings in 'instance/application.py'
"""

import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    LOG_LEVEL = logging.WARNING

    SERVER_PORT = 8013
    SERVER_HOST = '0.0.0.0'

    PRINTER_MODEL = 'QL-700'
    PRINTER_PRINTER = 'file:///dev/usb/lp0'

    LABEL_DEFAULT_ORIENTATION = 'standard'
    LABEL_DEFAULT_SIZE = '62'
    LABEL_DEFAULT_FONT_SIZE = 100
    LABEL_DEFAULT_QR_SIZE = 10
    LABEL_DEFAULT_LINE_SPACING = 120
    LABEL_DEFAULT_FONT_FAMILY = 'DejaVu Serif'
    LABEL_DEFAULT_FONT_STYLE = 'Book'
    LABEL_DEFAULT_IMAGE_MODE = 'grayscale'
    LABEL_DEFAULT_BW_THRESHOLD = 70

    FONT_FOLDER = ''
