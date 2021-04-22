from app import app

import unittest

class RestApiTest(unittest.TestCase):

    #test the get endpoint "/"
    def test_index_main(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the get endpoint "/music"
    def test_index_music(self):
        tester = app.test_client(self)
        response = tester.get('/music')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the post method endpoint "/music"

    # def test_index_music_post(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/music', json = {"artist": "test",
    #                                              "duration": 3,
    #                                              "genre": "pop",
    #                                              "name": "test"})
    #     status_code = response.status_code
    #     self.assertEqual(status_code, 200)

    # test the get method endpoint "/id/<id>"
    def test_index_music_id(self):
        tester = app.test_client(self)
        response = tester.get('/music/id/1')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the delete method endpoint "/id/<id>"

    # def test_index_music_id_delete(self):
    #     tester = app.test_client(self)
    #     response = tester.delete('/music/id/16')
    #     status_code = response.status_code
    #     self.assertEqual(status_code, 200)

    # test the get method endpoint "/names/<name>"
    def test_index_music_names(self):
        tester = app.test_client(self)
        response = tester.get('/music/names/lala')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the get method endpoint "/artists/<artist>"
    def test_index_music_artists(self):
        tester = app.test_client(self)
        response = tester.get('/music/artists/xuboyang')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the get method endpoint "/genres/<genre>"
    def test_index_music_genres(self):
        tester = app.test_client(self)
        response = tester.get('/music/artists/pop')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # test the get method endpoint "/duration/<duration>"
    def test_index_music_duration(self):
        tester = app.test_client(self)
        response = tester.get('/music/duration/3')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
        unittest.main()