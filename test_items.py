import time

def test_add_book_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link) 
    # находим элемент и запоминаем его название
    element_name = browser.find_element_by_css_selector(".btn-add-to-basket").tag_name
    # проверяем кнопка ли это
    assert element_name == "button", '"Add to cart" button hasn\'t found'
    add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    add_button.click()
    time.sleep(30)

