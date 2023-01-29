from rest_framework.test import APITestCase
from rest_framework.views import status


class FriendViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/transactions/"

        cls.maxDiff = None

    def test_parse_CNAB_without_required_fields(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        with self.subTest():
            expected_status_code = status.HTTP_400_BAD_REQUEST
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST sem os campos obrigatórios "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {
            "date": ["This field is required."],
            "hour": ["This field is required."],
            "value": ["This field is required."],
            "type": ["This field is required."],
            "cpf": ["This field is required."],
            "credit_card": ["This field is required."],
            "owner_name": ["This field is required."],
            "store_name": ["This field is required."],
        }
        msg = "Verifique se a mensagem de campos inválidos está correta"
        self.assertDictEqual(expected_data, returned_data, msg)

    def test_parse_CNAB_success(self):
        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        response = self.client.post(self.BASE_URL, data=CNAB_DATA, format="json")

        with self.subTest():
            expected_status_code = status.HTTP_201_CREATED
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_keys = set(response.json().keys())
        expected_keys = {
            "id",
            "date",
            "hour",
            "value",
            "type",
            "cpf",
            "credit_card",
            "owner_name",
            "store_name",
        }
        msg = "Verifique se o body está sendo retornado corretamente"
        self.assertSetEqual(expected_keys, returned_keys, msg)

    def test_list_all_CNAB_parsed_success(self):
        response_with_no_CNAB = self.client.get(self.BASE_URL)

        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response_with_no_CNAB.status_code
            msg = (
                "Verifique se o status code retornado do GET "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data_with_no_CNAB: dict = response_with_no_CNAB.json()
        msg = "Verifique se está sendo retornado uma lista vazia corretamente"
        self.assertEqual(len(returned_data_with_no_CNAB), 0, msg)

        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        self.client.post(self.BASE_URL, data=CNAB_DATA, format="json")

        response = self.client.get(self.BASE_URL)

        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do GET "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        msg = "Verifique se os CNAB's já parseados estão retornando corretamente"
        self.assertEqual(len(returned_data), 1, msg)

    def test_list_especific_CNAB_parsed_with_invalid_id(self):
        response = self.client.get(f"{self.BASE_URL}100/")

        with self.subTest():
            expected_status_code = status.HTTP_404_NOT_FOUND
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do GET com id inválido "
                + f"em `{self.BASE_URL}100/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {"detail": "Not found."}
        msg = "Verifique se a mensagem de não encontrado está correta"
        self.assertDictEqual(expected_data, returned_data, msg)

    def test_list_especific_CNAB_parsed_success(self):
        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        CNAB = self.client.post(self.BASE_URL, data=CNAB_DATA, format="json").json()

        response = self.client.get(f"{self.BASE_URL}{CNAB['id']}/")

        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do GET "
                + f"em `{self.BASE_URL}{CNAB['id']}/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_keys = set(response.json().keys())
        expected_keys = {
            "id",
            "date",
            "hour",
            "value",
            "type",
            "cpf",
            "credit_card",
            "owner_name",
            "store_name",
        }
        msg = "Verifique se o body está sendo retornado corretamente"
        self.assertSetEqual(expected_keys, returned_keys, msg)

    def test_partial_update_CNAB_with_invalid_id(self):
        response = self.client.patch(f"{self.BASE_URL}100/", data={}, format="json")

        with self.subTest():
            expected_status_code = status.HTTP_404_NOT_FOUND
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PATCH com id inválido "
                + f"em `{self.BASE_URL}100/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {"detail": "Not found."}
        msg = "Verifique se a mensagem de não encontrado está correta"
        self.assertDictEqual(expected_data, returned_data, msg)

    def test_partial_update_CNAB_success(self):
        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        CNAB = self.client.post(self.BASE_URL, data=CNAB_DATA, format="json").json()

        CNAB_UPDATE_DATA = {
            "owner_name": "KENZINHO",
            "store_name": "BAR DO KENZINHO",
        }

        response = self.client.patch(
            f"{self.BASE_URL}{CNAB['id']}/", data=CNAB_UPDATE_DATA, format="json"
        )

        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PATCH "
                + f"em `{self.BASE_URL}{CNAB['id']}/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        msg = "Verifique se a atualização foi feita corretamente"
        self.assertDictContainsSubset(CNAB_UPDATE_DATA, returned_data, msg)

    def test_full_update_CNAB_with_invalid_id(self):
        response = self.client.put(f"{self.BASE_URL}100/", data={}, format="json")

        with self.subTest():
            expected_status_code = status.HTTP_404_NOT_FOUND
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PUT com id inválido "
                + f"em `{self.BASE_URL}100/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {"detail": "Not found."}
        msg = "Verifique se a mensagem de não encontrado está correta"
        self.assertDictEqual(expected_data, returned_data, msg)

    def test_full_update_CNAB_success(self):
        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        CNAB = self.client.post(self.BASE_URL, data=CNAB_DATA, format="json").json()

        CNAB_UPDATE_DATA = {
            "type": "5",
            "date": "20220103",
            "value": "0000013200",
            "cpf": "55641815063",
            "credit_card": "3123****7687",
            "hour": "145607",
            "owner_name": "KENZINHO",
            "store_name": "BAR DO KENZINHO",
        }

        response = self.client.put(
            f"{self.BASE_URL}{CNAB['id']}/", data=CNAB_UPDATE_DATA, format="json"
        )

        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PUT "
                + f"em `{self.BASE_URL}{CNAB['id']}/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {
            "date": "2022-01-03",
            "hour": "14:56:07",
            "value": "132.0",
            "type": "Recebimento Empréstimo",
            "cpf": "55641815063",
            "credit_card": "3123****7687",
            "owner_name": "KENZINHO",
            "store_name": "BAR DO KENZINHO",
        }
        msg = "Verifique se a atualização foi feita corretamente"
        self.assertDictContainsSubset(expected_data, returned_data, msg)

    def test_delete_with_invalid_id(self):
        response = self.client.delete(f"{self.BASE_URL}100/")

        with self.subTest():
            expected_status_code = status.HTTP_404_NOT_FOUND
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do DELETE com id inválido "
                + f"em `{self.BASE_URL}100/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_data = {"detail": "Not found."}
        msg = "Verifique se a mensagem de não encontrado está correta"
        self.assertDictEqual(expected_data, returned_data, msg)

    def test_delete_success(self):
        CNAB_LIST: list = self.client.get(self.BASE_URL).json()
        msg = "Verifique se o GET está funcionando corretamente"
        self.assertEqual(len(CNAB_LIST), 0, msg)

        CNAB_DATA = {
            "type": "3",
            "date": "20190301",
            "value": "0000014200",
            "cpf": "09620676017",
            "credit_card": "4753****3153",
            "hour": "153453",
            "owner_name": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }

        CNAB = self.client.post(self.BASE_URL, data=CNAB_DATA, format="json").json()

        CNAB_LIST: list = self.client.get(self.BASE_URL).json()
        msg = "Verifique se o POST está funcionando corretamente"
        self.assertEqual(len(CNAB_LIST), 1, msg)

        response = self.client.delete(f"{self.BASE_URL}{CNAB['id']}/")

        with self.subTest():
            expected_status_code = status.HTTP_204_NO_CONTENT
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do DELETE "
                + f"em `{self.BASE_URL}{CNAB['id']}/` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        CNAB_LIST: list = self.client.get(self.BASE_URL).json()
        msg = "Verifique se a deleção foi feita corretamente"
        self.assertEqual(len(CNAB_LIST), 0, msg)
