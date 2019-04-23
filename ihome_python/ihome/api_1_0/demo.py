# coding:utf-8

from . import api
from ihome import db, models

from flask import current_app

@api.route('/index')
def index():
    current_app.logger.error("error info")
    current_app.logger.warn("warn info")
    current_app.logger.info("info info")
    current_app.logger.debug("debug info")
    return 'index page'