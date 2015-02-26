#!/bin/sh
dpkg -s python-nautilus >/dev/null 2>&1 &&{
     echo "Python Nautilus found"
     echo "Checking for python-nautilus folders"

     if [ ! -d ~/.local/share/nautilus-python ]
     then
        mkdir ~/.local/share/nautilus-python;
     fi
    
     if [ ! -d ~/.local/share/nautilus-python/extensions ]
     then
          mkdir ~/.local/share/nautilus-python/extensions;
     fi
     
     echo "Copying files"     

     cp imdb.py ~/.local/share/nautilus-python/extensions
     cp MessageMaker.py ~/.local/share/nautilus-python/extensions
     cp movieRating.py ~/.local/share/nautilus-python/extensions
     cp notify.py ~/.local/share/nautilus-python/extensions

     echo "Restarting Nautilus"

     nautilus -q
     
     echo "Done"

   } ||{
    echo "Python-Nautilus not found. Please Install Python-Nautilus for using IMDB movie displayer"
   }
