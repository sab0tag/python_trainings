# -*- coding: utf-8 -*-
"""
Задание №1: Подготовить инфраструктуру и создать первый работающий тест
Повторить действия, которые были продемонстрированы в лекциях:

Создать новый репозиторий на GitHub и клонировать его на локальную машину.
Создать новый проект в среде разработки PyCharm.
Записать в рекордере сценарий для создания новой группы в адресной книге.
Перевести сценарий на язык Python и перенести его в среду разработки.
В этот момент можно уложить промежуточные результаты работы в репозиторий.
Создать виртуальное окружение (virtualenv) и установить в него дополнительные библиотеки selenium и pytest.
Настроить проект в среде разработки на использование созданного виртуального окружения.
Настроить среду разработки на использование тестового фреймворка py.test.
Загрузить и установить вспомогательный исполняемый файл geckodriver.
Убедиться в том, что созданный тест успешно выполняется как из консоли, так и из среды разработки.
И снова можно уложить результаты работы в репозиторий. Делайте это после каждого успешного шага.
А если что-то сломалось -- можно отменить изменения, вернуться к предыдущему работающему состоянию, и попробовать ещё раз.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost:8080/addressbook/index.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_id("container").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("newGroup")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("some description")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("some description2")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
