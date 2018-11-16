import csv

CSVFILE = "soccer_players.csv"
TEAMS = ["Sharks", "Dragons", "Raptors"]
TEAMFILE = "teams.txt"


def read_player_list():
    """Create a list of players from CSV file.
    """
    with open(CSVFILE, "r") as csv_file:
        players = csv.DictReader(csv_file)
        return [row for row in players]


def get_experienced_players(players):
    """Identify players with soccer experience in a list.
    """
    experienced_players = []
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
    return experienced_players


def get_novice_players(players):
    """Identify players with no soccer experience in a list.
    """
    inexperienced_players = []
    for player in players:
        if player["Soccer Experience"] == "NO":
            inexperienced_players.append(player)
    return inexperienced_players


def create_teams(experienced_players, inexperienced_players):
    """Distribute teams based on experience."""

    num_teams = len(TEAMS)

    experienced_group = []
    for i in range(num_teams):
        experienced_group.append(experienced_players[i::num_teams])

    inexperienced_group = []
    for i in range(num_teams):
        inexperienced_group.append(inexperienced_players[i::num_teams])

    # Create list of dicts, each containing final team roster.
    return [
        {"team": team, "players": experienced_group.pop() + inexperienced_group.pop()}
        for team in TEAMS
    ]


def write_teams(teams):
    """Write each provided team and its players out to a text file.
    """
    # Player information we want for team roster.
    player_info = {"Name", "Soccer Experience", "Guardian Name(s)"}
    with open(TEAMFILE, "a") as team_file:
        for team in teams:
            team_file.write("\n{}\n".format(team["team"]))
            for player in team["players"]:
                team_file.write("{}, {}, {}\n".format(*[v for k, v in player.items() if k in player_info]))


def main():
    available_players = read_player_list()
    experienced_players = get_experienced_players(available_players)
    novice_players = get_novice_players(available_players)
    teams = create_teams(experienced_players, novice_players)
    write_teams(teams)


if __name__ == "__main__":
    main()
