# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import numpy as np




class AnalysedText(object):
    def __init__(self, text):

        pass
    # text2 = "Michael is handsome MichaelMichaelMichaelMichael"
    # text3 = text2.replace('Michael', 'Julie')
    # print(f"Text3 {text3}")
    # print(f"Type of {text2.split()} is {type(text2.split())}")
    # print(f"Count of Michael = {text2.count('Michael')}")


def shuffle(input_list, card_number):
    print(f"Origin cards = {input_list}, will be shuffle by each partition of {card_number} cards.")
    start_index = 0
    partition_list = []

    if len(input_list)%card_number == 0:
        partition = len(input_list)//card_number
        for group_index in range(partition):
            partition_list.append(result[start_index:start_index + card_number:])
            start_index+=card_number
        print(f"partition_list = {partition_list}")
    else:
        partition = len(input_list) // card_number + 1
        for group_index in range(partition):
            if group_index == partition-1:
                partition_list.append(result[start_index::])
                start_index+=card_number
            else:
                partition_list.append(result[start_index:start_index + card_number:])
                start_index += card_number
        print(f"partition_list = {partition_list}")

    if len(partition_list)%2 == 0:
        for index in range(int(len(partition_list)/2)):
            partition_list[index], partition_list[len(partition_list)-1-index] = partition_list[len(partition_list)-1-index], partition_list[index]
    else:
        for index in range(len(partition_list)//2):
            partition_list[index], partition_list[len(partition_list) - 1 - index] = partition_list[
                                                                                         len(partition_list) - 1 - index], \
                                                                                     partition_list[index]
    print(f"After shuffle = {partition_list}")
    input_list = []
    for group in partition_list:
        for element in group:
            input_list.append(element)
    print(f"Return input_list = {input_list}")
    return input_list





input_data = []

while(input() != ''):
    print(input_line)

input_line = input()
print(input_line)
if input_line == '':
    # break
    pass
else:
    input_data.append(input_line)
print(f"final = {input_data}")
result = 0
for element in input_data:
    result += int(element)
print(result)




