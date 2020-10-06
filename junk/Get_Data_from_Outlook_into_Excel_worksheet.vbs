'Get Data from Outlook into Excel worksheet
'https://www.exceltrainingvideos.com/get-data-from-outlook-into-excel-worksheet/
'https://stackoverflow.com/questions/30248748/vba-not-recognizing-mapi
Sub GetFromOutlook()

Dim OutlookApp As Outlook.Application
Dim OutlookNamespace As Namespace
Dim Folder As MAPIFolder
Dim OutlookMail As Variant
Dim i As Integer

Set OutlookApp = New Outlook.Application
Set OutlookNamespace = OutlookApp.GetNamespace(“MAPI”)
Set Folder = OutlookNamespace.GetDefaultFolder(olFolderInbox).Folders(“impMail”)

i = 1

For Each OutlookMail In Folder.Items
If OutlookMail.ReceivedTime >= Range(“email_Receipt_Date”).Value And Date <= 28 – mar – 2018 Then
	Range(“email_Subject”).Offset(i, 0).Value = OutlookMail.Subject
	Range(“email_Subject”).Offset(i, 0).Columns.AutoFit
	Range(“email_Subject”).Offset(i, 0).VerticalAlignment = xlTop
	Range(“email_Date”).Offset(i, 0).Value = OutlookMail.ReceivedTime
	Range(“email_Date”).Offset(i, 0).Columns.AutoFit
	Range(“email_Date”).Offset(i, 0).VerticalAlignment = xlTop
	Range(“email_Sender”).Offset(i, 0).Value = OutlookMail.SenderName
	Range(“email_Sender”).Offset(i, 0).Columns.AutoFit
	Range(“email_Sender”).Offset(i, 0).VerticalAlignment = xlTop
	Range(“email_Body”).Offset(i, 0).Value = OutlookMail.Body
	Range(“email_Body”).Offset(i, 0).Columns.AutoFit
	Range(“email_Body”).Offset(i, 0).VerticalAlignment = xlTop

i = i + 1
End If
Next OutlookMail

Set Folder = Nothing
Set OutlookNamespace = Nothing
Set OutlookApp = Nothing

End Sub