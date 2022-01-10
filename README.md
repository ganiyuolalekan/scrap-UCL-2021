# Scraping the UEFA Champions League (UCL) data

This project extracts group stage information on the current teams in the season 2021/22 (both statistical and historical data) making use of the scrapy tool. Most of the information scraped were hardcoded to obtain specified data.

```python
['Team Name', 'Team Code', 'Wins', 'Draws', 'Loses', 'Points',
 'Qualified','Group','Country Code','Goals','Goals conceded',
 'Possession (%)', 'Passing accuracy (%)', 'Balls recovered',
 'Tackles won', 'Clean sheets', 'Saves', 'Distance covered (km)',
 'Yellow cards', 'Red cards', 'Right foot', 'Left foot', 'Head', 
 'Assists', 'Attacks', 'Clear chances', 'Penalties scored', 
 'Corners taken', 'Offsides', 'Runs into attacking third', 
 'Runs into key play area', 'Passes completed', 
 'Short passes completed', 'Medium passes completed', 
 'Long passes completed', 'Crossing accuracy (%)', 
 'Crosses completed', 'Crosses attempted', 'Free-kicks taken', 
 'Times in possession', 'Passes into attacking third', 
 'Passes into key play area', 'Passes into penalty area', 'Blocks']
```

The data-set (which was published on [kaggle](https://www.kaggle.com/ganiyuolalekan/uefa-champions-league-202122)) is an intuitive data-set and thus it can be used to answer simple questions since it is quiet small but detailed. __read my article on [steps to creating a proper dataset](#)__ 

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
git clone 
cd 
scrapy crawl ucl_2021_team_info -o ucl_2021_22_data.csv
```

**OR**

```commandline
scrapy crawl ucl_2021_team_info -o ucl_2021_22_data.json
```
