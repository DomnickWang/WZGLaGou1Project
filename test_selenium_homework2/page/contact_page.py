from selenium.webdriver.common.by import By

from test_selenium_homework2.page.add_member_page import AddMember
from test_selenium_homework2.page.base_page import BasePage


class Contact(BasePage):
    # def add_member(self):
    #     self.find(By.ID, 'add_member').click()
    #     return AddMember(self.driver)

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR,
                              ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(2)")
        name_list = [element.get_attribute("title") for element in elements]
        print(name_list)

        return name_list

    # def delete_member(self):
    #     # 获取电话号码列表
    #     elements = self.finds(By.CSS_SELECTOR,
    #                           ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(5)")
    #     for element in elements:
    #         if element.get_attribute("title") == "18888886681":
    #             self.find(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)").click()
    #             self.find(By.CSS_SELECTOR, "js_delete").click()
    #             self.driver.switch_to.alert.accept()
    #             self.driver.switch_to.default_content()
    #             self.driver.refresh()
    #         else:
    #             pass
    #     self.get_member()
