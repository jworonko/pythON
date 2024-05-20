# import math
#
# print("pi", math.pi)
#
def put_a_brick():
    print("-", sep="", end="")
#
# def build_a_wall():
#     wall_length = 10
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_a_wall()

def build_a_wall(wall_length):
    for brick in range(wall_length):
        put_a_brick()
    print()

build_a_wall(20)
build_a_wall(30)
build_a_wall(5)

# def function_with_params(sth, sth_else):
#     print(sth, sth_else)
#
# function_with_params(1,4)
