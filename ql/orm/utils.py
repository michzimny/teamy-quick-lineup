from .models import Team


def get_num_of_tables():
    num_of_teams = Team.objects.count()
    assert num_of_teams % 2 == 0
    return int(num_of_teams / 2)
