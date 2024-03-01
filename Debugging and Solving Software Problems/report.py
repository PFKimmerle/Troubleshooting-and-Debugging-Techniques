#!/usr/bin/env python3

# Import necessary libraries for handling CSV, dates, and HTTP requests
import csv
import datetime
import requests

# Define the URL where the CSV file is located
FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_file_lines(url):
    """Download the CSV file and return its content as a list of lines."""
    # Send a GET request to the URL
    response = requests.get(url)
    # Decode the content to a string using UTF-8 encoding
    content = response.content.decode('utf-8')
    # Split the content into lines and return the list
    lines = content.splitlines()
    return lines

def preprocess_data(lines):
    """
    Convert the CSV file lines into a dictionary where each key is a start date
    and each value is a list of employees who started on that date.
    """
    # Create a CSV reader to parse the lines, skipping the header line
    reader = csv.reader(lines[1:])
    # Initialize an empty dictionary to hold the preprocessed data
    employee_start_dates = {}
    # Loop through each row in the CSV file
    for row in reader:
        # Convert the start date string to a datetime.date object
        start_date = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()
        # Concatenate the employee's first and last name
        employee = "{} {}".format(row[0], row[1])
        # If this start date isn't in the dictionary, add it with an empty list
        if start_date not in employee_start_dates:
            employee_start_dates[start_date] = []
        # Append the employee's name to the list for this start date
        employee_start_dates[start_date].append(employee)
    return employee_start_dates

def get_start_date():
    """Prompt the user to enter a start date and return it as a datetime.date object."""
    print('Getting the first start date to query for.')
    print('The date must be greater than Jan 1st, 2018')
    # Get year, month, and day from the user, ensuring they are integers
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    # Return entered date as a datetime.date object
    return datetime.datetime(year, month, day)

def list_newer(start_date, preprocessed_data):
    """
    Print out the list of employees who started on or after the given start date,
    using the preprocessed data dictionary.
    """
    # Get today's date for comparison
    current_date = datetime.datetime.today().date()
    # Loop from the start_date until today
    while start_date <= current_date:
        # Check if start_date is in the preprocessed data
        if start_date in preprocessed_data:
            # Get list of employees for this date
            employees = preprocessed_data[start_date]
            # Print date and the employees who started on this date
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        # Move to next date
        start_date += datetime.timedelta(days=1)

def main():
    # Get lines from the file once
    lines = get_file_lines(FILE_URL)
    # Preprocess data into a dictionary
    preprocessed_data = preprocess_data(lines)
    # Get start date from the user
    start_date = get_start_date().date()
    # List employees starting from the given start date
    list_newer(start_date, preprocessed_data)

# executing the main function when the script is run
if __name__ == "__main__":
    main()
