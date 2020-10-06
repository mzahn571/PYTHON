import win32com.client
import sys
import unicodecsv as csv

output_file = open('./outlook_test03.csv','wb')    
output_writer = csv.writer(output_file, delimiter = ";", encoding='latin2')

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. 
messages = inbox.Items

for i, message in enumerate(messages):              # enumerated the items
    try:

        sender = message.SenderName                 
        sender_address = message.sender.address         
        sent_to = message.To                    
        date = message.LastModificationTime         
        subject = message.subject                   

        output_writer.writerow([
            date, 
            sender, 
            sender_address,             
            sent_to,
            subject
            ]) 

    except Exception as e:
        ()

output_file.close()
