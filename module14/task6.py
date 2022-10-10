#Задача 6. Монетка 2
def test_point(x, y, rad):
    rad /= 2
    if rad <= x <= rad and rad <= y <= rad:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")

print("Введите координаты монетки:")
x_input, y_input = float(input("X: ")), float(input("Y: "))
rad_input = int(input("Введите радиус: "))
test_point(x_input, y_input, rad_input)