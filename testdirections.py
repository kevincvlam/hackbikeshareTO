import requests, json
from directions import directions

obj = directions("633 Bay St, Toronto ON", "45 Ulster, Toronto ON",'walking');

print(obj)
