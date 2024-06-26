from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
  print("Creating new window")
  num_rows = 12
  num_cols = 16
  margin = 50
  screen_x = num_cols * margin
  screen_y = num_rows * margin
  cell_size_x = (screen_x - 2 * margin) / num_cols
  cell_size_y = (screen_y - 2 * margin) / num_rows
  win = Window(screen_x, screen_y)

  maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 15)
  
  win.wait_for_close()

main()