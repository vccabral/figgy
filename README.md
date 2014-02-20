# figgy

figgy is sample code for interviews that relates to some of the code in our content management system.


# Python
 
## Mac Setup

### System dependencies

Assuming you're on a Mac, follow the steps below. If you're not, you're on your own.

Start by making sure you have these packages from Homebrew (`brew install` them but really closely
follow the Homebrew docs, *especially* for the databses):

* (None, yet)

Also do:

* virtualenv (`sudo easy_install virtualenv`)

### Very first time

This setup assumes you have just cloned the git repo and are in the directory with this `README.md`.

    $ virtualenv ve --python=python2.7 --prompt="(figgy)"  # Get a set of eggs just for this
    $ . ve/bin/activate                                    # Turn on the virtualenv
    $ python setup.py develop --always-unzip               # Fill the virtualenv with Python dependencies
    $ cp figgy/local.py.example figgy/local.py             # Your local.py is your personal settings. Edit them later.
    $ python manage.py syncdb --noinput                    # Fill out the database schema
    $ python manage.py createsuperuser                     # Establish an admin so you can log in
    $ python manage.py runserver                           # Prove this works by visiting http://localhost:8000

Before you write any code, make sure you can run the tests and get them to pass 100%.

### Every time

When you come back to work after a day or more, you'll need to update your git checkout, and make
sure you have any new dependencies or schema modifications:

    $ . ve/bin/activate                           # Turn on the virtualenv (Every time!)
    $ python setup.py develop --always-unzip      # Update the virtualenv with new Python dependencies
    $ python manage.py syncdb --noinput           # Make sure the database schema is still filled out
    $ python manage.py runserver                  # Prove this works by visiting http://localhost:8000

tc.

## Tests

The tests for this project are managed by `tox`, a Python package.
First, install `tox` via `easy_install` (or `pip`).

Prior to running tox, be sure to create a `figgy/_local_tests.py` file by copying
`figgy/_local_tests.py.example` to `figgy/_local_tests.py`.  Any modifications to the test settings
should be performed in the developer's `_local_test.py`.

To run the tests:

    tox

The first run will take a while as it builds a virtualenv and installs everything in it, subsequent
ones will be much faster.  To rebuild the virtualenv later with updated dependencies:

    tox -r

You normally shouldn't need to recreate the tox virtualenv, since it updates itself on each run,
but it might be necessary in cases of version conflicts.


## Importing test data
Import the initial set of test data.

````
$ python manage.py process_data_file data/initial/*.xml
````

Importing the update data may be a little tricky. But you can also try it by running:

````
$ python manage.py process_data_file data/update/*.xml
````

