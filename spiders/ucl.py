import scrapy
from .resources import *


class ScrapTeamInformation(scrapy.Spider):
    name = "ucl_2021_team_info"

    start_urls = [group_stage_url]

    def team_info_extraction(self, *args):
        """
        Extracts information on a team from the group stages
        and generate a dictionary with this information.
        Also the url to the team statistic page is generated

        :param args: data like goals, wins and the likes.
        :return: team info (dict) and team stats url
        """
        n1, n2, n3, n4, n5, n6, n7, n8, n9 = args

        def get_text(n):
            return n.css('::text').get()

        qualified = bool(len(n1.css('div.table_team-qualified')))
        team_name = n1.css('img::attr(title)').get()
        team_code = n1.css('span.team-code::text').get()
        stats_url = 'https://www.uefa.com' + n1.css('a::attr(href)').get() + 'statistics/'
        wins, draws, loses = (get_text(n) for n in (n3, n4, n5))
        points = n9.css('strong::text').get()

        return {
            'Team Name': team_name,
            'Team Code': team_code,
            'Wins': wins,
            'Draws': draws,
            'Loses': loses,
            'Points': points,
            'Qualified': qualified
        }, stats_url

    def process_team_statistics_info(self, response):
        """
        processes the statistical information from
        the teams statistical pages

        :param response: Response link to follow
        :return: updated team information
        """

        def stats_info(n):
            "Generates statistical information for the team information"

            results = n.css('div.stats-module__single-stat')

            def get_attr(result, of_type):
                return result.css(f'div[slot="stat-{of_type}"]::text').get()

            return {
                get_attr(result, 'label'): get_attr(result, 'value').replace('%', '')
                for result in results
                if bool(get_attr(result, 'value'))
            }

        n1, n2, n3, n4, n5, n6, n7 = response.css('.pk-col--content')

        _information = {
            k: v for k, v in zip(
                ['Key Stats', 'Attacking', 'Distribution', 'Defending', 'GoalKeeping', 'Disciplinary'],
                [stats_info(n) for n in (n2, n3, n4, n5, n6, n7)]
            )
        }

        team_group_info = response.meta['team_group_info']
        team_group_info['Country Code'] = n1.css('span.team-country-name::text').get()

        for k in _information.keys():
            for label in _information[k].keys():
                team_group_info[label] = _information[k][label]

        yield response.follow(
            historical_url(club_info[team_group_info['Team Name']]['sub_link']),
            callback=self.process_historical_team_info,
            meta={
                'team_group_info': team_group_info
            }
        )

    def process_historical_team_info(self, response):
        """
        processes the historical information from
        the teams historical pages dating from 2011/12.

        :param response: Response link to follow
        :return: updated team information
        """

        seasons_in_decade_2010 = response.css('section#decade_container_2010 div.item')[::-1]
        seasons_in_decade_2020 = response.css('section#decade_container_2020 div.item')[::-1]

        def get_season(s):
            return s.css('div.season-year::text').get().strip()

        def get_elimination_round(s):
            return s.css('span.js-fitty::text').get().strip()

        team_group_info = response.meta['team_group_info']

        for seasons in [seasons_in_decade_2010, seasons_in_decade_2020]:
            for season in seasons:
                team_group_info[get_season(season)] = get_elimination_round(season)

        yield team_group_info

    def parse(self, response, **kwargs):
        # Get's all the groups by their tables in the table standings
        # There are 8 groups labelled A-H.
        groups = response.css('table.table.table--standings')
        groups_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        # We then loop through the groups as well as their letter
        # which represents a group -- for instance Man city in group A
        # and so...
        for letter, group in zip(groups_letters, groups):
            # Lists out each team in a group.
            # There are always four (4) teams
            group_teams = group.css('tbody tr')

            for team in group_teams:
                # The method performs a duo function;
                # It first extracts the information of the team on the
                # table and then gets the url to the overall statistics
                # of the team on their group stage performance thus far.
                #
                # The team historical url is also generated from the
                # historical_url function and team id information as gotten
                # resources.py
                team_group_info, team_stats_url = self.team_info_extraction(*team.css('td'))
                team_group_info['Group'] = letter

                # The functions process_team_statistics_info and
                # process_historical_team_info extends the information on
                # each team getting statistical data like ball recoveries
                # to historical information like where the team dropped in
                # the year 2012.
                #
                # then we scraps and generate data.
                yield response.follow(
                    team_stats_url,
                    callback=self.process_team_statistics_info,
                    meta={
                        'team_group_info': team_group_info
                    }
                )
