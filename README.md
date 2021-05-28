# movie_recommendor

It is a web spider to scrape movies and suggest them according to your preferences and google rating and likes percent. If tired of finding new good movies, can be a real life saver.

## Packages required

It requires following packages of python 3:

#### Scrapy

`python3 -m pip install scrapy`

#### Selenium

`python3 -m pip install selenium`

#### Chrome

`sudo apt install chromium-chromedriver`

It also requires to download the git repo.

```
cd desired_folder
git clone https://github.com/devanshusingla/movie_recommendor.git
```

## How to Use

Change into the _movie_recommendor_ directory and select the desired options in _config.user.json_. For ex: you can specify genre from genres mentioned in _data/genre_ file and movie_categories from categories mentioned in _data/categories_ file. Then run the python script through
`python3 main.py`

It will continue to scrape data for a while. The extracted movies can be viewed in _data/movies.jl_ file.

### Credits

[Devanshu](https://github.com/devanshusingla) and [Amit](https://github.com/amit1729)
