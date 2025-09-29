def average_cardio(trens:list):
    cardio = [tren.cardio for tren in trens]
    if sum(cardio)/len(cardio) < 6:
        return {"message":f"you need more cardio, your cardio:{int(sum(cardio)/len(cardio))}"}
    elif sum(cardio)/len(cardio) > 12:
        return {"message":"you need more rest and few cardio"}
    return {"message":"you cardio is normal"}