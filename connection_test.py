import requests

data = '{"sender": "test_user1", "message": "whats good in high wind enviornment"}'
# data = '{"sender": "test_user1", "message": "tell me about low sun environment"}'
url = "http://206.189.104.159:5005/webhooks/rest/webhook"
response = requests.post(url, data)
print(response.content)
print(response.elapsed.total_seconds()) 