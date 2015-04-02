## About

Versa is a flat file based content management system built with flask. You can
save pages and posts as markdown files on your server and the CMS will display
them. The code for this project is based off
[kukkaisvoima](https://github.com/Petteri/kukkaisvoima) a python/cgi blog
application with a nice set of features.

### Installation

You will need python 2 and python virtualenv installed on your computer.

Create the blog web directory and flask directory

    mkdir -p /srv/http/blog/flask

Download Versa and unzip the file to /srv/http/blog/

    wget  https://github.com/meskarune/versa
    unzip versa.zip

create virtual enviroment

    virutalenv2 /srv/http/blog/flask

Activate the virtual enviroment you created

    source /srv/http/blog/flask/bin/activate

Install the application dependances

    pip install -r /srv/http/blog/app/requirements.txt

