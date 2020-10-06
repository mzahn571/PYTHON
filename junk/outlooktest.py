import win32com.client
import win32com
import os
import pickle
outlook = win32com.client.Dispatch("outlook.Application").GetNameSpace("MAPI")

inbox = outlook.Folders("Ibis2").Folders("Inbox").Folders("06-2016")

message = inbox.items
infolist = []
for message2 in message:
    #message2=message.GetLast()
    subject=message2.Subject
    #date1=message2.senton.Date()
    sender = message2.Sender
    receipt = message2.ReceivedTime
    print receipt, " | ", subject, " | ", sender
    infolist.append((receipt, subject, sender))
    message2.Save
    message2.Close(0)
fp = open("C:\Python27\\emails.pkl","w")
pickle.dump(infolist, fp)
fp.close() 
