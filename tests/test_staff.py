def test_staff(client):
    response = client.get('/2024/staff.html')
    assert 'David J. Malan' in response.get_data(as_text=True)
    assert 'Doug Lloyd' in response.get_data(as_text=True)
