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

```--browser``` (default: chrome) option for choosing a browser. Can be Chrome or Firefox. (Chrome is default)

```--alluredir``` option for setting the folder for allure reports.

```--screenshot``` (default: off) used to open plugin. 

```--screenshot_path``` (default: off) off: The screenshot will not be saved and will only be attached to the allure report.
on: The screenshots will be saved to the “./screenshot/%Y-%m-%d/” directory in the root path of the project.

## Load test
To run the tests:
```
locust
```

```get_products_for_each_category``` GET-requests to products from each category

```get_categories``` GET-requests to for each category

## Test Automation - API
To run the tests:
```
pytest back_tests --alluredir=allure_result
```

Run options: 

```--alluredir``` option for setting the folder for allure reports.