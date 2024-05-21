import requests

ENDPOINT = "https://jsonplaceholder.typicode.com"


class Typicode_api:
    """
    A class for working with the API
    """

    headers = {"Content-Type": "application/json; charset=UTF-8"}

    @staticmethod
    def call_endpoint():
        result_response = requests.get(ENDPOINT)
        return result_response

    @staticmethod
    def get_all_posts():
        result_response = requests.get(f"{ENDPOINT}/posts")
        return result_response

    @staticmethod
    def get_post(post_id: int):
        result_response = requests.get(f"{ENDPOINT}/posts/{post_id}")
        return result_response

    @staticmethod
    def create_new_post(post: dict):
        result_response = requests.post(
            f"{ENDPOINT}/posts", headers=Typicode_api.headers, json=post
        )
        return result_response

    @staticmethod
    def update_post(post: dict, post_id: int):
        result_response = requests.put(
            f"{ENDPOINT}/posts/{post_id}", headers=Typicode_api.headers, json=post
        )
        return result_response

    @staticmethod
    def patch_post(post: dict, post_id: int):
        result_response = requests.patch(
            f"{ENDPOINT}/posts/{post_id}", headers=Typicode_api.headers, json=post
        )
        return result_response

    @staticmethod
    def delete_post(post_id: int):
        result_response = requests.delete(f"{ENDPOINT}/posts/{post_id}")
        return result_response
