# -*- coding: utf-8 -*-
import scrapy
import datetime


class LeagueresultsSpider(scrapy.Spider):
    name = 'leagueresults'
    allowed_domains = ['xscores.com']
    start_urls = ['https://www.xscores.com/soccer/leagueresults/england/premier_league']

    def parse(self, response):
        rows = response.xpath('//div[@class="score_row padded_date country_header"]|//div[@data-game-status and @data-league-code]')

        match_data = {}
        for row in rows:

            if 'data-game-status' not in row.attrib:
                match_date = row.xpath('./text()').extract_first().strip()
                match_data['Date'] = datetime.datetime.strptime(match_date, "%d-%m-%Y").strftime("%Y-%m-%d")
                continue

            match_data['Match Time'] = row.xpath('.//div[@class="score_ko score_cell"]/text()').extract_first()
            match_data['Home Team'] = row.xpath('.//div[contains(@class, "score_home_txt")]/text()').extract_first()
            match_data['Away Team'] = row.xpath('.//div[contains(@class, "score_away_txt")]/text()').extract_first()

            half_time_score = row.xpath('.//div[@class="score_ht score_cell"]/text()').extract_first()
            match_data['Home Team Half-Time Score'], match_data['Away Team Half-Time Score'] = half_time_score.split('-')

            full_time_score = row.xpath('.//div[@class="score_score score_cell"]/text()').extract_first()
            match_data['Home Team Full-Time Score'], match_data['Away Team Full-Time Score'] = full_time_score.split('-')

            yield match_data
