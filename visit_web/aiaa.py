import requests
r = requests.get("https://arc.aiaa.org/")
print(r.elapsed)
print(r.elapsed.total_seconds())