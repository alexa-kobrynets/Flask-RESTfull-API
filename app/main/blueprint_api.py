from flask import Blueprint, jsonify
from .collect import main_func, form_xml_report, form_xml_drivers
from flask import request, current_app
from flasgger import swag_from
import xml.etree.cElementTree as ET
from ..models import *

blueprint_api = Blueprint('blueprint_api', __name__, url_prefix='/api/v1/')


@blueprint_api.route('/report/', methods=['GET'])
@swag_from('report.yml')
def report():
    format = request.args.get('format')
    order = request.args.get('order')
    res = Racing.select().order_by(Racing.time.asc()) if order != 'desc' else Racing.select().order_by(Racing.time.desc())
    if format != 'xml':
        result = [[place, team.name, team.team, team.time] for place, team in enumerate(res, 1)]
        return jsonify(result)
    else:
        result = form_xml_report(res).getroot()
        return current_app.response_class(ET.tostring(result), mimetype='application/xml')



@blueprint_api.route('/report/drivers/', methods=['GET'])
def drivers():
    driver = request.args.get('driver')
    format = request.args.get('format')
    res_all = Racing.select(Racing.abbr, Racing.name, Racing.time).order_by(Racing.time)
    res_driver = [[place, line] for place, line in enumerate(res_all, 1) if line.abbr == driver]
    result = res_driver if driver else enumerate(res_all, 1)
    if format == 'xml':
        result = form_xml_report(result, driver).getroot()
        return current_app.response_class(ET.tostring(result), mimetype='application/xml')
    else:
        return jsonify([[place, team.abbr, team.name, team.time] for place, team in result])
