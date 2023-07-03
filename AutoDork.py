############################################
#                                          #
#       To-do:                             #
#           Screenshots folder             #
#           If no results don't screenshot #
#           Proxies                        #
#           Threading                      #
#                                          #
#                                          #
############################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import argparse

def AutoDork(filename):

    domain_parser = argparse.ArgumentParser(description="Usage: python3 AutoDork.py google.com")

    domain_parser.add_argument('domain', metavar='exampledomain.com', help='Domain to be dorked')
    
    args = domain_parser.parse_args()
    domain = args.domain

    print(domain)

    iteration = 0

    filename = open(filename, 'r')
    for line in filename:
        dork = line.replace("`domain`", f"{domain}")
        print(dork)

        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(f'https://www.google.com/search?q={dork}')
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(1920,S('Height'))
        driver.find_element(By.TAG_NAME, 'body').screenshot(f'screenshot' + f'{iteration}.png')

        iteration += 1

    filename.close()
    driver.quit()

AutoDork("dorks.txt")
