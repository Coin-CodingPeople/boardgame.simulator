"""
Created by hangeonho on 2018. 10. 1..
"""
import random
import operator


def set_random_stack(stack):
    stack.clear()
    for index in range(8):
        stack.append(random.randrange(1, 6))


def is_same(list1, list2):
    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
        return True


def is_any_same(answer_list, list_list):
    for list in list_list:
        if is_same(list, answer_list):
            return True
        return False


def count_numbers(list_list):
    number_dict = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    for list in list_list:
        for list_item in list:
            number_dict[list_item] += 1

    return number_dict


stack = []  # answer

user1 = []
user2 = []
user3 = []
user4 = []

count = 1

counts = []
results = []

for i in range(10):
    for i in range(50):
        count = 1
        while count == 1 or is_any_same(stack, [user1, user2, user3, user4]):
            set_random_stack(stack)
            set_random_stack(user1)
            set_random_stack(user2)
            set_random_stack(user3)
            set_random_stack(user4)
            count += 1
        result = count_numbers([stack, user1, user2, user3, user4])
        counts.append(count)
        results.append(result[max(result.items(), key=operator.itemgetter(1))[0]])

    print(max(counts))
    print(max(results))
