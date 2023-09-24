
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
# The last part, I guess...#
max_value = 0
max_key = ""
for k, v in x.items:
    if v > max_value:
        max_value = v
        max_key = k

print("The commonly used char(letter) is {} and it's repeated {} times !".format(max_key, max_value))