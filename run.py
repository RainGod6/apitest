import os

os.system('pytest ./testcase -s -q --clean-alluredir=./report/allure_results')  # --clean清除历史数据
os.system('allure generate ./report/allure_results -o ./report/allure_html --clean')
os.system('allure serve ./report/allure_results')