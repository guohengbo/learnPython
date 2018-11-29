"""
    功能：五角星的绘制
    版本：2.0
    日期：08/08/2017
    新增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle


def draw_pentagram(size):
    """
        绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    while size <= 100:
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()

if __name__ == '__main__':
    main()
