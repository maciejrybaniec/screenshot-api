from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import logging


def capture_screenshot(url, html_element_id, filename):
    try:
        browser = webdriver.Chrome()

        logging.info('access page url', url)
        browser.get(url)
        sleep(1)

        try:
            element = browser.find_element_by_id(html_element_id)
            element.screenshot(filename)
        except NoSuchElementException:
            logging.error('cannot find html element on page')
            raise Exception('No element')

    except Exception as exception:
        logging.info('cannot capture screenshoot', str(exception))
    finally:
        browser.quit()
