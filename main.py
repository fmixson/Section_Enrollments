import pandas as pd
import openpyxl
from datetime import date, datetime



class SetDates:

    def __init__(self, section_df):
        self.section_df = section_df

    def set_start_date(self):
        
        if self.section_df.loc[0, 'Session Code'] == '1':
            self.section_df['Start Date'] == '2023-01-29'
        if self.section_df.loc[0, 'Session Code'] == '15Q':
            self.section_df['Start Date'] == '1/9/23'
        if self.section_df.loc[0, 'Session Code'] == '9A':
            self.section_df['Start Date'] == '1/9/23'
        if self.section_df.loc[0, 'Session Code'] == '15B':
            # self.section_df = self.section_df.assign(Start_Date='2/6/23')
            self.section_df.loc[:, 'Start Date'] = '2023-02-06'



        if self.section_df.loc[0, 'Session Code'] == '9B':
            self.section_df['Start Date'] == '3/20/23'
        self.section_df['Start Date'] = pd.to_datetime(self.section_df['Start Date'])

    def set_census_date(self):
        self.section_df['Census Date'] = self.section_df['Start Date'] + pd.Timedelta(days=21)

    def start_date_enrollment(self):
        start_date = self.section_df.loc[0, 'Start Date']
        # start_date = start_date.to_date()
        print(self.section_df.dtypes)
        self.section_df['Enrollment Drop Date'] = pd.to_datetime(self.section_df['Enrollment Drop Date'])
        start_date_enrollment_df = self.section_df[self.section_df['Enrollment Drop Date'] > start_date]

        starting_enrollment = len(self.section_df)
        print('start date df',start_date_enrollment_df)

    def census_date_enrollment(self):
        census_date = self.section_df['Start Date'] + pd.Timedelta(days=21)
        census_date_enrollment_df = self.section_df[self.section_df['Enrollment Drop Date'] > census_date]
        print(census_date_enrollment_df)
        print(len(census_date_enrollment_df))

    def current_date_enrollment(self):
        today = date.today()
        # ['Enrollment Drop Date'] = df[df['Enrollment Drop Date']].dt.date
        # semester_end_date = '2023-05-31'
        # date_object = datetime.strptime(semester_end_date, '%Y-%m-%d').date()
        print(type(today))
        print(semester_end_date)
        print(self.section_df.dtypes)
        if today > semester_end_date:
            today = semester_end_date
        else:
            current_enrollment_df = self.section_df[self.section_df['Enrollment Drop Date'] < today]

        print(current_enrollment_df)

# def set start dates
# def set census dates
# def calculate enrollment at start date
# def calculate drop rate
# def calculate FTES
df = pd.read_csv('C:/Users/family/Documents/Weekly Enrollment Sheets/Copy of Liberal Arts AHC and Undecided Spring 2023 ENR 2023.05.23.csv')
pd.set_option('display.max_columns', None)

df.sort_values(by=['Section Number'])
df.fillna(0)
semester_end_date = '2023-05-31'
semester_end_date = datetime.strptime(semester_end_date, '%Y-%m-%d').date()
df = df[df['Term'] != 'nan']

df['Enrollment Drop Date'] = pd.to_datetime(df['Enrollment Drop Date']).dt.date
print(df.dtypes)
section_numbers = []
print(len(df))
for i in range(len(df)):
    if df.loc[i, 'Section Number'] not in section_numbers:
        section_numbers.append(df.loc[i, 'Section Number'])

for section in section_numbers:
    section_df = df[df['Section Number'] == section].reset_index()
    section_df = section_df.fillna(semester_end_date)
    print(section_df.dtypes)
    dates = SetDates(section_df=section_df)
    dates.set_start_date()
    dates.set_census_date()
    dates.start_date_enrollment()
    dates.census_date_enrollment()
    dates.current_date_enrollment()
df.to_excel('Test.xlsx')
