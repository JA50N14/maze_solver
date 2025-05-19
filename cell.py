from canvas import Point, Line

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False
    
    def __repr__(self):
        return f'x1: {self._x1}, y1: {self._y1}, x2: {self._x2}, y2: {self._y2}'

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall, fill_color="black")
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall, fill_color="white")
        
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall, fill_color="black")
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall, fill_color="white")

        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall, fill_color="black")
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall, fill_color="white")
        
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall, fill_color="black")
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall, fill_color="white")
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
    
        cell_centre_1 = [abs((self._x1 + self._x2) / 2), abs((self._y1 + self._y2) / 2)]
        cell_centre_2 = [abs((to_cell._x1 + to_cell._x2) / 2), abs((to_cell._y1 + to_cell._y2) / 2)]
        line = Line(Point(cell_centre_1[0], cell_centre_1[1]), Point(cell_centre_2[0], cell_centre_2[1]))
        self._win.draw_line(line, fill_color)

    






