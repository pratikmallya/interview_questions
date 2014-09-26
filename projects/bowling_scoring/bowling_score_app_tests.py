import unittest
import bowling
import json


class BowlingTests(unittest.TestCase):

    def setUp(self):
        self.app = bowling.app.test_client()

    def test_basic(self):
        rv = self.app.get('/bowling/score')
        print(rv.data)
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 0)
        rv = self.app.get('/bowling/scores')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], [])
        rv = self.app.post('/bowling/score', data=json.dumps({'score': 1}),
                           content_type='application/json')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], ['1'])
        rv = self.app.post('/bowling/score', data=json.dumps({'score': 2}),
                           content_type='application/json')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'],
                         ['1', '2'])
        rv = self.app.get('/bowling/score')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 3)
        inp = "X 7 / 7 2 9 / X X X 2 3 X 7 / 3".split()
        rv = self.app.post('/bowling/new')
        for token in inp:
            self.app.post('/bowling/score', data=json.dumps({'score': token}),
                           content_type='application/json')
        rv = self.app.get('/bowling/score')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 171)



if __name__ == "__main__":
    unittest.main()
