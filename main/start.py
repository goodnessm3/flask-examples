from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
import main.fxns
from subprocess import run

bp = Blueprint('lookup_page', __name__, url_prefix='')


@bp.route('/', methods=('GET', 'POST'))
def begin():

    return render_template('page1/page1.html')


@bp.route('/ajax', methods=('GET',))
def ajax_example():

    return render_template('ajax/ajax.html')


@bp.route("/stringfunc/<astr>", methods=("GET",))
def do_string_func(astr):

    return main.fxns.string_func(astr)


@bp.route("/websockettest", methods=("GET",))
def websockettest():

    run(r'''websocketd\websocketd.exe --port=8080 py main\for_stdout.py''')

    return render_template('websocketpage/ws.html')