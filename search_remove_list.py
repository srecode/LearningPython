def search_remove_list(list_1,list_2):
    for element in list_1:
        if element in list_2:
            list_2.remove(element)

    return list_2

list_1 = ["a", "b"]
list_2 = ["a", "b", "c"]

print(search_remove_list(list_1,list_2))