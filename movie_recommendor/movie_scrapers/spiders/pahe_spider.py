from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaheSelenium:
    def __init__(self, name, release_date):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        search_string = "{} {}".format(name, release_date)
        search_string = search_string.replace(' ','+')
        url ='https://pahe.li/?s='+search_string
        self.parse(url)

        
    def navigateInterSites(self, site):
        self.driver.get(site)
        first_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//div[@class = "wait"]/center/img[@id = "soralink-human-verif-main"]')))
        first_click.click()
        second_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//div[@id = "landing"]/center/div[@class="to"]/a/img')))
        second_click.click()
        third_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', '//img[@id = "showlink"]')))
        third_click.click()
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        button = self.driver.find_element(by= 'xpath', value ='//a[@class = "btn btn-primary btn-xs"]')
        self.driver.execute_script("arguments[0].click();", button)
        link = self.driver.current_url
        try:
            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(('xpath', '//div[@class = "wait"]/center/img[@id = "soralink-human-verif-main"]'))).click()
        except:
            pass
        curr_tab = self.driver.current_window_handle
        self.driver.switch_to.window([x for x in self.driver.window_handles if x != curr_tab][0])
        self.driver.close()
        self.driver.switch_to.window(curr_tab)
        print(link)

    def parse(self, search_url):
        self.driver.get(search_url)
        link = self.driver.find_elements(by= 'xpath', value ='//ul[@class = "timeline"]//h2[@class = "post-box-title"]/a')[0].get_attribute('href')
        self.driver.get(link)
        downlinks = list(map(lambda x: x.get_attribute('href') ,self.driver.find_elements(by= 'xpath', value ='//div[@class = "box download  "]/div/a')))
        downtags = list(map(lambda x: x.get_attribute('text') ,self.driver.find_elements(by= 'xpath', value ='//div[@class = "box download  "]/div/a')))
        print(downtags)
        # self.navigateInterSites(downlinks[3])
    
    def __del__(self):
        self.driver.quit()

PaheSelenium('Avengers Endgame', '2019')