import unittest
from test_users import appi

class TestUsers(unittest.TestCase):
    """
        Abaixo são os testes do CRUD de Users.

    """

    def setUp(self):
        self.client = appi.test_client()

    def test_get_user_pelo_nome_retorna_status_200(self):
        response = self.client.get('/users/alex')
        self.assertEqual(200, response.status_code)

    