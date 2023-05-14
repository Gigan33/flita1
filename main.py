set_double = set()
set_decimal = set()

def convert_into_set_decimal_from_double(set_double):
    for i in set_double:
        set_decimal.add(int(str(i), base=2))
    return set_decimal


print("Введите число не из двоичной системы чтобы прекратить ввод")
while (1):
    print("Введите довичное число")
    input_value = str(input())
    for i in input_value:
        if i != '1' and i != '0' and i:
            if set_double != set():
                set_decimal = convert_into_set_decimal_from_double(set_double)
                print("Двоичные:\n", *set_double)
                print("Десятичные:\n", *set_decimal)
            exit()
    if int(input_value) in set_double:
        print("Ошбка, такой элемент уже есть")
    set_double.add(int(input_value))
