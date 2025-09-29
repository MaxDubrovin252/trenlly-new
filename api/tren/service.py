from collections import Counter

def average_cardio(trens:list)->str:
    cardio = [tren.cardio for tren in trens]
    if sum(cardio)/len(cardio) < 6:
        return {"message":f"you need more cardio, your cardio:{int(sum(cardio)/len(cardio))}"}
    elif sum(cardio)/len(cardio) > 12:
        return {"message":"you need more rest and few cardio"}
    return {"message":"you cardio is normal"}

def groups(trens:list):
    groups = [tren.body_group for tren in trens]
    freq = Counter(groups)
    
    most_common = freq.most_common(1)
    
    if most_common:
        value,count = most_common[0]
        return f"you favorite body group is {value}"
    
    
    
def exercise_freq(trens:list):
    exc_list = [tren.exercise for tren in trens]
    freq = Counter(exc_list)
    
    most_common = freq.most_common(1)
    
    
    
    if most_common:
        value,count = most_common[0]
        return f"most favorite exercise:{value}"