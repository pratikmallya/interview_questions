#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort, g
from score_parser import ScoreParser


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/bowling/score/<int:score_id>', methods=['GET', 'POST'])
def score(score_id):
    """add a score or return computed overall score"""

    if score_id not in g['all_scores']:
        abort(404)

    sp = g['all_scores'][score_id]

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
    if g['all_scores']:
        return jsonify(g['all_scores']), 200
    else:
        abort(404)


@app.route('/bowling/scores/<int:score_id>', methods=['GET'])
def scores(score_id):
    """return list of scores input"""
    if score_id in g['all_scores']:
        return jsonify({'scores': g['all_scores'][score_id].scores}), 200
    else:
        abort(404)

@app.route('/bowling/new', methods=['POST'])
def new_score():
    """create a new scorecard"""
    sp = ScoreParser()
    if 'all_scores' not in g:
        g['all_scores'] = {}
    g['all_scores'][id(sp)] = sp

    return jsonify({'score_id': id(sp)}), 201


@app.route('/bowling/delete/<int:score_id>', methods=['DELETE'])
def delete_scorecard(score_id):
    """delete the scorecard"""
    if score_id in g['all_scores']:
        del g['all_scores'][score_id]
        return jsonify({'result': True})
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
