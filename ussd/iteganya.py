from .models import * 

def insertData(category, sessionID, phoneNumber):
    insert = Iteganyagihe(category=category, 
     sessionId=sessionID,
     phonNumber=phoneNumber
    )
    saveDate= insert.save()
    return saveDate