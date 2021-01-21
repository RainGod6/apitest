import os

os.system('pytest ./testcase -s -q --alluredir=./report/allure_results')
os.system('allure generate ./report/allure_results -o ./report/allure_html --clean')
os.system('allure serve ./report/allure_results')