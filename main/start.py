from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
import main.fxns
import main.random_image

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

    return render_template('websocketpage/ws.html')


@bp.route("/randomimg", methods=("GET",))
def randomimg():

    fname = main.random_image.random_image()  # generate and save

    return render_template('randomimg/randimg.html', fname=fname)