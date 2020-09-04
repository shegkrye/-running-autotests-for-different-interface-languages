from selenium.common.exceptions import NoSuchElementException  
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_checking_the_button(browser):
    browser.get(link)
    button=len(browser.find_elements_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    browser.implicitly_wait(10)
    assert button >0,'Нету кнопки'
    time.sleep(30)  

