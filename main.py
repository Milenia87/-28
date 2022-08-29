from links import LabirintPage
from config import TestData
import time
import pytest


@pytest.mark.xfail
def test_loud_page(web_browser):
    page = LabirintPage(web_browser)
    page.wait_page_loaded()
    assert page.check_js_errors()


def test_go_to_main_page(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SALE_LINC.click()
    page.LOCATOR_LOGO_LABIRINT.click()
    assert page.get_current_url() == TestData.base_url



def test_visible_block_icons(web_browser):
    page = LabirintPage(web_browser)
    assert page.LOCATOR_BLOCK_ICONS.is_visible()


def test_scroll_page(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_HORROR)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATORS_PAGE_NUM_6.scroll_to_element()
    assert page.LOCATORS_PAGE_NUM_6.is_clickable()
    page.LOCATORS_PAGE_NUM_6.highlight_and_make_screenshot('scrolling.png')


def test_clic_icon_messages(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_MESSAGES.click()
    text = page.LOCATOR_AUTH_WINDOW.get_text()
    assert text == TestData.text_auth_window


def test_clic_icon_my_maze(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_MY_MAZE.click()
    text = page.LOCATOR_AUTH_WINDOW.get_text()
    assert text == TestData.text_auth_window


def test_clic_icon_postponed(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_POSTPONED.click()
    assert page.get_current_url() == TestData.postponed_url


def test_visible_up_navigation_panel(web_browser):
    page = LabirintPage(web_browser)
    assert page.LOCATOR_UP_NAVIGATION_PANEL.is_visible()


def test_delivery_and_payment_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_DELIVERY_AND_PAYMENT.click()
    assert page.get_current_url() == TestData.delivery_and_payment_url


def test_certificate_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_CERTIFICATE_LINC.click()
    assert page.get_current_url() == TestData.certificate_url


def test_certificate_availability(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_CERTIFICATE_LINC.click()
    page.LOCATORS_CERTIFICATE_TITLES.scroll_to_element()
    assert page.LOCATORS_CERTIFICATE_TITLES.count() == 8


def test_rating_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_RATING_LINC.click()
    assert page.get_current_url() == TestData.rating_url


def test_rating_book(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_RATING_LINC.click()
    assert page.LOCATORS_RATING_BOOK_TITLE.count() == 60

def test_news_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_NEWS_LINC.click()
    assert page.get_current_url() == TestData.news_url


def test_sale_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SALE_LINC.click()
    assert page.get_current_url() == TestData.sale_url


def test_phone_number_linc(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_PHONE_NUMBER_LINC.click()
    text = page.LOCATOR_PHONE_NUMBER_BTN.get_text()
    assert text == TestData.text_phone_number


def test_video_block(web_browser):
    page = LabirintPage(web_browser)
    text = page.LOCATOR_BLOCK_VIDEO.get_text()
    assert text == TestData.text_video_block


def test_photo_product(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_HORROR)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    assert page.LOCATORS_SEARCH_BOOK_TITLE.get_attribute('src') != ''


def test_search_product_adventure(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_HORROR)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    assert page.LOCATORS_SEARCH_BOOK_TITLE.count() == 720


def test_search_product_adventure_error(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_HORROR_ERROR)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    for title in page.LOCATORS_SEARCH_BOOK_TITLE.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Ужасы' or 'ужасы' in title(), msg


def test_add_book_in_cart(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATOR_BOOK_1.click()
    page.LOCATOR_BTN_ADD_TO_CART.click()
    page.LOCATOR_BTN_CART.click()
    assert page.LOCATOR_BOOK_1.is_visible()
    assert page.LOCATOR_COUNTER_CART.get_text() == '1'


@pytest.mark.xfail
def test_add_book_in_postponed(web_browser):
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATOR_BTN_POSTPONED.scroll_to_element()
    page.LOCATOR_BTN_POSTPONED.click()
    page.wait_page_loaded()
    page.LOCATOR_ICON_POSTPONED.scroll_to_element()