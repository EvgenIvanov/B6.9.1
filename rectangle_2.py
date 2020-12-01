from lesson.rectangle import Rectangle, Square

# создаем два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# вывод площади прямоугольников
print('площадь 1 прямоугольника:', rect_1.get_area())
print('площадь 2 прямоугольника:', rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(f'площадь 1-го квадрата: {square_1.get_area_square()}\n\
площадь 2-го квадрата: {square_2.get_area_square()}')

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())