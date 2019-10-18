import openpyxl
import shutil
import copy

distinct_stores = ['willy']



for idx,store in enumerate(distinct_stores):
    workbook_iter_name = store+'.xlsx'
    #using a blank, single worksheet xlsx file for illustration purposes
    shutil.copyfile('blank.xlsx',workbook_iter_name)
    primary = openpyxl.load_workbook(workbook_iter_name)
    reps_per_store = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen']
    for ido,reps in enumerate(reps_per_store): 
        ws = primary.get_sheet_by_name('rep')
        primary.add_sheet(copy.deepcopy(ws),ido+1)
        wss=primary.worksheets[ido+1]
        wss.title = reps
    primary.save(workbook_iter_name)