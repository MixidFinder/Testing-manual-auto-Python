import pytest

from utils.typicode_api import Typicode_api
from utils.checker import Checker


class Test_typicode_api:
    test_data_with_id = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }

    test_data_without_id = {
        "userId": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }

    def test_call_endpoint(self):
        code_response = Typicode_api.call_endpoint().status_code
        Checker.check_status_code(code_response, 200)

    def test_get_all_posts(self):
        code_response = Typicode_api.get_all_posts().status_code
        Checker.check_status_code(code_response, 200)

    @pytest.mark.parametrize(
        "post_id, post_data, expected_status_code",
        [
            (
                1,
                test_data_with_id,
                200,
            ),
            (-1, {}, 404),
        ],
    )
    def test_get_post(self, post_id, post_data, expected_status_code):
        result_response = Typicode_api.get_post(post_id)
        Checker.check_status_code(result_response.status_code, expected_status_code)
        Checker.check_response(result_response.json(), post_data)

    def test_post_post(self):
        result_response = Typicode_api.create_new_post(self.test_data_without_id)
        Checker.check_status_code(result_response.status_code, 201)
        result_response_data = {
            key: result_response.json()[key]
            for key in result_response.json()
            if key != "id"
        }
        Checker.check_response(result_response_data, self.test_data_without_id)

    def test_put_post(self):
        updated_post = {**self.test_data_with_id, "title": "updated title"}
        result_response = Typicode_api.update_post(
            updated_post, self.test_data_with_id["id"]
        )
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), updated_post)

    def test_put_post_negative(self):
        updated_post = {**self.test_data_with_id, "title": "updated title"}
        result_response = Typicode_api.update_post(updated_post, -1)
        Checker.check_status_code(result_response.status_code, 500)

    def test_patch_post(self):
        patched_post = {**self.test_data_with_id, "title": "patched title"}
        patched_value = {"title": "patched title"}
        result_response = Typicode_api.patch_post(
            patched_value, self.test_data_with_id["id"]
        )
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), patched_post)

    def test_delete_post(self):
        result_response = Typicode_api.delete_post(self.test_data_with_id["id"])
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), {})
