# Scraping the UEFA Champions League (UCL) data

This project extracts group stage information on the current teams in the season 2021/22 (both statistical and historical data) making use of the scrapy tool. 

Most of the information scraped currently were hardcoded to obtain specified data from this season (2021/22). But in future works it would be able to extract the entire league data of each seasonal competition which will be recorded at [kaggle](https://www.kaggle.com/ganiyuolalekan/uefa-champions-league-202122).

Some data recorded are:

| Columns | Descriptions |
|:--------------:|:--------------:|
| Team Name | Team names record  |
| Team Code | Teams short code information |
| Country Code | Teams country code information |
| Wins | Number of wins in the competition  |
| Draws | Number of draws in the competition |
| Loses | Number of loses in the competition |
| Points | Total point of teams in the season |
| Group | Teams group for the season |
| Qualified | Team qualification status (True if qualified) |

Others includes: Goals, Goals conceded, Possession, Passing accuracy, Balls recovered, Tackles won, Clean sheets, Saves, Distance covered e.t.c.

The [data-set](https://www.kaggle.com/ganiyuolalekan/uefa-champions-league-202122)) is an intuitive data-set, thus it can be used to answer simple questions since it is quiet small but detailed. __read my article on [Factors Essential to Creating a Data-Set](https://gmolalekan.medium.com/factors-essential-to-creating-a-data-set-88aa617a71f8)__ 

To recreate the crawling steps start by installing Scrapy; using conda, run:

```commandline
conda install -c conda-forge scrapy
```

Alternatively, if you’re already familiar with installation of Python packages, you can install Scrapy and its dependencies from PyPI with:

```commandline
pip install Scrapy
```

Once this is done, you can proceed to cloning the project and crawling the data into a csv or json file.

```commandline
git clone https://github.com/ganiyuolalekan/scrap-UCL-2021.git
cd 
scrapy crawl ucl_2021_team_info -o ucl_2021_22_data.csv
```

**OR**

```commandline
scrapy crawl ucl_2021_team_info -o ucl_2021_22_data.json
```
