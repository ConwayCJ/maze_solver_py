from graphics import Line, Point

class Cell():
    """A cell represents one square with 4 points."""
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        color = "red" if undo == False else "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, color)
        
    def draw(self, x1, y1, x2, y2):
        '''Self drawing autonomous square with a thirst for human suffering
        '''
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(line, "white")
            
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(line, "white")