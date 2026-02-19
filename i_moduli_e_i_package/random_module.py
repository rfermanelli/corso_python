import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(10))
print(random.randrange(3, 10))
print(random.randrange(3, 10, 2))
print(random.choice('abc'))
print(random.choices('abcdefghilmnopqrstuvz', k=3))
print(random.sample(range(10), 3))
carte = ["asso di quadri", "q di cuori", "k di fiori"]
random.shuffle(carte)
print(carte)


