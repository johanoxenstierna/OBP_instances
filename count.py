

"""Counts number of instances"""

import os

namesf = ['Conventional', 'NoObstacles', 'NR1', 'NR2', 'SingleRack', 'TwelveRacks']

N = 0
for namef in namesf:
    path = './' + namef + '/instances/'
    _, folders, _ = os.walk(path).__next__()
    N += len(folders)

print("There are " + str(N) + " instances.")