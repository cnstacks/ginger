#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: ginger 
# Software: PyCharm
# Time    : 2018-10-05 00:22
# File    : ginger.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from app.app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)