import os

import invoke

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)


@invoke.task
def deps(c):
    """Install Packaging Dependencies"""
    c.run('python3 -m pip install --user --upgrade setuptools twine wheel build')


@invoke.task
def gen_dist(c):
    """Generate distribution archives"""
    c.run('python3 build')


@invoke.task
def upload(c, repo='testpypi'):
    """Upload distribution archives"""
    c.run('python3 -m twine upload --repository {} dist/*'.format(repo))

