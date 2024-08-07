def test_faqs(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['faqs']}.html")
    assert '12' in response.get_data(as_text=True)
    assert 'CS50 AP' in response.get_data(as_text=True)
    assert 'edX' in response.get_data(as_text=True)
    assert '30' in response.get_data(as_text=True)
    assert '70%' in response.get_data(as_text=True)
    assert '7/8' in response.get_data(as_text=True)
    assert '0%' in response.get_data(as_text=True)
    assert 'LinkedIn' in response.get_data(as_text=True)
    assert 'cs50.dev/restart' in response.get_data(as_text=True)
