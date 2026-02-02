import json
from src.utils import JSONFileWorker
from unittest.mock import patch

def test_get_data(fileworker):
    result = fileworker.get_data()
    assert result == [
        {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com"
        }
    ]

@patch.object(JSONFileWorker, "get_data")
def test_save_data(mock_get_data, fileworker):
    fileworker.filename = "tests/test_file_2.json"
    new_data = [
        {"url": 5}, {"url": 2},
        {"url": 6}, {"url": 7}
    ]
    mock_get_data.return_value = [
        {"url": 1}, {"url": 2},
        {"url": 3}, {"url": 4}
    ]
    fileworker.save_data(new_data)

    with open("tests/test_file_2.json", "r") as f:
        result = json.load(f)
        assert result == [
            {"url": 1}, {"url": 2},
            {"url": 3}, {"url": 4},
            {"url": 5}, {"url": 6}, 
            {"url": 7}
        ]

