def max_in_list(list):
    my_max = 0
    for num in list:
        if num > my_max:
            my_max = num
    print(f"Il numero più grande della lista passata è {my_max}")