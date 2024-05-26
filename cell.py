from graphics import Line, Point

class Cell():
    """A cell represents one square with 4 points."""
    def __init__(self, window, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._mid_x = ((self._x1 + self._x2) / 2)
        self._mid_y = ((self._y1 + self._y2) / 2)
        self._win = window

    def draw_move(self, to_cell, undo=False):
        color = "red" if undo == False else "gray"
        line = Line(Point(self._mid_x, self._mid_y), Point(to_cell._mid_x, to_cell._mid_y))

        self._win.draw_line(line, color)
        
    def draw(self):
        '''Self drawing autonomous square with a thirst for human suffering
        '''

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
            
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))
            self._win.draw_line(line, "black")