from core.models import Profile 

def give_statistic(profile:Profile)->str:
    message = f"your weight is {profile.weight}"
    return message