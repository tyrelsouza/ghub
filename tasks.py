from invoke import task

@task
def test(c):
    c.run("pytest tests.py --pdb")

@task
def black(c):
    """
    Runs The uncompromising Python code formatter on specific python files.
    """
    c.run("black *.py")
