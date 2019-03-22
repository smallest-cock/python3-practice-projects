# python3

from random import randint
from math import sqrt
import matplotlib.pyplot as plt


class Rocket():
    def __init__(self, x=0, y=0, name='Rocket'):
        self.x = x
        self.y = y
        self.name = name

    def move(self, x_displacement=0, y_displacement=1):
        self.x += x_displacement
        self.y += y_displacement

    def distance(self, another_rocket):
        dist = round(sqrt((self.x - another_rocket.x)**2 + (self.y - another_rocket.y)**2), 2)
        return dist
# Defines Rocket class


class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights=0, name='Shuttle'):
        super().__init__(x, y)
        self.name = name
        self.flights = flights

    def home(self):
        self.x = 0
        self.y = 0
        self.flights += 1
# Defines Shuttle class (which inherits from the parent Rocket class) and adds some extra features


rockets = []
shuttles = []
rocketx = []
rockety = []
shuttlex = []
shuttley = []
rocketName = []
shuttleName = []

# Creates 5 rocket objects and 3 shuttle objects, and stores them in appropriate lists
for i in range(5):
    rockets.append(Rocket())
for i in range(3):
    shuttles.append(Shuttle())

# Randomly moves each rocket and shuttle
for i in rockets:
    i.move(randint(-10, 10), randint(1, 50))
for i in shuttles:
    i.move(randint(-10, 10), randint(1, 50))

# Takes a "snapshot" of the locations of all rockets and shuttles by storing location data in appropriate lists
# and prints location of each rocket/shuttle
print(' Check 1 '.center(60, '='))
print(' ')
for i in range(len(rockets)):
    rockets[i].name = rockets[i].name + ' ' + str(i)
    rocketName.append(rockets[i].name)
    rocketx.append(rockets[i].x)
    rockety.append(rockets[i].y)
    print('Rocket %s is at (%s, %s)' % (i, rockets[i].x, rockets[i].y))
print(' ')
for i in range(len(shuttles)):
    shuttles[i].name = shuttles[i].name + ' ' + str(i)
    shuttleName.append(shuttles[i].name)
    shuttlex.append(shuttles[i].x)
    shuttley.append(shuttles[i].y)
    if shuttles[i].flights == 1:
        print('Shuttle %s is at (%s, %s) and has completed %s flight.' %
              (i, shuttles[i].x, shuttles[i].y, shuttles[i].flights))
    elif shuttles[i].flights == 0:
        print('Shuttle %s is at (%s, %s) and hasn\'t completed any flights yet.' %
              (i, shuttles[i].x, shuttles[i].y,))
    else:
        print('Shuttle %s is at (%s, %s) and has completed %s flights.' %
              (i, shuttles[i].x, shuttles[i].y, shuttles[i].flights))
print(' ')
print(' ')

# Plots the first snapshot on an xy graph
x = rocketx
y = rockety
plt.plot(x, y, 'ro')
sx = shuttlex
sy = shuttley
plt.plot(sx, sy, 'bo')
plt.xlabel('Horizontal distance from lauch point (ft)')
plt.ylabel('Altitude (ft)')
for rock in rockets:
    plt.annotate(rock.name, xy=(rock.x, rock.y), xytext=((rock.x - 1), (rock.y + 1)))
for shut in shuttles:
    plt.annotate(shut.name, xy=(shut.x, shut.y), xytext=((shut.x - 1), (shut.y + 1)))
plt.show()

# Randomly moves each rocket and shuttle
for i in rockets:
    i.move(randint(-10, 10), randint(1, 50))
for i in shuttles:
    i.move(randint(-10, 10), randint(1, 50))

# Takes second snapshot of the locations of all rockets and shuttles, and prints the locations
print(' Check 2 '.center(60, '='))
print(' ')
for i in range(len(rockets)):
    rocketx[i] = rockets[i].x
    rockety[i] = rockets[i].y
    print('Rocket %s is at (%s, %s)' % (i, rockets[i].x, rockets[i].y))
print(' ')
# Randomly picks a shuttle to "return home" (testing the .home() method)
shuttles[randint(0, len(shuttles) - 1)].home()
for i in range(len(shuttles)):
    shuttlex[i] = shuttles[i].x
    shuttley[i] = shuttles[i].y
    if shuttles[i].flights == 1:
        print('Shuttle %s is at (%s, %s) and has completed %s flight.' %
              (i, shuttles[i].x, shuttles[i].y, shuttles[i].flights))
    elif shuttles[i].flights == 0:
        print('Shuttle %s is at (%s, %s) and hasn\'t completed any flights yet.' %
              (i, shuttles[i].x, shuttles[i].y,))
    else:
        print('Shuttle %s is at (%s, %s) and has completed %s flights.' %
              (i, shuttles[i].x, shuttles[i].y, shuttles[i].flights))


# Prompts user for name of rocket or shuttle, then prints the relative distance to every other rocket/shuttle.
# If user input isn't a valid rocket or shuttle name, asks user to try again or press ENTER to skip
found = False
while found is False:
    choice = input(
        '\nEnter name of rocket or shuttle (e.g. rocket 3, shuttle 1) or press ENTER to skip:  ')
    if choice == '':
        break
    for i in rockets:
        if choice.lower() in i.name.lower():
            for r in rockets:
                if i != r:
                    print('%s is %s units away from %s.' % (i.name, i.distance(r), r.name))
            print(' ')
            for s in shuttles:
                print('%s is %s units away from %s.' % (i.name, i.distance(s), s.name))
            found = True
    print(' ')
    for i in shuttles:
        if choice.lower() in i.name.lower():
            for r in rockets:
                print('%s is %s units away from %s.' % (i.name, i.distance(r), r.name))
            print(' ')
            for s in shuttles:
                if i != s:
                    print('%s is %s units away from %s.' % (i.name, i.distance(s), s.name))
            found = True
    if found is False:
        print('That\'s not a valid name. Please try again..')

# Plots the second snapshot on an xy graph
x = rocketx
y = rockety
plt.plot(x, y, 'ro')
sx = shuttlex
sy = shuttley
plt.plot(sx, sy, 'bo')
plt.xlabel('Horizontal distance from lauch point (ft)')
plt.ylabel('Altitude (ft)')
for rock in rockets:
    plt.annotate(rock.name, xy=(rock.x, rock.y), xytext=((rock.x - 1.5), (rock.y + 2)))
for shut in shuttles:
    plt.annotate(shut.name, xy=(shut.x, shut.y), xytext=((shut.x - 1.5), (shut.y + 2)))
plt.show()
