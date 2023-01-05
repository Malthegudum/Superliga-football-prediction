# Superliga football prediction
This is my attempt at predicting the results of the Danish Superliga, which is the Danish football championship.

It was done by finding the difference in xG for every match the current and last two seasons fo the Superliga. This was found on https://footballxg.com/xg-league-tables/. Then I found a rating of every club in the Superliga on https://footballdatabase.com/ranking/denmark/1 and then found the difference in rating of the two teams for each match. Then I plotted the difference in rating on the x-axis and difference in xG on the y-axis and did linear regression on it:

![image](https://user-images.githubusercontent.com/82721293/210566912-8a6621f8-8a67-4fad-983c-d100a52d3b65.png)

This gave me the formula, ΔxG = 0.00315 * Δrating + 0.20276. The standard deviation was 1.05645.

I assumed that real xG difference followed a normal distribution where the mean is the formula and the standard deviation is 1.05645. The away team wins if the ΔxG is under -0.5, it's a draw if the ΔxG is between -0.5 and 0.5 and the home team wins if it's above 0.5.
The probability of those scenarios is the area under the normal distribution for those values.
![image](https://user-images.githubusercontent.com/82721293/210573836-b5de9ed0-8e2b-4c1c-abbf-f1f8f6de5672.png)

In match-probabilities.py a data frame is created with probabilities for all matches in the league.

In superliga-sim.py the league is simulated 10000 times using the probabilities from the data frame. The probability of a team becoming champions is the number of times a team won the league in the simulations divided by 10000.

This is the results:
![image](https://user-images.githubusercontent.com/82721293/210575757-a9c6acc5-b5c3-447d-8fb4-ec04efef2379.png)

It predicts that FC Copenhagen will become Danish champions again with a 52% chance. FC Midtjylland is also quite likely to win with a chance of 44%.
It's important to note that the program does not use the current points in Superligaen, but instead acts like no matches has been played. This is why FC Nordsjælland and Viborg have far lower chances of winning than FC Copenhagen and FC Midjylland even though they both have more points in the real Superliga.
