def test_honesty(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['honesty']}.html")
    assert 'certificates@cs50.harvard.edu' in response.get_data(as_text=True)
    assert 'cs50.ai' in response.get_data(as_text=True)
    assert 'ChatGPT' in response.get_data(as_text=True)
