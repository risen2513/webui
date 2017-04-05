#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app, render_template, request, redirect


@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
        test1 = request.form['test1']
        test2 = request.form['test2']
        msg = 'test1 : %s \ntest2 : %s' % (test1, test2)
        return render_template('user.html', name='testform', msg=msg)

@app.route('/form')
def form():
        return render_template('form.html')
