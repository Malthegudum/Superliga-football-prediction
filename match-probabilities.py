from scipy.stats import norm
import csv
import pandas as pd

def xGMean(hometeamRating, awayteamRating):
	ratingDifference = hometeamRating - awayteamRating
	xGMeanDifference = slope * ratingDifference + yIntercept
	return xGMeanDifference

def homeEvenAwayProbability(xGMeanDifference):
	awayProbability = norm.cdf(-0.5, xGMeanDifference, standartDeviation)
	evenProbability = norm.cdf(0.5, xGMeanDifference, standartDeviation) - awayProbability
	homeProbability = 1 - awayProbability - evenProbability
	return homeProbability, evenProbability, awayProbability

teams = ["AaB", "AC Horsens", "AGF", "FC Nordsjaelland", "Lyngby", "Odense BK", "Silkeborg", "FC Copenhagen", "Viborg", "Brondby", "FC Midtjylland", "Randers FC", "Vejle", "Sonderjyske"]
ratings = [1353, 1278, 1374, 1420, 1223, 1360, 1354, 1568, 1382, 1426, 1561, 1374, 1267, 1272]

slope = 0.00315
yIntercept = 0.20276
standartDeviation = 1.05645

pi_directory = "./superligaResults.df"


probabilityTable = pd.DataFrame("X", index=range(12), columns=range(12))

for homeIndex in range(12):
	for awayIndex in range(12):
		if homeIndex != awayIndex:
			xG = xGMean(ratings[homeIndex], ratings[awayIndex])
			HT, X, AT = homeEvenAwayProbability(xG)
			print(HT, X, AT, homeIndex, awayIndex)
			probabilityTable.loc[homeIndex, awayIndex] = [HT, X, AT]

print(probabilityTable)

probabilityTable.to_pickle(pi_directory)
