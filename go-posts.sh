#1/bin/bash
#
#This Script replaces a string in one file with the contents of another file


# Set String to replace

string=@post

# Replace @post in template.html with the contents of cat-posts.html

sed -e "/$string/r cat-posts.html" -e "/$string/d" template.html
