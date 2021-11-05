from invoke import task
from cli import main


@task
def run(c):
    main()


@task
def test(c):
    c.run("pytest --cov=. *_tests.py")


@task(pre=[test])
def coverage(c):
    c.run("coverage html")
    c.run("xdg-open coverage_html_report/index.html")


@task
def black(c):
    """
    Runs The uncompromising Python code formatter on specific python files.
    """
    c.run("black *.py")
