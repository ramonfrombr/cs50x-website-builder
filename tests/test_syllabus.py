def test_syllabus(client):
    response = client.get('/2024/syllabus.html')
    assert "How Computers Work" in response.get_data(as_text=True)
    assert "Programming in C" in response.get_data(as_text=True)
