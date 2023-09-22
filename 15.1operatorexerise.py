#always do first bracket and inside bracket also do first * then / then + then - 
#a+b*c-d/a
#(a+b)*(c-d)/a
#(a+b*c)-d/a
#a+b*(c-d/a)
a = 5
b = 10
c = 15
d = 20
print(a + b * c - d / a)
print((a + b) * (c - d) / a)
print((a + b * c) - d / a)
print((a + b * (c - d/ a)))
