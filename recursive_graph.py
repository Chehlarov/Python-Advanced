from turtle import *


# Write your code here
def draw_branch(branch_length, angle, width):
    if branch_length > 5:
        pensize(width)
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle, width // 1.5)
        left(2 * angle)
        draw_branch(branch_length - 15, angle, width // 1.5)
        right(angle)
        backward(branch_length)


# draw_branch(100, 20)
def draw_tree(trunk_length, angle, width):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, width)
    done()


draw_tree(100, 45, 16)
