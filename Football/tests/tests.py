from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from Football.tests.factories import SuperUserFactory


class FootballApiTest(APITestCase):
    def setUp(self):
        su = SuperUserFactory()
        self.client = APIClient()
        self.client.login(username=su.username, password='test')

    def test_post_team(self):
        postdata = dict(
            name='Arsenal FC',
            country='GB',
            year_founded='1961-01-01',
        )
        response = self.client.post('/api/v1/teams/', postdata, format='json')

        assert response.status_code == 201
        assert postdata['name'] == response.json()['name']

    # def test_get_team_by_country(self):
    #     response = self.client.get('/api/v1/teams/?country=GB')

    #     assert response.status_code == 200
    #     print(response.json())
    #     assert response.json()['name'] == 'Arsenal FC'
