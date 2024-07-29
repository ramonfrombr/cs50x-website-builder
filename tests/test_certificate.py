def test_certificate(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['certificate']}.html")
    assert 'certificates@cs50.harvard.edu' in response.get_data(as_text=True)
    assert 'https://cs50.harvard.edu/certificates/20f627af-99e6-4f7b-ac0c-ce19076f2aac.png' in response.get_data(
        as_text=True)
