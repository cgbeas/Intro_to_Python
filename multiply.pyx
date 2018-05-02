##############################
# My Compiled Python Program
#############################

cpdef int multiply(int a, int b):
    return a * b

cdef int result
result = multiply(2, 4)
print(result)
