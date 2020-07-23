from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

bp = Blueprint('lookup_page', __name__, url_prefix='')


@bp.route('/', methods=('GET', 'POST'))
def begin():

    return render_template('page1/page1.html')
