import time
import allure

import pytest
from allure_commons.types import AttachmentType

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    @allure.feature('Open pages')
    @allure.story('Open "petrovich" pages')
    @allure.severity('trivial')
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_result = homepage_nav.get_nav_links_text()
        expected_result = homepage_nav.NAV_LINK_TEXT
        print(actual_result)
        num = 9 #Количество элементов
        for indx in range(num):
            with allure.step('Make screenshot'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=
                AttachmentType.PNG)
            homepage_nav.get_nav_links()[indx].click()
            time.sleep(1)
            #homepage_nav.driver.delete_all_cookies()
            assert actual_result == expected_result






