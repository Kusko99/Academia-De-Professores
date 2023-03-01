

def DateSQLToDate(date):
    day = str(date.day)
    month = str(date.month)
    year = str(date.year)
    formated_date = day + "/" + month + "/" + year
    print(formated_date)
    return formated_date

def DateSQLToDate_STR(date):
    day = date[8:10]
    month = date[5:7]
    year = date[0:4]
    formated_date = day + "/" + month + "/" + year
    print(formated_date)
    return formated_date

# DateToSQLDate('2022-11-30')