PySIS
=================

Project Home Page : http://bitbucket.org/dkmurthy/pysis

Student Information System, developed with Django and Python.
This software is still in development. Not yet ready for production use.

Available Modules:
===================

* Student Profiles
* Knowledge Base
* Institutional Repository (Work-in-progress)


Installation
===============

This software is developed with Django and Python, so technically it should run on all supported platforms. But I tested it only on Linux, specifically Ubuntu 10.04.

Prerequisites
------------------

* Python 2.6
* pip
* virtualenv
* nginx
* MySQL (optional)

Steps
-----------------

#. Install virtualenv and pip ::

    sudo apt-get install python-pip
    sudo pip install virtualenv

#. Create a new virtualenv ::

    virtualenv --no-site-packages pysis_env
    source pysis_env/bin/activate

#. Install requirements ::

    cd /path_to_pysis_project_src_root
    pip install -r requirements/requirements.txt

#. Add pysis to python path. Verify that this command won't throw any error ::

    >>> import pysis

