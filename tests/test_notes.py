def test_notes0(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/0.html")
    assert '4 2 1' in response.get_data(as_text=True)
    assert '128514' in response.get_data(as_text=True)


def test_notes1(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/1.html")
    assert '2/3' in response.get_data(as_text=True)
    assert 'MIT' in response.get_data(as_text=True)
    assert '$ clang -o' in response.get_data(as_text=True)
    assert '%li' in response.get_data(as_text=True)


def test_notes2(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/2.html")
    assert 'movabsq' in response.get_data(as_text=True)
    assert 'check50 cs50/problems/hello' in response.get_data(as_text=True)


def test_notes3(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/3.html")
    assert 'RAM' in response.get_data(as_text=True)
    assert 'Ω' in response.get_data(as_text=True)


def test_notes4(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/4.html")
    assert 'FF0000' in response.get_data(as_text=True)
    assert './jpeg' in response.get_data(as_text=True)


def test_notes5(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/5.html")
    assert '*x = 42;' in response.get_data(as_text=True)


def test_notes6(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/6.html")
    assert 'print("' in response.get_data(as_text=True)
    assert 'qr.py' in response.get_data(as_text=True)


def test_notes7(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/7.html")
    assert 'IMDb' in response.get_data(as_text=True)
    assert 'PRIMARY KEY' in response.get_data(as_text=True)


def test_notes8(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/8.html")
    assert 'HTTPS' in response.get_data(as_text=True)
    assert 'DNS' in response.get_data(as_text=True)
    assert 'getCurrentPosition' in response.get_data(as_text=True)


def test_notes9(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/9.html")
    assert 'http-server' in response.get_data(as_text=True)
    assert 'AJAX' in response.get_data(as_text=True)


def test_notes10(client):
    response = client.get(
        f"/2024/{client.application.config['PAGES_URLS']['notes']}/10.html")
    assert 'OpenAI' in response.get_data(as_text=True)
