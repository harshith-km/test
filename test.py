



# def my_decorator(func):
#     def wrapper():
#         print('before the function')
#         func()
#         print('after the function')
#     return wrapper


# @my_decorator
# def hello_world():
#     print('hello !')



# hello_world()


def find_max_in_nested_list(nested_list):
    largest = nested_list[0][0]

    for lis in nested_list:
        for item in lis:
            if item > largest:
                largest = item

    print(largest)

find_max_in_nested_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
find_max_in_nested_list([[10, 20], [30, 5], [1, 2]])