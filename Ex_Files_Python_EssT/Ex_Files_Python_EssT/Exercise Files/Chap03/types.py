#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x=(2,3,[4,5],'two', 2.0)

y=(2,3,[4,5],'two', 2.0)

print("The x, y are both same tuples but ID is differnt")
print(id(x))
print(id(y))
print("But the x[0] and y[0] has the same ID, Python deosnt need to create x[0] and then again y[0]", id(x[0]), id(y[0]))

print("Also know that below will never work if you want to compare the type\n"
      "if type(x) is tuple -> this is wrong and that is why we use isinstance\n"
      "if isinstance(x, tuple)")
if isinstance(x,tuple):
    print("yep")
else:
    print("nope")