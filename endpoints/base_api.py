from settings import token
import requests
import json

class APIBaseClass(object):

    def __init__(self):
        """
            Initialize API client with application under test's base url
        """
        self.base_url = "https://api.github.com"
        self.token = token
        self.header = {'content-type': 'application/json', 'Authorization': "token %s" % self.token}

    def set_token(self, token):
        """ 
            Setting a valid token for the API base requests
            :param token: <str> use as the authentication
        """
        if token is None or token == "":
            raise Exception("Token is empty or not provided")
        else:
            self.token = token

    def get(self, uri, param=None):
        """ 
            Perform https GET request for given uri, And use request header as per argument
            :param uri: <str> eg. "https://api.github.com/user"
            :param param: <dict> request parameters in dictionary
            :return: <dict> return response with keys "text" and "status_code"
        """
        if param and not isinstance(params, dict):
            raise Exception("'params' should be of dictionary")
        url = self.base_url + uri
        response = requests.get(url, params=param, headers=self.header)
        return {"text": json.loads(response.text), "status_code": response.status_code}

    def post(self, uri, payload):
        """ 
            Perform https POST request for given uri, pass payload data to request
            :param uri: <str> eg. "https://api.github.com/user"
            :param payload: <dict> payload dictionary
            :return: <dict> return response with keys "text" and "status_code"
        """
        url = self.base_url + uri
        response = requests.post(url, data=payload, headers=self.header)
        return {"text": json.loads(response.text), "status_code": response.status_code}

    def put(self, uri, payload=None):
        """
            Perform https PUT request for given uri, pass payload data to request
            :param uri: <str> eg. "https://api.github.com/user/1"
            :param payload: <dict> payload dictionary
            :return: <dict> return response with keys "text" and "status_code"
        """
        url = self.base_url + uri
        response = requests.put(url, data=payload, headers=self.header)
        return {"text": json.loads(response.text), "status_code": response.status_code}

    def patch(self, uri, payload=None):
        """
            Perform https PATCH request for given uri, pass payload data to request
            :param uri: <str> eg. "https://api.github.com/user/1"
            :param payload: <dict> payload dictionary
            :return: <dict> return response with keys "text" and "status_code"
        """
        url = self.base_url + uri
        response = requests.patch(url, data=payload, headers=self.header)
        return {"text": json.loads(response.text), "status_code": response.status_code}

    def delete(self, uri):
        """
            Perform https DELETE request for given uri
            :param uri: <str> eg. "https://api.github.com/user/1"
            :return: <dict> return response with keys "text" and "status_code"
        """
        url = self.base_url + uri
        response = requests.put(url, headers=self.header)
        return {"text": json.loads(response.text), "status_code": response.status_code}
