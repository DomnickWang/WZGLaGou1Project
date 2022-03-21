from selenium.webdriver.common.by import By

from test_selenium_homework2.page.base_page import BasePage
from test_selenium_homework2.page.contact_page import Contact


class AddMember(BasePage):
    _username = "username"

    def add_member(self):
        self.find(By.ID, 'username').send_keys("王子枫9")
        self.find(By.ID, 'memberAdd_acctid').send_keys("998877669")
        self.find(By.ID, 'memberAdd_biz_mail').send_keys("998877669")
        self.find(By.ID, 'memberAdd_phone').send_keys("18888886689")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return Contact(self.driver)

    def add_member_fail(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, self._username).send_keys("维恩2")
        self.find(By.ID, 'memberAdd_acctid').send_keys("998877669")
        self.find(By.ID, 'memberAdd_biz_mail').send_keys("998877669")
        self.find(By.ID, 'memberAdd_phone').send_keys("18888886689")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contact(self.driver)
