import json
f = open('Test/kv.json')
data = json.load(f)


def func(kun):
    txt = f" {data[kun][0]['user']} {data[kun][0]['food']}"
    return txt


f.close()


# print(data['Mon'][0]['user'])
# print(data['students']['sanoat'])
