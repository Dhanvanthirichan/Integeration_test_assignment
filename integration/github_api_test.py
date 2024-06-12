import pytest
import requests

class TestGithubApi:
    """
    Test cases for Github API
    """

    def setup_class(self):
        """
        Setup method for Github API
        """
        self.url = 'https://api.github.com/'
        self.bearer_token = '<input_bearer_token>'
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + self.bearer_token,
            "X-GitHub-Api-Version": "2022-11-28"
        }

    
    def test_get_repository_content(self):
        """
        Test case to get repository content
        """
        response = requests.get(
            self.url + 'repos/Dhanvanthirichan/Integeration_test_assignment/contents/README.md', headers=self.headers)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['name'] == 'README.md'
        assert response_body['type'] == 'file'
        assert response_body['encoding'] == 'base64'
        assert response_body['path'] == 'README.md'

    def test_delete_repository_file(self):
        """
        Test case to delete repository file
        """
        response = requests.delete(
            self.url + 'repos/Dhanvanthirichan/Integeration_test_assignment/contents/unknown_file',
            headers=self.headers,
            data='{"message":"have deleted the unknow file","committer":{"name":"DhanvanthiriChan","email":"dhan@github.com"},"sha":"329688480d39049927147c162b9d2deaf8850123"}'
        )
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['message'] == 'unknown_file deleted'
        assert response_body['commit']['message'] == 'have deleted the unknow file'
        assert response_body['commit']["sha"] == '329688480d39049927147c162b9d2deaf8850123'
        assert response_body['commit']['committer']['name'] == 'DhanvanthiriChan'
        assert response_body['commit']['committer']['email'] == 'dhan@github.com'

        assert response_body['commit']['verification']['verified'] == True
        assert response_body['commit']['verification']['reason'] == 'valid'

        #  can be used to verify passing test case
        # assert response.status_code == 422
        # assert response.reason == 'Unprocessable Entity'
        # assert response.json()[
        #     'documentation_url'] == 'https://docs.github.com/rest/repos/contents#delete-a-file'
