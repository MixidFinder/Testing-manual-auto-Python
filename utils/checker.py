class Checker:
    @staticmethod
    def check_status_code(code_response: int, expected_status_code: int):
        assert code_response == expected_status_code

    @staticmethod
    def check_response(result_response: dict, expected_value: dict):
        assert result_response == expected_value
