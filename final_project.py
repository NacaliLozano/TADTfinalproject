import csv
import datetime
import requests
from pickle import TRUE

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    response = requests.get(url, stream=TRUE)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

# def get_same_or_newer(start_date):
#     data = get_file_lines(FILE_URL)
#     reader = csv.reader(data[1:])
#     min_date = datetime.datetime.today()
#     min_date_employees = []
#     dictionary = {}
#     for row in reader:
#         if not datetime.datetime.strptime(row[3], '%Y-%m-%d') in dictionary:
#             dictionary[datetime.datetime.strptime(row[3], '%Y-%m-%d')] = []
#             dictionary[datetime.datetime.strptime(row[3], '%Y-%m-%d')].append(row[0] + " " + row[1])
#         else:
#             dictionary[datetime.datetime.strptime(row[3], '%Y-%m-%d')].append(row[0] + " " + row[1])
#     print(dictionary)
    
def list_newer(start_date):
    # while start_date < datetime.datetime.today():
    #     start_date, employees = get_same_or_newer(start_date)
    #     print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
    #     start_date = start_date + datetime.timedelta(days=1)
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    dictionary = {}
    
    for row in reader:
        if not datetime.datetime.strptime(row[3], '%Y-%m-%d') in dictionary:
            dictionary[datetime.datetime.strptime(row[3], '%Y-%m-%d')] = []
        dictionary[datetime.datetime.strptime(row[3], '%Y-%m-%d')].append(row[0] + " " + row[1])
    
    while start_date < datetime.datetime.today():
        if not start_date in dictionary.keys():
            pass
        else:
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), dictionary[start_date]))
        start_date += datetime.timedelta(days=1)
        
def main():
    start_date = get_start_date()
    list_newer(start_date)
    
if __name__ == "__main__":
    main()