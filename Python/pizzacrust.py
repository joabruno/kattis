r,c = input().split()
pi = 3.14159265359
pizza_area = int(r)**2 * pi
pizza_area_inner = (int(r) - int(c))**2 * pi

print(pizza_area_inner/pizza_area*100)