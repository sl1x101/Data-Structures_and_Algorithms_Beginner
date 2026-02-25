#Array & list basic
def  find_max(number):
    max_val = number[0]
    for num in number:
        if num > max_val:
            max_val = num
    return max_val
my_list = [10,5,20,15]
print(f"max value:{find_max(my_list)}")