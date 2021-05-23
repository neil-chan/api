import pytest

from fixtures.base import ResponseCode
from fixtures.user_endpoint_base import UserEndpoint
from settings import USERNAME


class TestUsers(UserEndpoint):
    """
    Test Cases for the different resources of users API
    """

    # def setup_method(self, method):
    #     super().setup_method(method)

    def teardown_method(self, method):
        if method.__name__ == "test_update_user":
            payload = {"name": "initial_name"}
            self.update_authenticated_user(payload)

    def test_authenticated_user(self):
        """
        Test that authenticated user is returning 200 and should return correct username.
        """
        response = self.get_authenticated_user()
        print(response)
        assert response["status_code"] == ResponseCode.OK_200, (
            "Response is not  200 successful %s" % response["text"]
        )
        assert response["text"]["login"] == USERNAME, (
            "Username is incorrect %s" % response["text"]
        )

    @pytest.mark.xfail
    def test_update_user(self):
        """
        Test authenticate user's information can be updated.
        """
        payload = {"name": "updated_name"}
        # user = self.token() ####if you want to have another users' token to initiate action
        # response = user.update_authenticated_user(payload)
        response = self.update_authenticated_user(payload)
        assert response["status_code"] == ResponseCode.OK_200, (
            "Update is not successful %s" % response["text"]
        )

        response = self.get_authenticated_user()
        assert response["text"]["name"] == "updated_name", (
            "Update User Information is not reflecting %s" % response["text"]
        )
