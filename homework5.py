immutable_var = 2, "четное", 3, "нечетное", True
print("immutable_var:", immutable_var)
# immutable_var[3] = "четное" - нельзя заменить поскольку переменная-"immutable_var" является неизменяемым типом данных и относится к категории "tuple"
mutable_list = [2, "четное", 3, "нечетное", True]
mutable_list[3] = "четное"
print("mutable_list:", mutable_list)
