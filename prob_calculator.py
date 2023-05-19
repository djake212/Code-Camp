import copy
import random
# Consider using the modules imported above.

class Hat:
  
  contents = []
  
  def __init__(self,**kwargs):
    self.contents = []
    for key, value in kwargs.items():
      count = value
      while True:
        self.contents.append(key)
        count -= 1
        if count == 0:
          break
    return

  def draw(self,ballnum):
    ballstaken = []
    copyself = copy.deepcopy(self)
    for balls in range(ballnum):
      numb = len(self.contents) - 1
      if numb == -1:
        self = copy.deepcopy(copyself)
        numb = len(self.contents) - 1
      randint = random.randint(0,numb)
      ballstaken.append(self.contents.pop(randint))
    return ballstaken

    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  totexp = 0
  totcorrect = 0
  while True:
    
    hatsave = copy.deepcopy(hat)
    ballcount = {}

    ballstake = hatsave.draw(num_balls_drawn)
    for balls in ballstake:
      ballcount[balls] = ballcount.get(balls,0) + 1

    for dicitems in expected_balls.keys():
      try:
        if ballcount[dicitems] >= expected_balls[dicitems]:
          succ = True
        else:
          succ = False
          break
      except:
        succ = False
        break
      
    if succ is True:
      totcorrect += 1
    totexp += 1
    if totexp == num_experiments:
      break
  #print('total correct:',totcorrect, 'total exp:', totexp)
  return totcorrect/totexp
  
        
