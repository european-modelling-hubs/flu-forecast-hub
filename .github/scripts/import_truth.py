import os
import sys
import csv
from urllib.request import urlopen
from datetime import datetime, timedelta
from isoweek import Week

import pycountry

# Config

url = 'https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/snapshots/{snapshot_date}_ILIARIRates.csv'
out_files_ILI = ['target-data/ERVISS/latest-ILI_incidence.csv', 'target-data/ERVISS/snapshots/{report_date}-ILI_incidence.csv']


# Build URL

today = datetime.now()
days_to_last_friday = (today.weekday() - 4) % 7
last_friday_date = today - timedelta(days=days_to_last_friday)
snapshot_date=last_friday_date.date().isoformat()

url = url.format(snapshot_date=snapshot_date)
try:
    response = urlopen(url)
except urllib.error.HTTPError:
    sys.exit(0)


# Read data

lines = [line.decode('utf-8') for line in response.readlines()]

csv_reader = csv.DictReader(lines, delimiter=',')

ILI_records = [('location', 'truth_date', 'year_week', 'value')]


for row in csv_reader:
    if (row['survtype'] != 'primary care syndromic'
            or row['indicator'] != 'ILIconsultationrate'
            or row['age'] != 'total'):
        continue
    country2 = pycountry.countries.lookup(row['countryname']).alpha_2
    year, week = map(int, row['yearweek'].split('-W'))
    week_obj = Week(year, week)
    truth_date = week_obj.sunday().isoformat()
    value = float(row['value'])
    ILI_records.append((country2, truth_date, row['yearweek'], value))


# Write output files

out_files_ILI = [of.format(report_date=snapshot_date) for of in out_files_ILI]

for output_path in out_files_ILI:
    with open('./repo/' + output_path, 'w') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(ILI_records)    

env_file = os.getenv('GITHUB_OUTPUT')
with open(env_file, "a") as outenv:
   outenv.write (f"imported_files={' '.join([out_file for out_file in out_files_ILI if not 'latest-' in out_file] )}")
