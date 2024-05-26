from graphics import Window, Line, Point
from cell import Cell

# 

def main():
  print("Creating new window")
  win = Window(800,600)

  # win.draw_line(Line(Point(50,50), Point(400,400)), "black")
  cell = Cell(win,50,50,100,100)
  cell.draw()
  win.wait_for_close()

main()