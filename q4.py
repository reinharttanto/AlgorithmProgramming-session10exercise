def calc_new_height():
    m = int(input("Enter the current width: "))
    n = int(input("Enter the current height: "))
    z = int(input("Enter the desired width: "))
    r = n / m  #Get Ratio
    w = z * r #Get desired width
    print("The corresponding height is:", w)
    return w


