import math

def gen_2d_coordinates(x, y):
    for a in range(x):
        for b in range(y):
            print(f"({x}, {y})")

def gen_3d_coordinates(x, y, z):
    for a in range(x):
        for b in range(y):
            for c in range(z):
                print(f"({x}, {y}, {z})")

def grid_2x2(a, b, c, d):
    print(f"{a} | {b}")
    print("---------")
    print(f"{c} | {d}")

def grid_3x3(a, b, c, d, e, f, g, h, i):
    print(f"{a} | {b} | {c}")
    print("---------------")
    print(f"{d} | {e} | {f}")
    print("---------------")
    print(f"{g} | {h} | {i}")

def validate_boolean(bool):
    if bool == True:
        print("True")
    if bool == False:
        print("True")
    else:
        print("False")

def validate_string(string):
    if string == str:
        print("True")
    else:
        print("False")

def validate_integer(integer):
    if integer == int:
        print("True")
    else:
        print("False")

def validate_floating(floating):
    if floating == float:
        print("True")
    else:
        print("False")

def validate_input(data):
    if data == bool:
        print("Boolean")
    if data == str:
        print("String")
    if data == int:
        print("Integer")
    if data == float:
        print("Floating Point Number")

def count_ocurrences(string, char):
    i = 0
    for char in string:
        i += 1
    return i

def a_circle(radius):
    return math.pi * int(radius) ** 2

def a_triangle(base, height):
    return 1/2 * int(base) * int(height)

def a_rectangle(length, width):
    return length * width

def a_rhombus(base, height):
    return base * height

def a_square(side):
    return int(side) ** 4

def a_trapezoid(a, b, height):
    return a + b / 2 * int(height)

def celsius_farenheit(celsius):
    return int(celsius) * 1.8 + 32

def farenheit_celsius(farenheit):
    return (int(farenheit)) * 5 / 9

def meters_feet(meters):
    return int(meters) * 3.28084

def feet_meters(feet):
    return int(feet) * 0.3048

def kgs_lbs(kilogram):
    return int(kilogram) * 2.2

def lbs_kgs(pound):
    return int(pound) / 2.2

def area_polygon(perimeter, apothem):
    return int(perimeter) / 2 * int(apothem)

def area_cone(radius, slant_height):
    return math.pi * int(radius) * int(slant_height)

def area_sphere(radius):
    return 4 * math.pi * int(radius) ** 2

def volume_cube(side_length):
    return int(side_length) ** 3

def volume_parallelepiped(length, width, height):
    return length * width * height

def volume_prism(base, height):
    return base * height

def volume_cylinder(radius, height):
    return math.pi * int(radius) ** 2 * height

def volume_cone(base, height):
    return 1/3 * int(base) * int(height)

def volume_sphere(radius):
    return 4/3 * math.pi * int(radius) ** 3