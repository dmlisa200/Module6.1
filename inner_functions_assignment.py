a_list = [2.1, 3.4]
b_list = [3.5]


def measurements(list):
    def area(list):
        area = list[0] * list[1]
        print("Area = " + str(area))

    def perimeter(list):
        perimeter = (list[0]*2) + (list[1]*2)
        print("Perimeter = " + str(perimeter))

    def square_area(list):
        square_area = list[0] * list[0]
        print("square_area = " + str(square_area))

    def square_perimeter(list):
        square_perimeter = list[0] * 4
        print("square_perimeter = " + str(square_perimeter))


    perimeter(a_list)
    area(a_list)
    square_area(b_list)
    square_perimeter(b_list)


measurements(list)
