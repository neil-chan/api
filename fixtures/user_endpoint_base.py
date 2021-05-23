from fixtures.base import APIBaseClass


class UserEndpoint(APIBaseClass):
    """
    These fixtures are from this document
    https://docs.github.com/en/free-pro-team@latest/rest/reference/users#get-the-authenticated-user
    """

    # def __init__(self):
    #     super(UserEndpoint, self).__init__()

    def get_authenticated_user(self):
        uri = "/user"
        return self.get(uri)

    def update_authenticated_user(self, payload):
        uri = "/user"
        return self.put(uri, payload)

    def get_users_list(self):
        uri = "/users"
        return self.get(uri)

    def get_user(self, username):
        uri = "/users/" + username
        return self.get(uri)

    def get_user_hovercard(self, username):
        uri = "/users/%s/hovercard" % str(username)
        return self.get(uri)

    def get_blocked_users(self):
        uri = "/user/blocks"
        return self.get(uri)

    def is_user_blocked_by_auth_user(self, username):
        uri = "user/blocks/" + username
        res = self.get(uri)

        if res["status_code"] == 204:
            return True
        elif res["status_code"] == 404:
            return False

    def block_user(self, username):
        uri = "/user/blocks" + username
        return self.put(uri)

    def unblock_user(self, username):
        uri = "/user/blocks" + username
        return self.delete(uri)
