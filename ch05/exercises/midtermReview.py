def find_min():
    print("PLease enter 3 numbers")
    num_a = int(input(":")) # 10
    num_b = int(input(":")) # 5
    num_c = int(input(":")) # 2

    lowest = num_a

    if num_b < lowest:
        lowest = num_b
    
    if num_c < lowest:
        lowest = num_c

    print(lowest)


find_min()
