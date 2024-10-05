def add_dots(str):
    return ".".join(str)
res = add_dots("test")
print(res)

def remove_dots(str):
    return str.replace('.',"")
res = remove_dots("t.e.s...t")
print(res)