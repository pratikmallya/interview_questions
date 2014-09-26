import unittest
import bowling
import json


class BowlingTests(unittest.TestCase):

    def setUp(self):
        self.app = bowling.app.test_client()

    def test_basic(self):
        rv = self.app.post('/bowling/new')
        print(rv.data)
        id1 = json.loads(rv.data.decode('utf-8'))['score_id']
        rv = self.app.get('/bowling/score/{}'.format(id1))
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 0)
        rv = self.app.get('/bowling/scores/{}'.format(id1))
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], [])
        rv = self.app.post('/bowling/score/{}'.format(id1),
                            data=json.dumps({'score': 1}),
                            content_type='application/json')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], ['1'])
        rv = self.app.post('/bowling/score/{}'.format(id1),
                           data=json.dumps({'score': 2}),
                           content_type='application/json')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'],
                         ['1', '2'])
        rv = self.app.get('/bowling/score/{}'.format(id1))
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 3)


if __name__ == "__main__":
    unittest.main()
