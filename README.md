**This is a sample pytest framework in automation some Github API Endpoints**

* **Install Requirements**
    1. pipenv --python 3.8.5
    2. pipenv shell
    3. pipenv install -r requirements.txt

* **Running the Tests**
* Running All Test
** pytest test_cases/
* Running Smoke Test Tag
**  pytest -m smoke
* Running Test with HTML report
** pytest --html=report.html --self-contained-html test_cases/