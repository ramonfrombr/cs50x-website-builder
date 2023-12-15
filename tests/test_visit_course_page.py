def test_homepage(client):
    response = client.get("/2023/")
    assert "CS50x" in response.get_data(as_text=True)

def test_visit_python_course_homepage(client):
    response = client.get("/python/")
    assert "Python" in response.get_data(as_text=True)

def test_visit_web_course_homepage(client):
    response = client.get("/web/")
    assert "Web" in response.get_data(as_text=True)
    assert "Python" in response.get_data(as_text=True)
    assert "JavaScript" in response.get_data(as_text=True)

def test_visit_ai_course_homepage(client):
    response = client.get("/ai/")
    assert "Python" in response.get_data(as_text=True)