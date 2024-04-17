from functools import reduce

def sum_num(*data):
    numbers = []
    for item in data:
        if type(item) is int:
            numbers.append(item)
    return numbers


num_filter = lambda *data: [item for item in data if type(item) is int]
my_sum = lambda *mums : reduce(lambda a, b: a + b, mums)


sum_num(1, True, [], {}, (1,2,3,44), 1, 10000, 0, -90 ,12134342)

numbers = num_filter(100000, 1010, -90, True, 0, False, {1,2,5,8}, (), {"id":1})
print(my_sum(numbers))


