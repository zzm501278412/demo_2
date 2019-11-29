from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import random

from time import sleep

"""
对selenium做二次封装
打开浏览器
打开地址
元素定位
元素操作
"""

url = "http://172.16.1.204/ecshop/"
admin_url2 = 'http://172.16.1.204/ecshop/admin'
login_url = 'http://172.16.1.204/ecshop/user.php'


def open_browser(browser='chrome'):
    """

    :param browser: 浏览器名称
    :param url:
    :return: driver
    """
    driver = None
    if browser == "firfox":
        driver = webdriver.Firefox()

    elif browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'IE':
        driver = webdriver.Ie()

    else:
        print("请输入正确的浏览器")
    return driver


class Base:
    def __init__(self, driver):
        """
        初始化driver
        """
        self.driver = driver

    def open_url(self, url):
        # 浏览器输入网址
        self.driver.maximize_window()
        self.driver.get(url)

    def back(self):
        """
        后退
        :return:
        """
        self.driver.back()

    def find_element(self, locator):
        """
        定位单个元素,如果定位成功,返回元素本身,如果失败返回False
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"{locator[0]}元素没找到")
            return False

    def find_elements(self, locator):
        """
        定位一组元素,如果定位成功,返回元素本身,如果失败返回False
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f"{locator[0]}元素没找到")
            return False

    def click(self, locator):
        # 点击元素
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        # 输入内容
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        # 关闭浏览器
        self.driver.close()

    def is_text_inelement(self, locator, text, timeout=5):
        """
        判断文本是是否存在元素中
        :param locator:定位器
        :param test:验证文本
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            print('元素未找到或文本')
            return False

    def switch_iframe(self, locator):

        # 进入frame
        self.driver.switch_to.frame(locator)

    def select(self, locator, text):
        # 下拉菜单选择
        element = self.find_element(locator)
        selectA = Select(element)
        selectA.select_by_visible_text(text)

    def alert(self):
        # 获取弹窗文本
        a = self.driver.switch_to.alert
        return a.text

    def alert_accept(self):
        # 解散弹窗
        a = self.driver.switch_to.alert
        a.accept()

    def alert_back(self):
        # 退出frame
        self.driver.switch_to.parent_frame()

    def js(self, js):
        # 去除JS
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def is_lists(self, locator):
        # 操作多选框
        cars = self.find_elements(locator)
        for i in cars:
            if i.is_selected():
                pass
            else:
                i.click()

    def is_list(self, locator):
        apple = self.find_element(locator)
        # 操作单选框
        if apple.is_selected():  # 判断单选框是否被选中
            pass
        else:
            apple.click()

    def drop_down(self, locator):
        '''
        下拉框
        :return:
        '''
        # provinces = self.find_elements(locator_1)
        # index = random.randint(1,len(provinces)-1)
        # selectA = self.find_element(locator)
        # Select(selectA).select_by_index(index)
        select = self.find_element(locator)  # 获取父元素select
        options = select.find_elements_by_css_selector("option")  # 通过父元素定位一组子元素
        index = random.randint(1, len(options) - 1)  # 使用随机方法，选择索引值
        Select(select).select_by_index(index)  # 通过索引操作下拉框

        # 键盘 enter 回车事件

    def keyboard_envent_enter(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    def backspace(self, locator):

        element = self.find_element(locator)
        element.send_keys(Keys.BACKSPACE)

    def drop_single(self, locator):
        """
        单选框
        :param locator:
        :return:
        """
        elements = self.find_elements(locator)
        for i in elements:
            if i.is_selected():
                pass
            else:
                i.click()

    def click_show_goods(self, locator, locator1, locator2):
        paginations = len(self.find_elements(locator1))  # 总页数
        for pagination in range(1, paginations + 1):  # 遍历页数页数
            if pagination == paginations:  # 判断是否为最后一页
                goods = len(self.find_elements(locator))  # 商品
                for only_goods in range(goods):
                    self.find_element(
                        ('xpath', '//*[@id="compareForm"]/div/div/div[' + str(only_goods + 1) + ']/a[1]/img')).click()
                    sleep(1)
                    self.back()
                    sleep(1)
                break

            else:
                goods = len(self.find_elements(locator))  # 商品
                for only_goods in range(goods):
                    self.find_element(
                        ('xpath', '//*[@id="compareForm"]/div/div/div[' + str(only_goods + 1) + ']/a[1]/img')).click()
                    sleep(1)
                    self.back()
                    sleep(1)
                self.find_element(locator2).click()

    def choose(self, locator):
        """
        选择下拉框问题
        :param locator:
        :return:
        """
        select = self.find_element(locator)  # 获取父元素select
        options = select.find_elements_by_css_selector("option")  # 通过父元素定位一组子元素
        index = random.randint(1, len(options) - 1)  # 使用随机方法，选择索引值
        Select(select).select_by_index(index)  # 通过索引操作下拉框

    def redio_is_selectde(self, locator):
        """
        判断单选框是否被选中
        :return:
        """
        element = self.find_element(locator)
        if element.is_selected():
            pass
        else:
            element.click()


if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    base.open_url('http://172.16.1.244/ecshop/user.php')
    # username = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[1]/td[2]/input')
    # password = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[2]/td[2]/input')
    # queding = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]')
    # base.send_keys(username, "zzm6226")
    # base.send_keys(password, 'zzm6226')
    # base.click(('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]'))
    # print(base.is_text_inelement(('class name', 'f4_b'), 'zzm6226'))
    base.alert()
