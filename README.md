**This is a sample pytest framework in automation some Github API Endpoints**

* **Generate your personal token in GitHub**
    * Add in your LOCAL ENV, or
    * Add token in settings.py file but do not commit

* **Install Requirements**
    * pipenv --python 3.8.5
    * pipenv shell
    * pipenv install -r requirements.txt

* **Running the Tests**
* Running All Test
** pytest test_cases/
* Running Smoke Test Tag
**  pytest -m smoke
* Running Test with HTML report
** pytest --html=report.html --self-contained-html test_cases/