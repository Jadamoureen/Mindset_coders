#Try to see what results you get looking for character: (X).
# First with .find() method and then with .index() method.

str="The best revenge is massive success."

#.find() method returns -1, when it can’t find a character
ans_1=str.find("X")

#.index() method returns a ValueError.
ans_2=str.index("X")

print(ans_1)
