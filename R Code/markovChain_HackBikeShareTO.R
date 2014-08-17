markovChain_HackBikeShareTO <- function(rebal,stations,stationID,weekday,hour,tripLength){

## Load relavent packages into workspace
source("splitDateTime.R")
source("setFlags.R")
source("FindProbabilities.R")
source("createProbabilityMatrix.R")
source("PowerMatrix.R")
library(chron)
library(expm)

probabilities <- FindProbabilities(rebal,stationID,weekday,hour)

probMatrix <- createProbabilityMatrix(probabilities,stations[stations$Station.ID == stationID,"Total.Docks"])

powerMatrixFinal <- PowerMatrix(probMatrix,tripLength)

powerMatrixFinal
}
