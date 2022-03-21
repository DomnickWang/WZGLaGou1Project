from test_selenium_homework2.page.main_page import MainPage


class TestAddMember():
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # 1. 点击添加成员,跳转到添加成员页面 2.填写成员信息 3. 点击保存
        # 4. 断言是否添加成功
        assert "王子涵1" in self.main.goto_add_member().add_member().get_member()

    def test_add_membet_fail(self):
        assert "维恩2" not in self.main.goto_add_member().add_member_fail().get_member()

    def test_delete_member(self):
        self.main.goto_contact().delete_member()

    def teardown(self):
        self.main.quit()
