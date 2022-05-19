## InsTestTask

### Before launch
```
brew install --cask chromedriver
```
```
brew install geckodriver
```
```
brew install allure
```
```
brew install locust
```
```
pip install -r requirements.txt
```

### To create report
```
allure serve allure_result   
```
## Test Automation
To run the tests:
```
pytest front_tests --browser={chrome/firefox} --alluredir=allure_result --screenshot=on --screenshot_path={on/off}
```

Run options: 

```--browser``` (default: firefox) option for choosing a browser. Can be Chrome or Firefox. (Chrome is default)

```--alluredir``` option for setting the folder for allure reports.

```--screenshot``` (default: off) used to open plugin. 

```--screenshot_path``` (default: off) off: The screenshot will not be saved and will only be attached to the allure report.
on: The screenshots will be saved to the “./screenshot/%Y-%m-%d/” directory in the root path of the project.

## Load test
To run the tests:
```
locust -f load_tests/locustfile.py --headless --users 10 --spawn-rate 1 -H https://www.n11.com
```

```get_base_page``` GET-request to base page with checking title in response

```get_search_request``` GET-requests to search result pages

```get_products_from_results``` GET-requests to product pages from search result

## Test Automation - API
To run the tests:
```
pytest back_tests --alluredir=allure_result
```

Run options: 

```--alluredir``` option for setting the folder for allure reports.