#1
def merge_lists_to_dict(k, v):
    return dict(zip(k, v))

word = ["f", "a", "b", "c"]
price = [50, 30, 60, 40]

result1 = merge_lists_to_dict(k=word, v=price)
result2 = merge_lists_to_dict(word, v=[100, 200, 300])

print(result1)
print(result2)


#2
def update_car_info(**cu):
    car = cu
    car['is_available'] = True
    return car

result = update_car_info(brand='Nissan', price=7000000)

print(result)