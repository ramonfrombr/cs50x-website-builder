def test_honesty(client):
    response = client.get('/2024/honesty.html')
    assert 'certificates@cs50.harvard.edu' in response.get_data(as_text=True)
    assert 'cs50.ai' in response.get_data(as_text=True)
    assert 'ChatGPT' in response.get_data(as_text=True)
