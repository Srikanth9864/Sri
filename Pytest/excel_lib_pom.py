from xlrd import open_workbook

# Reading locators
def read_locators(pagename):
    wb = open_workbook("K:/Python Notes/Pytest/Objects.xls")
    ws = wb.sheet_by_name(pagename)
    used_rows = ws.nrows
    locators = { }
    for i in range(1, used_rows):
        data = ws.row_values(i)
        locators[data[0]] = (data[1], data[2])
    return locators

# Read headers # headers = "gender,fname,lname,email,password"
# Read the headers
def read_headers(sheet_name, test_case_name):
    wb = open_workbook("K:/Python Notes/Pytest/Testdata.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    for i in range(0, used_rows):
        row = ws.row_values(i)
        if row[0] == test_case_name:
            headers = ws.row_values(i-1)
            # Get only those items which evaluates to Boolean True (Removing empty strings)
            headers = [ header  for header in headers if header]
            return ",".join(headers[2:])

# Reading the actual data
def read_data(sheet_name, test_case_name):
    actual_data = [ ]
    wb = open_workbook("K:/Python Notes/Pytest/Testdata.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    for i in range(0, used_rows):
        row = ws.row_values(i)
        if row[0] == test_case_name:
            # Get only those items which evaluates to Boolean True (Removing empty strings)
            data = [ item for item in row if item]
            if data[1] == "Yes":
                actual_data.append(data[2:])
    return actual_data