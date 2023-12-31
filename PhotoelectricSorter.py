# This is a sample Python script.
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from colour import Color

import utils

# These variables are inputted from the command line
temp = 0  # Temperature (in kelvin)
wavelength = 0  # Wavelength (in meters)

# Their original values have no meaning, I'm just not good enough with python to not init them.

WF_database1 = pd.read_csv('WF_database_29270_part1.csv')
WF_database2 = pd.read_csv('WF_database_29270_part2.csv')

# TODO: Make it so that we can actually combine the two databases in a clean way.
#  (where the graphs don't look unreadable.)

# IMPORTANT CHANGE THIS IF YOU WANT TO SWITCH INPUTS.

WF_database = WF_database2

aluminums, aluminumsH, aluminumsErr = [], [], []
zincs, zincsH, zincsErr = [], [], []
magnesiums, magnesiumsH, magnesiumsErr = [], [], []
silicons, siliconsH, siliconsErr = [], [], []
titaniums, titaniumsH, titaniumsErr = [], [], []
savedMatNameAl, numAluminums = '', 1
savedMatNameZn, numZincs = '', 1
savedMatNameMn, numMagnesiums = '', 1
savedMatNameSi, numSilicons = '', 1
savedMatNameTi, numTitaniums = '', 1
wf = 0  # work function
matName = 'AlCl'  # name of the material

print(len(WF_database.columns))
print(WF_database.size / len(WF_database.columns))

for row in WF_database.itertuples(index=False):
    matName = row.surface_elements_string
    if "Al" in matName:
        utils.duplicate_averager(aluminums, aluminumsH, matName, row, savedMatNameAl, numAluminums)
        utils.multiple_sort(aluminumsH, [aluminumsH, aluminums])
        # utils.duplicate_stderr(aluminums, aluminumsH, aluminumsErr, matName, row, savedMatNameAl, numAluminums)
    if "Zn" in matName:
        utils.duplicate_averager(zincs, zincsH, matName, row, savedMatNameZn, numZincs)
        utils.multiple_sort(zincsH, [zincsH, zincs])
    if "Mn" in matName:
        utils.duplicate_averager(magnesiums, magnesiumsH, matName, row, savedMatNameMn, numMagnesiums)
        utils.multiple_sort(magnesiumsH, [magnesiumsH, magnesiums])
    if "Si" in matName:
        utils.duplicate_averager(silicons, siliconsH, matName, row, savedMatNameSi, numSilicons)
        utils.multiple_sort(siliconsH, [siliconsH, silicons])
    if "Ti" in matName:
        utils.duplicate_averager(titaniums, titaniumsH, matName, row, savedMatNameTi, numTitaniums)
        utils.multiple_sort(titaniumsH, [titaniumsH, titaniums])

# BELOW IS THE SECTION FOR SHOWING THE GRAPHS
# TODO: MAKE IT LOOK BETTER

# gray = Color("#a2b1ae")  # defining gray
# colors = list(gray.range_to(Color("#010101"), aluminums.__len__()))  # Color is a gradient from gray to white
# for i, color in enumerate(colors):  # make colors a list of strings
#     colors[i] = color.hex

alX = (range(len(aluminums)))
alX = [2 * i for i in alX]
fig, al = plt.subplots(figsize=(20, 15))
al.bar(alX, aluminumsH, label=aluminums, color=(0, 0, 0, 1))
plt.xticks(alX, aluminums, rotation='vertical')
plt.yticks(fontsize=20)
al.set_ylabel('Work Function', fontsize=50)
al.set_title('Aluminum compounds and their work functions', fontsize=50)
plt.show()

fig, zn = plt.subplots()
zn.bar(zincs, zincsH, label=zincs, color=(0, 0, 0, 1), align='edge', width=.6)
plt.xticks(rotation='vertical', fontsize=5)
zn.set_ylabel('Work Function')
zn.set_title('Zinc compounds and their work functions')
plt.show()

fig, mn = plt.subplots()
mn.bar(magnesiums, magnesiumsH, label=magnesiums, color=(0, 0, 0, 1), width=.6)
plt.xticks(rotation='vertical', fontsize=5)
mn.set_ylabel('Work Function')
mn.set_title('Magnesium compounds and their work functions')
plt.show()

fig, si = plt.subplots(figsize=(20, 15))
siX = (range(len(silicons)))
siX = [2 * i for i in siX]
si.bar(siX, siliconsH, label=silicons, color=(0, 0, 0, 1))
plt.xticks(siX, silicons, rotation='vertical')
plt.yticks(fontsize=20)
si.set_ylabel('Work Function', fontsize=50)
si.set_title('Silicon compounds and their work functions', fontsize=50)
plt.show()

fig, ti = plt.subplots()
ti.bar(titaniums, titaniumsH, label=titaniums, color=(0, 0, 0, 1), width=.6)
plt.xticks(rotation='vertical', fontsize=5)
ti.set_ylabel('Work Function')
ti.set_title('Titanium compounds and their work functions')
plt.show()

