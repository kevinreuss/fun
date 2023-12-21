from renderer import *

if __name__ == '__main__':
    screen = Screen(30, 10)
    screen.add_line(Line(2, 7, 10, 2))
    screen.add_line(Line(10, 2, 20, 7))
    screen.add_line(Line(20, 7, 2, 7))

    screen.add_line(Line(22, 2, 26, 2))
    screen.add_line(Line(26, 2, 26, 5))
    screen.add_line(Line(26, 5, 22, 5))
    screen.add_line(Line(22, 5, 22, 2))
    screen.render()
