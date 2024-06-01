from large_list import liste

def filter_tuples(list):
    new_list = []
    for tuple in list:
        if tuple[0] + tuple[1]  ==  tuple[2]:
            new_list.append(tuple)
    return new_list

def selection_sort(list):
    for i in range(len(list)):
        min_index = i 
        for j in range(i+1, len(list)):
            if list[j][-1] < list[min_index][-1]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

listeTuples = liste
new_list = filter_tuples(listeTuples)
sorted_list = selection_sort(new_list)

print(sorted_list)





