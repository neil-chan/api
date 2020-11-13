from endpoints.users_endpoint import UserEndpoint
from settings import USERNAME
import pytest


class TestUsers(UserEndpoint):
    """
        Test Cases for the different resources of users API
    """

    def setup_method(self, method):
        super().setup_method(method)
    
    def teardown_method(self, method):
        if method.__name__ == 'test_update_user':
            payload = {"name":"initial_name"}
            self.update_authenticated_user(payload)

    @pytest.mark.smoke
    def test_authenticated_user(self):
        """
            Test that authenticated user is returning 200 and should return correct username.
        """
        response = self.get_authenticated_user()
        assert response["status_code"] == 200, "Response is not  200 successful %s" response["text"]
        assert response["text"]['login'] == USERNAME, "Username is incorrect %s" response["text"]

    def test_update_user(self):
        """
            Test authenticate user's information can be updated.
        """
        payload = {"name":"updated_name"}
        response = self.update_authenticated_user(payload)
        assert response["status_code"] == 200, "Update is not successful %s" response["text"]

        response = self.get_authenticated_user()
        assert response["text"]['name'] = "updated_name", "Update User Information is not reflecting %s" response["text"]
        
