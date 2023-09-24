
my_str = "Hello everyone and welcome to GitHub !"

x = {}

for i in my_str:
    if i.isalpha():
        # print(i, end=" ")
# second part >>>#
        if i in x.keys():
            x[i] += 1
        else:
            x[i] = 1

print(x)