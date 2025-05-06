#!/bin/bash

# Assuming you are in the root directory of your project
# Navigate to the directory where Serverless Offline stores its cache
cd .serverless

# Delete cached data
rm -rf .cache

# Go back to the root directory of your project
cd ..

# Now you can restart Serverless Offline with --reloadHandler option
serverless offline start --reloadHandler
