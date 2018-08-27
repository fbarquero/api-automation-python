import unittest
import json

from requests_verbs.request_verbs import RedisApiRequests


class FlaskServiceTests(unittest.TestCase):

    def setUp(self):
        self.s = RedisApiRequests()

    def test_healthcheck(self):
        # Arrange
        endpoint = '/v1.0/redis/healthcheck'

        # Act
        r = self.s.do_get(endpoint=endpoint)
        response_data = json.loads(r.content)
        status_code = r.status_code

        # Assert
        self.assertEqual(r.status_code, 200,
                         'Expected status code {e_status_code} '
                         'but instead {r_status_code}'.format(e_status_code=200, r_status_code=status_code))
        self.assertTrue(response_data['status'] == u'I\'m Healthy!!')

    def test_redis_write_400(self):
        # Arrange
        endpoint = '/v1.0/redis/entry/add_redis_entry'
        data = {'bad_request': '400'}

        # Act
        r = self.s.do_post(endpoint=endpoint, data=data)
        response_data = json.loads(r.content)
        status_code = r.status_code

        # Assert
        self.assertEqual(r.status_code, 400,
                         'Expected status code {e_status_code} '
                         'but instead {r_status_code}'.format(e_status_code=400, r_status_code=status_code))
        self.assertTrue(response_data['error'] == u'Bad Request')

    def test_redis_get_redis_entry_404(self):
        # Arrange
        endpoint = '/v1.0/redis/entry/tttttt'

        # Act
        r = self.s.do_get(endpoint=endpoint)
        response_data = json.loads(r.content)
        status_code = r.status_code

        # Assert
        self.assertEqual(r.status_code, 404,
                         'Expected status code {e_status_code} '
                         'but instead {r_status_code}'.format(e_status_code=404, r_status_code=status_code))
        self.assertTrue(response_data['error'] == u'Not found')

    def test_redis_post_redis_entry_201(self):
        # Arrange
        endpoint = '/v1.0/redis/entry/add_redis_entry'

        # Act
        data = {'redis_entry': {'key': 'test_entry', 'value': 'test_value'}}
        r = self.s.do_post(endpoint=endpoint, data=data)
        response_data = json.loads(r.content)
        status_code = r.status_code

        # Assert
        self.assertEqual(r.status_code, 201,
                         'Expected status code {e_status_code} '
                         'but instead {r_status_code}'.format(e_status_code=201, r_status_code=status_code))
        self.assertTrue(response_data['data'] is True)

    def test_redis_get_redis_entry_200(self):
        # Arrange
        endpoint_get = '/v1.0/redis/entry/test_entry2'
        endpoint_post = '/v1.0/redis/entry/add_redis_entry'
        # Act
        data = {'redis_entry': {'key': 'test_entry2', 'value': 'test_value'}}
        r = self.s.do_post(endpoint=endpoint_post, data=data)

        # Act
        r = self.s.do_get(endpoint=endpoint_get)
        response_data = json.loads(r.content)
        status_code = r.status_code

        # Assert
        self.assertEqual(r.status_code, 200,
                         'Expected status code {e_status_code} '
                         'but instead {r_status_code}'.format(e_status_code=200, r_status_code=status_code))
        self.assertTrue(response_data['data'] == u'test_value')
