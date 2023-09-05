import customtkinter
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

from scrapy.crawler import CrawlerProcess
from movie_recommendor.movie_scrapers.spiders.gcextractor_spider import preliminarySpider

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
            
        # configure window
        self.title("Salary Recorder")
        self.geometry(f"{1100}x{580}")
        self.minsize(1100,580)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.button = customtkinter.CTkButton(self, text='Run', command=self.buttonClicked)
        self.button.pack()

    def buttonClicked(self):
        process = CrawlerProcess()
        process.crawl(preliminarySpider)
        process.start()
    # def buttonClicked(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument("--start-maximized")

    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
    #     driver.get("https://www.google.com")
   
if __name__ == "__main__":
    app = App()
    app.mainloop()