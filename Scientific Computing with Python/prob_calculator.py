import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key,value in balls.items():
            for i in range(int(value)):
                self.contents.append(key)

    def draw(self, chance):
        if chance >= len(self.contents):
            chance = len(self.contents)

        rBall = []
        for i in range(chance):
            ball = self.contents.pop(random.randint(0, len(self.contents)-1))
            rBall.append(ball)
        return rBall
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        oriHat = copy.deepcopy(hat)
        result = oriHat.draw(num_balls_drawn)
        #need_count = [c for c in expected_balls]
        #need_count.sort()
        
        result = Counter(result)
        to_count = [c for c in result]
        flag = True
        for colour, num in expected_balls.items():
            if colour in result:
                if result[colour] < num:
                    flag = False
            else:
                flag = False

        if flag:
            success += 1
    return (success / num_experiments)