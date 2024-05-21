import pytest

from utils.checker import Checker
from utils.typicode_api import Typicode_api


class Test_typicode_api:
    """
    A class for testing the Typecode API.
    """

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
        """
        Tests the basic API call and checks the response status code.

        Checks that the response status code is 200 (OK).
        """
        code_response = Typicode_api.call_endpoint().status_code
        Checker.check_status_code(code_response, 200)

    def test_get_all_posts(self):
        """
        Tests the receipt of all posts and checks the status code of the response.

        Checks that the response status code is 200 (OK).
        """
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
    def test_get_post(self, post_id: int, post_data: dict, expected_status_code: int):
        """
        Parameterized test to get one post by ID and check the response.

        Args:
        post_id (int): ID of the post to receive.
        post_data (dict): The expected data of the post.
        expected_status_code (int): The expected status is the response code.

        Checks that the response status code matches the expected one, and that the response data matches the expected data.
        """
        result_response = Typicode_api.get_post(post_id)
        Checker.check_status_code(result_response.status_code, expected_status_code)
        Checker.check_response(result_response.json(), post_data)

    def test_post_post(self):
        """
        Tests the creation of a new post and verifies the correctness of the response.

        Uses data without ID (`test_data_without_id') to create a new post.
        Checks that the response status code is 201 (Created).
        Checks that the response data matches the sent data, excluding the 'id' field.
        """
        result_response = Typicode_api.create_new_post(self.test_data_without_id)
        Checker.check_status_code(result_response.status_code, 201)
        result_response_data = {
            key: result_response.json()[key]
            for key in result_response.json()
            if key != "id"
        }
        Checker.check_response(result_response_data, self.test_data_without_id)

    def test_post_post_negative(self):
        """
        Tests the negative scenario of creating a new post with incorrect data.

        Checks that the status code is 500 (Internal Server Error).
        """
        wrong_data = 1
        result_response = Typicode_api.create_new_post(wrong_data)
        Checker.check_status_code(result_response.status_code, 500)

    def test_put_post(self):
        """
        Tests the update of an existing post and verifies the correctness of the response.

        Checks that the response status code is 200 (OK).
        Checks that the response data matches the sent data.
        """
        updated_post = {**self.test_data_with_id, "title": "updated title"}
        result_response = Typicode_api.update_post(
            updated_post, self.test_data_with_id["id"]
        )
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), updated_post)

    def test_put_post_negative(self):
        """
        Tests the negative scenario of update of an existing post with incorrect id.

        Checks that the status code is 500 (Internal Server Error).
        """
        updated_post = {**self.test_data_with_id, "title": "updated title"}
        result_response = Typicode_api.update_post(updated_post, -1)
        Checker.check_status_code(result_response.status_code, 500)

    def test_patch_post(self):
        """
        Tests a partial update of an existing post and verifies the correctness of the response.

        Checks that the response status code is 200 (OK).
        Checks that the response data matches the sent data.
        """
        patched_post = {**self.test_data_with_id, "title": "patched title"}
        patched_value = {"title": "patched title"}
        result_response = Typicode_api.patch_post(
            patched_value, self.test_data_with_id["id"]
        )
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), patched_post)

    def test_patch_post_negative(self):
        """
        Tests the negative scenario of a partial update of an existing post with incorrect data.

        Checks that the status code is 500 (Internal Server Error).
        """
        wrong_data = 1
        result_response = Typicode_api.patch_post(wrong_data, -1)
        Checker.check_status_code(result_response.status_code, 500)

    def test_delete_post(self):
        """
        Tests the deletion of an existing post and verifies the correctness of the response.

        Checks that the response status code is 200 (OK).
        Checks that the response data matches the empty dict.
        """
        result_response = Typicode_api.delete_post(self.test_data_with_id["id"])
        Checker.check_status_code(result_response.status_code, 200)
        Checker.check_response(result_response.json(), {})
