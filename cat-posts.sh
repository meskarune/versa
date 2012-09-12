#!/bin/bash
#
#This Script Concatenates the 15 most recent posts in /archive into
#cat-posts.html

#Find the 15 most recent posts

ls -lart /archives | tail -n 15

posts=

for posts in list
do
	cat "$(posts)" >> cat-posts.html
done
