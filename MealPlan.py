# This script asks the user for their netID and password.
# It then outputs the users remaining blocks and flex.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import getpass
import os
import sys


def main():
    # show/hide Chrome browser # don't commit
    if (True):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()
        driver.set_window_position(1300,20)

    # login urls
    url = "https://mybanner.msstate.edu/prod/wwskmeal.P_DispMealPlan"
    url2 = "https://mybanner.msstate.edu/prod/twbkwbis.P_ValLogin"
    driver.get(url)

    while(driver.current_url == url or driver.current_url == url2):
        # clear the command prompt
        clear = lambda: os.system('cls')
        clear()

        # login
        sid = input("username: ")
        driver.find_element_by_name('sid').send_keys(sid)
        pin = getpass.getpass("password: ")
        driver.find_element_by_name('PIN').send_keys(pin)
        driver.find_element_by_name('PIN').submit()

        # make sure passed login
        try:
            driver.find_element_by_name('KEYWRD_IN')
        except:
            print("Login Failed. Please Try Again.")
            sleep(2)


    # search 'meal plan' in search box
    driver.find_element_by_name('KEYWRD_IN').send_keys('meal plan') # can't find where 'View Your 
    driver.find_element_by_name('KEYWRD_IN').submit()               # Meal Plan' is in directory.
    # open View Your Meal Plan page
    driver.find_element_by_link_text('View Your Meal Plan').click()

    # select elements in table that contain remaining amounts
    blocks = driver.find_element_by_xpath("//table[@class='msu_table_wb']/tbody/tr[last()]/td[last()]")
    flex = driver.find_element_by_xpath("//table[@class='msu_table_wb'][2]/tbody/tr[last()]/td[last()]")

    # display results
    print("BLOCK MEALS REMAINING:\t" , blocks.text)
    print("FLEX DOLLARS REMAINING:\t", flex.text)

    # close webdriver
    # driver.close()

if __name__ == '__main__':
    main()
