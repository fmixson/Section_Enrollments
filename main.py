import pandas as pd
import openpyxl

df = pd.read_csv('C:/Users/family/Documents/Weekly Enrollment Sheets/Copy of Liberal Arts AHC and Undecided Spring 2023 ENR 2023.05.23.csv')
pd.set_option('display.max_columns', None)
print(df.dtypes)
df.sort_values(by=['Section Number'])
df.fillna(0)
print(df)

class SetDates:

    def __init__(self, section_df):
        self.section_df = section_df

    def set_start_date(self):
        
        if self.section_df.loc[0, 'Session Code'] == '1':
            self.section_df['Start Date'] == '1/9/23'
        if self.section_df.loc[0, 'Session Code'] == '15Q':
            self.section_df['Start Date'] == '1/9/23'
        if self.section_df.loc[0, 'Session Code'] == '9A':
            self.section_df['Start Date'] == '1/9/23'
        if self.section_df.loc[0, 'Session Code'] == '15B':
            # self.section_df = self.section_df.assign(Start_Date='2/6/23')
            self.section_df.loc[:, 'Start Date'] = '2/6/23'
            self.section_df['Start Date'] = pd.to_datetime(self.section_df['Start Date'])
            self.section_df['Enrollment Drop Date'] = pd.to_datetime(self.section_df['Enrollment Drop Date'])

        if self.section_df.loc[0, 'Session Code'] == '9B':
            self.section_df['Start Date'] == '3/20/23'

    def set_census_date(self):
        self.section_df['Census Date'] = self.section_df['Start Date'] + pd.Timedelta(days=21)

    def start_date_enrollment(self):
        start_date = self.section_df.loc[0, 'Start Date']
        start_date_enrollment_df = self.section_df[self.section_df['Enrollment Drop Date'] > start_date]
        starting_enrollment = len(self.section_df)
        print(starting_enrollment)

    def census_date_enrollment(self):
        census_date = self.section_df['Start Date'] + pd.Timedelta(days=21)
        census_date_enrollment_df = self.section_df[self.section_df['Enrollment Drop Date'] > census_date]
        print(census_date_enrollment_df)
        print(len(census_date_enrollment_df))
# def set start dates
# def set census dates
# def calculate enrollment at start date
# def calculate drop rate
# def calculate FTES
df = df[df['Term'] != 'nan']
section_numbers = []
print(len(df))
for i in range(len(df)):
    if df.loc[i, 'Section Number'] not in section_numbers:
        section_numbers.append(df.loc[i, 'Section Number'])

for section in section_numbers:
    section_df = df[df['Section Number'] == section].reset_index()
    section_df = section_df.fillna('5/31/23')
    dates = SetDates(section_df=section_df)
    dates.set_start_date()
    dates.set_census_date()
    dates.start_date_enrollment()
    dates.census_date_enrollment()

df.to_excel('Test.xlsx')
