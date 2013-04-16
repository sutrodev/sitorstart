#!/usr/bin/env python

import csv
import argparse 
import requests

from team import Team


league = {}
team = None
BASE_TWITTER_SEARCH='http://search.twitter.com/search.json?q=%s&src=typd'


def setup_league():
    with open('../league_164_rosters.csv', 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        for row in filereader:
            current_key = row[0]
            if current_key in league.keys():
                league[current_key].append(row[1])
            else:
                league[current_key] = [row[1]]


def print_league():
    for k, v in league.items():
        team = Team(k, v)
        print team.name
        for player in team.players:
            print '\t' + player
        print '\n'


def init_team(team_name):
    team = Team(team_name, league[team_name])
    search_team(team)
           

def search_team(team):
    for player in team.players:
        url = BASE_TWITTER_SEARCH % player
        r = requests.get(url)
        player_results = r.json()
        for results in player_results['results']:
            print results['text']
            print '\n\n'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Let Twitter set your linup!')
    parser.add_argument('-t', '--team', help='Your team name', required=True)
    team_name = parser.parse_args().team

    setup_league()
    print_league()
    init_team(team_name)
