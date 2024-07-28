def test_syllabus(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['syllabus']}.html")
    assert "How Computers Work" in response.get_data(as_text=True)
    assert "Programming in C" in response.get_data(as_text=True)
