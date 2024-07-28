def test_homepage(client):
    response = client.get('/2024/')
    assert 'CS50x' in response.get_data(as_text=True)