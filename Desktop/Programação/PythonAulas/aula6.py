# Type Conversion or Coercion
# You can convert one type to another
# immutable and primitive type:
# str, int, float, bool
# Type casting: int(), str(), float(), bool()

print(1+1) # both are int, so 1+1=2
print('1' + '1') # now both are str, so 1+1 = 11
print('a' + 'b') # both are str, a+b = ab

#print('1' + 1) # throws an error, can't concatenate str and int
print(int('1')+ 1) # using the int class, we convert str to int

# to sum, the int is converted to float
print(float('1') + 1) 