class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = []
    
    def add_line(self, line):
        self.lines.append(line)

    def render(self):
        for i in range(self.height):
            row = self.create_row(i)
            print(row)

    def create_row(self, column):
        row = ""
        for i in range(self.width):
            if column == 0 or column == self.height - 1:
                row = row + "-"
            else:
                if i == 0 or i == self.width - 1:
                    row = row + "|"
                else:
                    row = row + self.render_pixel(i, column)
        return row
    
    def render_pixel(self, x, y):
        for line in self.lines:
            if self.is_on_line(line, x, y):
                return '*'
        return ' '

    def is_on_line(self, line, x, y):
        if x < min(line.x1, line.x2):
            return False
        if x > max(line.x1, line.x2):
            return False
        if y < min(line.y1, line.y2):
            return False
        if y > max(line.y1, line.y2):
            return False
        if line.x1 == x and line.y1 == y:
            return '*'
        if line.x2 == x and line.y2 == y:
            return '*'
        linedx = line.x2 - line.x1
        linedy = line.y2 - line.y1
        if linedx != 0:
            slope = linedy / linedx
            dx = x - line.x1
            dy = slope * dx
            if round(line.y1 + dy) == y:
                return True
            else:
                return False
        else:
            if line.x1 == x:
                return True
            else:
                return False

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2