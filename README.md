![GitHub last commit](https://img.shields.io/github/last-commit/StephanoGit/UniHack-2021) ![GitHub repo size](https://img.shields.io/github/repo-size/StephanoGit/UniHack-2021)
# GreatUniHack 2021 - Booking. com Challenge 

We were challenged by Booking.com to develop in a 24-hour timeframe a website for car rental customers that estimates the time taken to arrive at the car rental depot after landing. The output is generated using a machine learning model that we trained in the given timeframe.


## Table of Contents
1. Algorithm and training model
2. Datasets Used
3. Parameters Chosen
4. Results
5. Website Implementation
6. Additional Features


## Algorithm and training model
The training of the model was done using the Random Forest Classification method because of the high accuracy that it provides through cross validation. 
Random forest, like its name implies, consists of many individual decision trees. Each individual tree in the random forest spits out a class prediction, and the class with the most votes becomes our model’s prediction.
We have decided to use 10 trees for our use as we observed that an increase would not make a difference in the accuracy of the results.

## Datasets Used
The model has been trained on two datasets like the one below:

![Corpus](https://github.com/StephanoGit/UniHack-2021/blob/master/other%20files/corpus.png)

A third one was used for extracting the names of airports determined by the given coordinates.

## Parameters Chosen
We choose out parameters carefully in order to optimize as much as possible our model. This was done by generating a correlation heatmap based on the 2 corpuses given.

![HeatmapLarge](https://github.com/StephanoGit/UniHack-2021/blob/master/other%20files/heatmap_large.png)

We discovered that most of the, do not influence the “Time Taken” one, so we condensed the map into an easier to understand one.

![HeatmapSmall](https://github.com/StephanoGit/UniHack-2021/blob/master/other%20files/heatmap_small.png)

Given the corpus, we discovered that Haul cannot be part of our parameters because we wouldn’t know if a flight is long or not just based on simple coordinates. Assuming this, we decided to make our own, “Travel Distance” by calculating the distance between destination and departure coordinates.

## Results
Considering all the decisions we have taken along the way, we managed to train a model with the following results:

![Results](https://github.com/StephanoGit/UniHack-2021/blob/master/other%20files/results.png)

## Website Implementation
The site has been completely remade by me, because the one we sent was not fully developed and not user friendly. I have used Python Flask to connect the back end with the frontend.

## Additional Features
During the competition I started to work on a QR scanner. Because most of the plane tickets have one, we wanted to ease the usability for the user. The scan would generate the expected “Time taken” in the web application. This feature is still in progress.

![QRscanner](https://github.com/StephanoGit/UniHack-2021/blob/master/other%20files/scanner_demonstration.png)

## Future Improvements
-	Other Airports datasets (we were given only 8)
-	More relevant parameters
-	Full implementation of the scanner
-	Suggestions of nearby attractions or accommodations for tourists
-	Explicit directions on how to exit the airports.




