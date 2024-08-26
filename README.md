- Name - Pramod
- Author - Pramod

### Web Automation Framework with POM in Python(Selenium)

- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.


### Folder Structure

<img width="944" alt="Screenshot 2023-08-28 at 5 28 26 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/629dd569-5a7f-4293-a821-7af6f97786cc">

### CI/CD Run

<img width="1199" alt="Screenshot 2023-08-28 at 5 28 46 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/b339baf7-ae46-4188-b285-bfb88862f752">

### All the dependencies used 
```
- pip install allure-pytest selenium
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal
- pip install python-dotenv
```

### Install all in the one Go
```python
pip install allure-pytest selenium pytest openpyxl faker pytest-xdist pytest-html
```


#### How to run the Framework?
```pytest -n auto tests/vwoLoginTests/pom/test_*```

#### How to run Testcase parallel ?

``` pytest -n auto tests/test/vwoLoginTests/test_vwo_login.py```

#### How to run a Single TestClass
```pytest tests/test/vwoLoginTests/test_vwo_login_pf.py```

#### How to run All Testcase parallel ?

```pytest -n auto tests/test/vwoLoginTests/test_*```


pip install -r requirements.txt