from flask import Blueprint, request, jsonify
from flask_login import login_required
from helpers.DataReduction import FindPeaksAndValleys
from data.sql import dbcontext
from services import SessionService

sessionapis = Blueprint('sessionapis', __name__, url_prefix='/api')

@sessionapis.route('/values', methods=['GET', 'POST'])
@login_required
def values():
    if request.method == 'GET':
        return jsonify({'status' : 'success GET'})
    else:
        return jsonify({'status' : 'success POST'})

@sessionapis.route('/timedata', methods=['POST'])
@login_required
def thermals():
    form = request.form
    session_thermals = dbcontext.get_session_data(form['sess_id'])
    session_thermals = FindPeaksAndValleys(session_thermals, 'data', 'time', int(form['num_points']))
    return jsonify({'session_id' : form['sess_id'],
                        'time_stamps' : session_thermals['time'].values.tolist(),
                        'temps' : session_thermals['data'].values.tolist() })

@sessionapis.route('/saveannotation', methods=['POST'])
@login_required
def save_annotation():
    sess_id = request.json['sess_id']
    annotations = request.json['annotations']
    result = SessionService.save_session_annotations(sess_id, annotations)
    return jsonify({'status' : result})

@sessionapis.route('/uniquesessions', methods=['GET'])
def get_unique_sessions():
    session_names = dbcontext.get_session_names()
    return jsonify(session_names)