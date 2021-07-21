import random
import string

class Robot:

    robots = set()

    def __init__(self):
        self.name = self.generate_name()
        Robot.robots.add(self.name)

    def reset(self):
        Robot.robots.remove(self.name)
        self.name = self.generate_name()
        Robot.robots.add(self.name)

    def generate_name(self):
        random.seed()
        return ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))