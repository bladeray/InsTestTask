# InsTestTask

## Before launch
```
brew install --cask chromedriver
```
```
brew install geckodriver
```
```
brew install allure
```
## Test Automation
For launch:
```
pytest front_tests --browser=firefox --alluredir=allure_result --screenshot=on 
```

Options: 

```--browser``` - option for choosing a browser. Can be Chrome or Firefox. (Chrome is default)

```--alluredir``` - option for setting the folder for allure reports.

```--screenshot``` - option for saving a screenshot in allure reports on failures.

## Load test
For launch:
```
locust
```

```get_products_for_each_category``` - GET-requests to products from each category
```get_categories``` - GET-requests to for each category

## Test Automation - API
For launch:
```
pytest back_tests
```