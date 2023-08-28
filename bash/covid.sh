#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
INICUCURRENTLY=$(echo $DATA | jq '.[0].inIcuCurrently')
DEATH=$(echo $DATA | jq '.[0].death')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $INICUCURRENTLY people in the ICU, $DEATH total COVID deaths, with an increase of $DEATHINCREASE over the past 24 hours. "

