#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort, g
from score_parser import ScoreParser


app = Flask(__name__)
sp = ScoreParser()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/bowling/score', methods=['GET', 'POST'])
def score():
    """add a score or return computed overall score"""

    if request.method == 'GET':
            return jsonify({'score': sp.score}), 200
    elif request.method == 'POST':
        if not request.json or 'score' not in request.json:
            abort(400)
        sp.read(str(request.json['score']))
        return jsonify({'scores': sp.scores}), 201


@app.route('/bowling/scores', methods=['GET'])
def every_score():
    """return list of scores input"""
    return jsonify({'scores': sp.scores}), 200


@app.route('/bowling/new', methods=['POST'])
def new_score():
    """clear the scorecard"""
    sp.reset()
    return jsonify({sp.scores}), 201


if __name__ == "__main__":
    app.run(debug=True)
