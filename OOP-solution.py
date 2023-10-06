class Pod_Racer:
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def repair(self):
        self.condition = 'repaired'


class Jar_Jar_Binks(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner='Jar Jar Binks'):
        super().__init__(self, max_speed, condition, price, owner)

    def boost(self):
        self.max_speed *= 2


class Darth(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner='Darth Vader'):
        super().__init__(self, max_speed, condition, price, owner)

        def flame_jet(self, other_pod):
            print('flaming', other_pod.owner)
            other_pod.condition = 'destroyed'


jar_Jar_Binks_Pod = Jar_Jar_Binks(25, 'perfect', 1000)

darth_pod = Darth(50, 'perfect', 500)

print('jar jar condition', jar_Jar_Binks_Pod.condition)
print('darth condition', darth_pod.condition)

darth_pod.flame_jet(jar_Jar_Binks_Pod)

print('jar jar condition', jar_Jar_Binks_Pod.condition)
print('darth condition', darth_pod.condition)
