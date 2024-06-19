import copy
import random
from collections import Counter

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for color, num_balls in kwargs.items():
            self.contents += [color] * num_balls
            
    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            sample = self.contents
            self.contents = []
            return sample
        sample = random.sample(self.contents, num_balls_drawn)
        for s in sample:
            self.contents.remove(s)
        return sample
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    for _ in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        draw = exp_hat.draw(num_balls_drawn)
        draw_count = Counter(draw)
        result = all([True if draw_count[color] >= expected_balls[color] else False for color in expected_balls.keys()])
        results.append(result)
        
    return round(float(sum(results)) / num_experiments, 3)
        
    
hat1 = Hat(yellow=3, blue=2, green=6)

hat = Hat(black=6, red=4, green=3)
prob = experiment(hat=hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(prob)
