import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

pi_directory = "C:/Users/Bruger/Documents/python/stuff/superligaResults.df"
teams = ["AaB", "AC Horsens", "AGF", "FC Nordsjaelland", "Lyngby", "Odense BK", "Silkeborg", "FC Copenhagen", "Viborg", "Brondby", "FC Midtjylland", "Randers FC"]

simulations = 10000

#with open(csvdirectory, newline='') as csvfile:
#    probabilities = list(csv.reader(csvfile))
probabilities = pd.read_pickle(pi_directory)
"""
for i in range(12):
	for j in range(12):
		if i == j:
			probabilities.loc[i, j] = None
		else:
			splitlist = probabilities.loc[i, j].split(",")
			probabilities.loc[i,j] = list(map(float,splitlist))"""


def simulateSeason():
	points = [0] * 12

	for homeIndex in range(12):
		for awayIndex in range(12):
			if homeIndex != awayIndex:
				x = random.random()
				home = probabilities.loc[homeIndex, awayIndex][0]
				even = probabilities.loc[homeIndex, awayIndex][1]
				away = probabilities.loc[homeIndex, awayIndex][2]

				if x < home: # Home team wins
					points[homeIndex] += 3
				elif x > home + even: # Away team wins
					points[awayIndex] += 3
				else: # Even
					points[homeIndex] += 1
					points[awayIndex] += 1

	return points

def mesterskabsspil(points):
	topsix = []

	extractpoints = list(points)
	for j in range(6):
		maxpoints = max(extractpoints)
		pos = extractpoints.index(maxpoints)
		topsix.append(pos)
		extractpoints[pos] = 0

	for homeIndex in topsix:
		for awayIndex in topsix:
			if homeIndex != awayIndex:
				home = probabilities.loc[homeIndex, awayIndex][0]
				even = probabilities.loc[homeIndex, awayIndex][1]
				away = probabilities.loc[homeIndex, awayIndex][2]

				x = random.random()

				if x < home: # Home team wins
					points[homeIndex] += 3
				elif x > home + even: # Away team wins
					points[awayIndex] += 3
				else: # Even
					points[homeIndex] += 1
					points[awayIndex] += 1
	return points


wins = [0] * 12
start = time.time()
lastUpdate = start + 1
for i in range(simulations):
	points = simulateSeason()
	points = mesterskabsspil(points)
	winpoints = max(points)
	wins[points.index(winpoints)] += 1


	procent = round((i + 1) / simulations * 100, 2)
	timeSpent = time.time() - start
	timeLeft = round(timeSpent * simulations / (i + 1) - timeSpent)

	if lastUpdate < time.time():
		lastUpdate = time.time() + 1
		print(f"{procent}% completed - {timeLeft} seconds left")

winprobability = np.array(wins) / simulations

#print(winprobability)

winprop = {}
for key in teams:
    for value in winprobability:
        winprop[key] = value


fig, ax = plt.subplots()
bars = ax.barh(teams, winprobability, color=["red", "yellow", "mistyrose", "orange", "blue", "steelblue", "skyblue", "lavender", "forestgreen", "yellow", "black", "navy"])
fig.subplots_adjust(left=0.25)
ax.bar_label(bars)
print("Task completed")
plt.show()
#["AaB", "AC Horsens", "AGF", "FC Nordsjaelland", "Lyngby", "Odense BK", "Silkeborg", "FC Copenhagen", "Viborg", "Brondby", "FC Midtjylland", "Randers FC"]