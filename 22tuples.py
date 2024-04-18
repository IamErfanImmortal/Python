tuple_a = (1,2,3,4,5)
tuple_b = ("Apple" , "Orange" , "Berry")

tuple_c = tuple_a + tuple_b
a,b,c = tuple_b

try:
    tuple_a[0] = 2
except Exception as e:
    print(f" Error: {e}!. Tuples cannot be modified.")

