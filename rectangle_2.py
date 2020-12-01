from lesson.rectangle import Rectangle, Square, Circle

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

circle_1 = Circle(1)
circle_2 = Circle(10)

print(f'площадь 1-го круга: {circle_1.get_area_circle()}\n\
площадь 2-го круга: {circle_2.get_area_circle()}')


figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Circle):
        print(figure.get_area_circle())
    elif isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())