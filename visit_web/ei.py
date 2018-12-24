import requests
r = requests.get("http://www.engineeringvillage.com/search/quick.url?acw=&utt=")
print(r.elapsed)
print(r.elapsed.total_seconds())