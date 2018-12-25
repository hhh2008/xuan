import requests
r = requests.get("http://www.webofknowledge.com/")
print(r.elapsed)
print(r.elapsed.total_seconds())