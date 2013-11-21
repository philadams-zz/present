from fabric.api import local

def register():
    """register project on pypi"""
    local('python setup.py register')

def prepare():
    """prepare project for pypi"""
    local('python setup.py sdist')

def distribute():
    """distribute project on pypi"""
    local('python setup.py sdist upload')
