#!/bin/bash

log_file="logs/download_data.log"

# Download data from Kaggle
echo "$(date '+%Y-%m-%d %H:%M:%S') - Downloading data from Kaggle..." >> $log_file
kaggle datasets download -d himanshupoddar/zomato-bangalore-restaurants

# Move data from utils folder to data/external folder
echo "$(date '+%Y-%m-%d %H:%M:%S') - Moving data to data/external folder..." >> $log_file
mv zomato-bangalore-restaurants.zip data/external/

# Unzip data from data/external folder to raw folder
echo "$(date '+%Y-%m-%d %H:%M:%S') - Unzipping data to data/raw folder..."
unzip data/external/zomato-bangalore-restaurants.zip -d data/raw/