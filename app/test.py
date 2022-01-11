class MazeRunnerChanged1(object):

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True

    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self

################################################################################

def maze_controller(maze_runner):
  import random
  def left():
    maze_runner.turn_left()
    maze_runner.turn_right()
  def around():
    left()
    left()
  def forward():
    return maze_runner.go()
  def isPathLeft():
    left()
    res = forward()
    if res:
      around()
      forward()
      left()
      return True
    else:
      right()
      return False
  def isPathForward222():
  # some comment
  def isPathForward():
    res = forward()
    if res:
      around()
      forward()
      around()
      return True
    else:
      return False
  def isPathRight():
    right()
    res = forward()
    if res:
      around()
      forward()
      right()
      return True
    else:
      left()
      return False

  ways = []
  while maze_runner.found() == False:

    if isPathLeft():
      ways.append('l')
    if isPathRight():
      ways.append('r')
    if isPathForward():
      ways.append('f')

    if len(ways) == 0:
      around()
    else:
      r = random.choice(ways)
      ways = []

      if r == 'l':
        left()
      if r == 'r':
        right()

    forward()

  # if isPathLeft():
  #   left()
  # else:
  #   if isPathForward():
  #     pass
  #   else:
  #     if isPathRight():
  #       right()
  #     else:
  #       around()
  # forward()

# x + s ?




1+1=2

################################################################################

maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found()

maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}
maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True






# def maze_controller(maze_runner):
#   import random
#   orient = ['N'] # 'N','O','S','W'
#   coords = [0,0]
#   karte  = [['s']]

#   def buildKarte(orient, what):
#     print("buildKarte: " + str(orient[0]) + what)
#     if orient[0] == 'N':
#       searchedCoords = [coords[0], coords[1] + 1]
#       if karte[searchedCoords][1]:
#         print("karte[searchedCoords]", karte[searchedCoords])
#         pass
#       else:
#         karte[searchedCoords][coords[0]] = what
#         print("karte", karte)
#     if orient[0] == 'S':
#       pass
#     if orient[0] == 'W':
#       pass
#     if orient[0] == 'O':
#       pass
#   def changeCoords(arg):
#     if arg == 'N':
#       coords[1] = coords[1] + 1
#     if arg == 'S':
#       coords[1] = coords[1] - 1
#     if arg == 'W':
#       coords[0] = coords[0] - 1
#     if arg == 'O':
#       coords[0] = coords[0] + 1
#     print("coords", coords)

#   def change_orient(arg):
#     if arg == 'l':
#       if orient[0] == 'N':
#         orient[0] = 'W'
#       elif orient[0] == 'W':
#         orient[0] = 'S'
#       elif orient[0] == 'S':
#         orient[0] = 'O'
#       else:
#         orient[0] = 'N'
#     if arg == 'r':
#       if orient[0] == 'N':
#         orient[0] = 'O'
#       elif orient[0] == 'O':
#         orient[0] = 'S'
#       elif orient[0] == 'S':
#         orient[0] = 'W'
#       else:
#         orient[0] = 'N'
#   def left():
#     maze_runner.turn_left()
#     change_orient('l')
#   def right():
#     maze_runner.turn_right()
#     change_orient('r')
#   def around():
#     left()
#     left()
#   def forward():
#     res = maze_runner.go()
#     # this is all for build karte
#     #if res:
#       # buildKarte(orient,'+')
#       #changeCoords(orient[0])
#       # return (orient,'+')
#     # else:
#       # buildKarte(orient,'-')
#       # return (orient,'-')
#     return res
#   def isPathLeft():
#     left()
#     res = forward()
#     if res:
#       around()
#       forward()
#       left()
#       return True
#     else:
#       right()
#       return False
#   def isPathForward():
#     res = forward()
#     if res:
#       around()
#       forward()
#       around()
#       return True
#     else:
#       return False
#   def isPathRight():
#     right()
#     res = forward()
#     if res:
#       around()
#       forward()
#       right()
#       return True
#     else:
#       left()
#       return False

#   # print 'run l: ' + str(isPathLeft())
#   # print 'run f: ' + str(isPathForward())
#   # print 'run r: ' + str(isPathRight())
#   # print("my result", maze_runner.found())

#   ways = []
#   while maze_runner.found() == False:

#     if isPathLeft():
#       ways.append('l')
#     if isPathRight():
#       ways.append('r')
#     if isPathForward():
#       ways.append('f')

#     if len(ways) == 0:
#       around()
#     else:
#       r = random.choice(ways)
#       ways = []

#       if r == 'l':
#         left()
#       if r == 'r':
#         right()

#     forward()
