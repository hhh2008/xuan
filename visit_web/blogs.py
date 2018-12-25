import requests
r = requests.get("http://www.cnblogs.com/yoyoketang/")
print(r.elapsed)
print(r.elapsed.total_seconds())