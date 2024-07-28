def test_staff(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['staff']}.html")
    assert 'David J. Malan' in response.get_data(as_text=True)
    assert 'Doug Lloyd' in response.get_data(as_text=True)
