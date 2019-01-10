items = [0,1,2,3,4,5]

item = filter(lambda x: x==2 or x == 3, items)

items_x_4 = map(lambda item: item * 4, items)

def random_def():
    for item in items_x_4:
         print(item)
random_def()