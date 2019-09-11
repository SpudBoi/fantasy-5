#Author: Conor Muldoon

library("tseries")
library("forecast")

#loading in database
database <- read.csv("C:\\Users\\ConMa\\Documents\\Projects\\fantasy-5\\fantasy5.csv")

#adding columns for each drawing's sum, odd count, range, and mean
database$sum <- database$num1 + database$num2 + database$num3 + database$num4 + database$num5
database$odd <- (database$num1 %% 2) + (database$num2 %% 2) + (database$num3 %% 2) + (database$num4 %% 2) + (database$num5 %% 2)
database$range <- database$num5 - database$num1
database$mean <- database$sum / 5