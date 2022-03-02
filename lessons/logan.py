alist = ['one', 'two', 'one', 'two']
empty = {}
index = 0 
length = len(alist)
counter = 1 


while index != length:
	if alist[index] in empty:
		counter += 1 
		empty[alist[index]] = counter
	else:
		counter = 1
		empty[alist[index]] = counter
		index += 1
print(empty)


# protos

def count(x: list[str]) -> dict[str, int]:

    inverse_dict = {x[k]: k for k in x}
    
    return(inverse_dict)    


    flipped = {}

    for key, value in x.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)


            def invert(x: dict[str, str]):
    """Inverts dict key and vaule."""
    inverse_dict = {v: k for k, v in x.items()}
    x_values = x.values()
    inverse_dict_keys = inverse_dict.keys()
    if x_values == inverse_dict_keys:
        print(inverse_dict) 
    else:
        print("Error")


        def count(x: list[str]) -> dict[str, int]:
    empty = {}
    index = 0 
    counter = 1
    length = len(x)
    while index != length:
        if x[index] in empty:
            empty[x[index]] = counter
            index += 1
        else:
            counter


            index = 0 
    dic = {}
    max_length = len(x)
    while index != max_length:
        if x[index] in dic:
            dic[x[index]] += 1
        else:
            dic[x[index]] = 1
            index + 1 