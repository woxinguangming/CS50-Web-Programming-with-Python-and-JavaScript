people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]

# def f(person):
#     return person["name"]

# people.sort(key = f)
# lambda表达式取代定义函数f, people作为参数,people["name"]作为返回值
people.sort(key = lambda people: people["name"])
print(people)