def g(a, b):
    while b:
        a, b = b, a % b
    return a
def h(a, b):
    return a * b // g(a, b)
def nok_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = h(result, numbers[i])
    return result
numbers = input(" ")
numbers = [int(num) for num in numbers.split(",")]
nok = nok_list((numbers))
print("NOK",numbers,"=", nok)





