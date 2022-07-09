import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for itr in range(value):
                self.contents.append(key)

    def draw(self, numb):

        if numb > len(self.contents):
            numb = len(self.contents)

        extr_list = []

        for i in range(numb):
            bila = self.contents.pop(random.randrange(len(self.contents)))
            extr_list.append(bila)
        return extr_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for j in range(num_experiments):

        hat_work = copy.deepcopy(hat)
        loto = hat_work.draw(num_balls_drawn)
        flag = True
        for key,value in expected_balls.items():
            if loto.count(key) < value:
                flag = False
                break

        if flag:
            num_success += 1

    return (num_success / num_experiments) *100


hat = Hat(a=8, b=9, g=16, k=23)
#print(hat)
a=experiment(hat,{"a":2, "g":5}, 10, 10000)
print(a)

