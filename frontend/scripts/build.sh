#! /bin/bash

echo "I am going to move some files from the build folder to the static folder in the backend"
echo "Moving CSS"
cp build/static/css/main.*.css ../backend/reasonmljobs/static/frontend/css/main.css
echo "Moving JS"
cp build/static/js/main.*.js ../backend/reasonmljobs/static/frontend/js/main.js

echo "Exit"