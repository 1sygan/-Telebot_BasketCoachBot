from fuzzywuzzy import fuzz


def recognize_team(team, teams):

    recognized = {'id': '', 'percent': 0}
    for key, value in teams.items():
        for t in value:
            percent = fuzz.ratio(team, t)
            if percent > recognized['percent']:
                recognized['id'] = key
                recognized['percent'] = percent
    return recognized['id']