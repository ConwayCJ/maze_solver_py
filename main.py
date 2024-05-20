from graphics import Window, Line, Point, Cell

# 

def main():
  print("Creating new window")
  win = Window(800,600)

  win.draw_line(Line(Point(50,50), Point(400,400)), "black")
  cell = Cell(win,100,100,500,500)
  cell.draw()
  win.wait_for_close()

main()