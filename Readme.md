## Running

* First you should be on a current supported version of python, (I'm using 3.9.7). 
* Once this is installed, you need to create a virtalenv `python3 -m venv VENVNAMEHERE` and source activate it `source VENVNAMEHERE/bin/activate`.
* Once that's activated, `pip install -r requirements.txt`.
* Finally create a GitHub Personal Token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token  and set the appropriate environment variable. `export GITHUB_TOKEN=ghabcdeghijk1231412313`
* Then run `python cli.py` and presto! you can see all of someone's github repos!
