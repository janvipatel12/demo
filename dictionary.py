
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
student={
"name":"happy",
"age":21,
"city":"ahmd"
}

print(student["name"],student["age"],student["city"])
student2=student.copy()
print(student2)
print(student.get("name"))
lst=student.items()
print(lst)
print(student2.keys())
print(student2.pop('name'))
print(student2.popitem())
print(dict.fromkeys(student2))
print(student2.values())
print(student2.setdefault("course","python"))
student2.update({"name":"shree","age":20})
student2.clear()
print(student2)
#print(dir(dict))


