import json
f = open('Test/new.json')
data = json.load(f)


def func(type, fakultet, guruh, kun):
    for i in data[type]:
        for j in i[fakultet]:
            # print(j[guruh])
            for l in j[guruh]:
                txt = ''
                for m in l[kun]:
                    txt += f"<code>{m['time']}</code> | {m['fan']} | <a href='{m['zoom']}'>{m['domla']}</a>\n"
                return txt


f.close()


# print(data['students'][0]['farmatsiya'][0]['1-kurs'][0]['f101a'][0]['Du'][0]['08:30'])
# print(data['students']['sanoat'])
