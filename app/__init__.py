#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
# from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# manager = Manager(app)
bootstrap = Bootstrap(app)

import views
