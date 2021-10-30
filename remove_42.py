def remove_42(numbers):
    while 42 in numbers:
        numbers.remove(42)

    return numbers

nums = [42, 42, 3]
print(remove_42(nums))

#Modularies like so:
def remove_target(target_list, target):
    while target in target_list:
        target_list.remove(target)

    return target_list
