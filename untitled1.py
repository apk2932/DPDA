# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:26:35 2019

@author: prc1424
"""

from waitress import serve
import API as app1
serve(app1.app, host='0.0.0.0', port=5000,url_scheme ='https',threads=100,channel_timeout=600)
