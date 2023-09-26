import json
# f = open('Test/new.json')
f = open('new.json')
data = json.load(f)


def func(type, fakultet, guruh, kun):
    for i in data[type]:
        for j in i[fakultet]:
            # print(j[guruh])
            for l in j[guruh]:
                print(l)
                # txt = ''
                # for m in l[kun]:
                #     txt += f"<code>{m['time']}</code> | {m['fan']} | <a href='{m['zoom']}'>{m['domla']}</a>\n"
                # return txt


f.close()
# func()
for x in data['students'][0]['farmatsiya'][0]['f101a'][0]:
    print(x)
# print(data['students']['sanoat'])
