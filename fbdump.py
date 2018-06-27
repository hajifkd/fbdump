import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    url = 'https://www.facebook.com/'
    email = input('Email: ')
    password = getpass.getpass()

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    driver.set_window_size(1920, 1080)
    driver.get(url)

    driver.save_screenshot('hoge.png')


if __name__ == '__main__':
    main()
