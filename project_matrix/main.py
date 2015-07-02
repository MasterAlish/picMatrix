import random
from pic_matrix import PicMatrix


def add_to_arr_random_number(a):
    if random.randint(1,4) <3:
        a.append(random.randint(1, 500))
    else:
        a.append(random.randint(1, 10))
    return a

for i in range(20):
    test_pic_weights = reduce(lambda arr, e: add_to_arr_random_number(arr), range(50), [])
    PicMatrix(test_pic_weights).run()