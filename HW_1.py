
# 1. Создать переменную типа String
My_name = "Artem"
# 2. Создать переменную типа Integer
Age = 37
# 3. Создать переменную типа Float
Weight = 70
# 4. Создать переменную типа Bytes
a_bytes = bytes(5)
# 5. Создать переменную типа List
Friends = ["Vadim", "Sergei", "Ivan", "Kostya", "Nikita", "Pasha", "Valik"]
# 6. Создать переменную типа Tuple
Tuple_friends = tuple(Friends)
# 7. Создать переменную типа Set
Set_friends = set(Friends)
# 8. Создать переменную типа Frozen Set
FrozenSet_friends = frozenset(Friends)
# 9. Создать переменную типа Dict
Age_Friends = {"Vadim": 35, "Sergei": 30, "Ivan": 33, "Kostya": 31, "Nikita": 33, "Pasha": 33, "Valik": 33}
# 10. Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("Task #10")
print("     Task #1 My_name:            ", type(My_name), "   ", My_name)
print("     Task #2 Age:                ", type(Age), "   ", Age)
print("     Task #3 Weight:             ", type(Weight), '  ', Weight)
print("     Task #4 a_bytes:            ", type(a_bytes), '  ', a_bytes)
print("     Task #5 Friends:            ", type(Friends), '  ', Friends)
print("     Task #6 Tuple_friends:      ", type(Tuple_friends), '  ', Tuple_friends)
print("     Task #7 Set_friends:        ", type(Set_friends), '     ', Set_friends)
print("     Task #8 FrozenSet_friends:  ", type(FrozenSet_friends), '  ', FrozenSet_friends)
print("     Task #9 Age_Friends:        ", type(Age_Friends), '      ', Age_Friends)
# 11. Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
Wife = "Daria"
Cat = "Jack"
Happiness = Wife + Cat
print("Task #11:", Happiness)
# 12. Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 5
b = 10
Summ = a + b
print("Task #12:", Summ)
# 13. Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
Mult = a*b
print("Task #13:", Mult)
# 14. Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
Div = a/b
print("Task #14:", Div)
# 15. Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
DivWhole = a // b
print("Task #15:", DivWhole)
# 16. Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
Residue = a % b
print("Task #16:", Residue)
# 17. (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
Total = (7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4
print("Task #17:", Total)

