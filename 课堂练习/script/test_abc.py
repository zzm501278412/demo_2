import pytest
from time import sleep
def test_baidu(driver):
    driver.get("localhost:8080/jenkins")
    sleep(5)

if __name__ == '__main__':
    pytest.main()