def selection_sort_one_pass(list):
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    list[0], list[min_index] = list[min_index], list[0]

    return list 

        
print(selection_sort_one_pass([3,1,5,2,0]))

        

    


