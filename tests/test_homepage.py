def test_homepage(client):
    response = client.get('/2024/')
    assert client.application.config['TITLE'] in response.get_data(as_text=True)
    assert client.application.config['BACKGROUND_COLOR'] in response.get_data(as_text=True)