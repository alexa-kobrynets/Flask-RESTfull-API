from flask import Blueprint
from .collect import main_func
from flasgger import Swagger
from flask import render_template, request, current_app, make_response
from ..models import Racing

main = Blueprint('main', __name__)
swagger = Swagger(current_app)

@main.route('/report/')
def report():
    order = request.args.get('order')
    if order == 'desc':
        res = Racing.select().order_by(Racing.time.desc())
    else:
        res = Racing.select().order_by(Racing.time)
    return render_template('report.html', res=enumerate(res, 1), order=order)



@main.route('/report/drivers/')
def drivers():
    driver = request.args.get('driver')
    if driver:
        res = Racing.select().where(Racing.abbr == driver)
        return render_template('one_driver.html', res=res)
    else:
        res = Racing.select(Racing.abbr, Racing.name).order_by(Racing.time)
        return render_template('report_drivers.html', res=res)


@main.app_errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp
