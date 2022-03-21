from selenium.webdriver.common.by import By

from test_selenium_homework2.page.base_page import BasePage
from test_selenium_homework2.page.contact_page import Contact


class AddMember(BasePage):
    _username = "username"
    _acctid = "memberAdd_acctid"
    _mail = "memberAdd_biz_mail"
    _phone = "memberAdd_phone"
    _save = ".js_btn_save"
    _cancel = ".js_btn_cancel"

    def add_member(self):
        self.find(By.ID, self._username).send_keys("王子涵1")
        self.find(By.ID, self._acctid).send_keys("998877671")
        self.find(By.ID, self._mail).send_keys("998877671")
        self.find(By.ID, self._phone).send_keys("18888886671")
        self.find(By.CSS_SELECTOR, self._save).click()
        return Contact(self.driver)

    def add_member_fail(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, self._username).send_keys("维恩2")
        self.find(By.ID, self._acctid).send_keys("998877669")
        self.find(By.ID, self._mail).send_keys("998877669")
        self.find(By.ID, self._phone).send_keys("18888886689")
        self.find(By.CSS_SELECTOR, self._save).click()
        self.find(By.CSS_SELECTOR, self._cancel).click()
        return Contact(self.driver)
