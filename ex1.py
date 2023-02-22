def print_n_time(str, n):
    print(str * n)

def get_sec_in_min(sec_in_day):
    return sec_in_day % 60
x = get_sec_in_min(86000)
print (x)

def print_time_from_sec(sec_in_day):
    x= (sec_in_day) % 60
    y= (sec_in_day//60) % 60
    z= sec_in_day//60//60
    print(str(x)+":"+str(y)+":"+str(z))
    print (sec_in_day)
print_time_from_sec(86000)
x = get_sec_in_min(86000)
print (x)

("Hello World", 5)
print_n_time("Manetheren", 4)
