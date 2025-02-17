import pytest
from main import APIClient


def test_fetch_random_users_success(mocker):
    """mocking api response to test successful fetch"""
    mock_response = {
        "results": [
            {"name": {"first": "John", "last": "Doe"}, "email": "johndoe@example.com", "location": {"country": "USA"}},
            {"name": {"first": "Jane", "last": "Smith"}, "email": "janesmith@example.com",
             "location": {"country": "Canada"}}
        ]
    }
    mocker.patch("requests.get", return_value=mocker.Mock(json=lambda: mock_response, status_code=200))

    api_client = APIClient()
    data = api_client.fetch_random_users(2)

    assert data is not None
    assert len(data["results"]) == 2
    assert data["results"][0]["name"]["first"] == "John"
    assert data["results"][1]["name"]["first"] == "Jane"


def test_fetch_random_users_failure(mocker):
    """mocking failed api fetch"""
    mocker.patch("requests.get",
                 return_value=mocker.Mock(raise_for_status=mocker.Mock(side_effect=Exception("API Error"))))

    api_client = APIClient()
    data = api_client.fetch_random_users(2)

    assert data is None
