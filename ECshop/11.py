import requests
import re
import jsonpath
url="http://172.16.1.204:8000/api/departments/"
a=requests.get(url)
print(a.json())
b=a.json()
re.findall("'master_name': ''")