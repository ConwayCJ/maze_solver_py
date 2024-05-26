from cell import Cell
import time

class Maze ():
  def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win,
  ):
    self._x1 = x1  
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    
    self._cells = []
    self._create_cells()
    self._break_entrance_and_exit()

  def _create_cells(self):
    print("Creating cells")
    for i in range(self._num_cols):
      cell_row = []
      for j in range(self._num_rows):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        print("Appending a cell", x1,y1,x2,y2)
        cell_row.append(Cell(self._win, x1,y1,x2,y2))
      self._cells.append(cell_row)
    print("Done")

  def _draw_cell(self):
    for row in self._cells:
      for col in row:
        col.draw()
        self._animate()

  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    last_col = len(self._cells) - 1
    last_row = len(self._cells[last_col]) - 1
    
    self._cells[0][0].has_top_wall = False
    self._cells[0][0].has_left_wall = False

    self._cells[last_col][last_row].has_right_wall = False
    self._cells[last_col][last_row].has_bottom_wall = False