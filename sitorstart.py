#!/usr/bin/env python

import csv

from team import Team


league = {}


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


def main():
    setup_league()
    print_league()


if __name__ == "__main__":
    main()
