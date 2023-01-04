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

csvdirectory = "C:/Users/Bruger/Documents/python/stuff/superligaResults.csv"
pi_directory = "C:/Users/Bruger/Documents/python/stuff/superligaResults.df"

#probabilityTable = [[0] * 12] * 12

probabilityTable = pd.DataFrame("X", index=range(12), columns=range(12))

for homeIndex in range(12):
	for awayIndex in range(12):
		if homeIndex != awayIndex:
			xG = xGMean(ratings[homeIndex], ratings[awayIndex])
			HT, X, AT = homeEvenAwayProbability(xG)
			print(HT, X, AT, homeIndex, awayIndex)
			probabilityTable.loc[homeIndex, awayIndex] = [HT, X, AT] #f"{HT},{X},{AT}"
			#probabilityTable[homeIndex][awayIndex] = f"{HT},{X},{AT}"

print(probabilityTable)

probabilityTable.to_pickle(pi_directory)

"""
with open(csvdirectory,"w") as my_csv:
    csvWriter = csv.writer(my_csv)
    csvWriter.writerows(probabilityTable)





if __name__ == "__main__":
	xG = xGMean(ratings[2], ratings[7])

	HT, X, AT = homeEvenAwayProbability(xG)

	print(xG)
	print(HT, X, AT)
"""