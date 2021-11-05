from invoke import task
from cli import main


@task
def run(c):
    main()


@task
def test(c):
    c.run("pytest --cov=. *_tests.py")


@task
def black(c):
    """
    Runs The uncompromising Python code formatter on specific python files.
    """
    c.run("black *.py")
