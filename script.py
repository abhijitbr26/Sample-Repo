import requests


r = requests.get("https://www.linkedin.com/in/abhijitbr/")
print(r.status_code)
print(r.ok)
