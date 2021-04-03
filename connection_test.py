import requests

data = '{"sender": "test_user", "message": "what is photosynthesis"}'
url = "http://206.189.104.159:5005/webhooks/rest/webhook"
response = requests.post(url, data)
print(response.content)
print(response.elapsed.total_seconds())