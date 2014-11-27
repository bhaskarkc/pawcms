### 1. Install
```
virtualenv env # create a virtual environment
source env/bin/activate # Enter the virtual environment
git clone git@github.com:awecode/pawcms.git # git clone the repo
cd app # cd to project dir
pip install -r requirements/development.txt # install Python packages required for development
cp app/local_settings.sample.py app/local_settings.py # create local settings file from sample file
vi app/local_settings.py # configure your settings here, database, static & media paths and urls
./manage.py migrate # synchronize database and run migrations
./manage.py collectstatic # collect static files
```
