import unittest
import bowling
import json

class BowlingTests(unittest.TestCase):

    def setUp(self):
        self.app = bowling.app.test_client()

    def test_basic(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        rv = self.app.get('/')
        self.assertIn('Hello, World!', str(rv.data))
        rv = self.app.get('/bowling/score')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['score'], 0)
        rv = self.app.get('/bowling/scores')
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], [])
        rv = self.app.post('/bowling/score', data="{'score': 1}", headers=headers)
        print(rv.data)
        self.assertEqual(json.loads(rv.data.decode('utf-8'))['scores'], [1])

if __name__ == "__main__":
    unittest.main()