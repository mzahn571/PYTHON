# The below method is used to read data from an active worksheet and store it in memory.
def reader(file):
    global path
    abs_file = os.path.join(path, file)
    wb_sheet = load_workbook(abs_file).active
    rows = []
    # min_row is set to 2, to ignore the first row which contains the headers
    for row in wb_sheet.iter_rows(min_row=2):
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        # custom column data I am adding, not needed for typical use cases
        row_data.append(file[17:-6])
        # Creating a list of lists, where each list contain a typical row's data
        rows.append(row_data)
    return rows


if __name__ == '__main__':
    # Folder in which my source excel sheets are present
    path = r'C:/Users/ab21600/Documents/DA'
    # To get the list of excel files
    files = os.listdir(path)
    for file in files:
        rows = reader(file)
        # below mentioned file name should be already created
        book = load_workbook('new.xlsx')
        sheet = book.active
        for row in rows:
            sheet.append(row)
        book.save('new.xlsx')
