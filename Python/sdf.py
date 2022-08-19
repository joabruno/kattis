class cd:
    shortest = 10

    def something(self):
        self.shortest += 1

to = cd()
to.something()
print(to.shortest)