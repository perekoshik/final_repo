import requests
import json

def api_get_datelist():
    header = {'X-Auth-Token':'ppo_10_10096', }
    url = "https://olimp.miet.ru/ppo_it_final/date"
    response = requests.get(url, headers=header)
    resv_data = response.json()
    return resv_data #dict


def api_get_dateinfo(date): #date in format dd-mm-yy
    d, m, y = date.split("-")
    header = {'X-Auth-Token':'ppo_10_10096', }
    url = f"https://olimp.miet.ru/ppo_it_final?day=" + d + "&month=" + m + "&year=" + y
    response = requests.get(url, headers=header)
    resv_data = response.json()
    return resv_data #dict


def api_post_validate(count, nums, date):
    header = {'X-Auth-Token':'ppo_10_10096', 'Content-Type':'applications/json'}
    content = {"data":{"count": count, "rooms": [i for i in nums]}, "date": date,}
    print(json.dumps(content))
    url = f"https://olimp.miet.ru/ppo_it_final"
    response = requests.post(url, headers=header, data=json.dumps(content))
    resv_data = response.json()
    return resv_data

a = api_get_datelist()
print(a)

b = api_get_dateinfo("25-01-23")
print(b)

c = api_post_validate(1, [0,2,3], '25-01-23') #<int> <list> <str>
print(c)