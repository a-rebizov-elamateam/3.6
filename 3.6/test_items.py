

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
