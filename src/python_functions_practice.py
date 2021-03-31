def return_10():
    return 10

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y

def length_of_string(x):
    return len(x)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number( x, y ):
    return int(x) + int(y)

def number_to_full_month_name(x):
    lst = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November',
            'December']
    return lst[x-1]

def number_to_short_month_name(x):
    lst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sept', 'Oct', 'Nov',
            'Dec']
    return lst[x-1] 

def calc_vol_cube(x,y,z):
    return (x*y*z)

def reverseString(string):
    revStr = string[::-1]
    return revStr

def ftoc(x):
    cels = (x - 32) * (5/9) 
    return cels