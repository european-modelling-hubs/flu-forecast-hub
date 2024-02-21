# Target Data - ERVISS

This folder contains the ground truth information about ILI incidence in EU/EEA countries from [ERVISS](https://erviss.org/).

To access the latest data file, consider the [`latest-ILI_incidence.csv`]((https://github.com/european-modelling-hubs/flu-forecast-hub/blob/main/target-data/ERVISS/latest-ILI_incidence.csv)). Alternatively, historical data files are stored in the folder [`snapshots`](https://github.com/european-modelling-hubs/flu-forecast-hub/tree/main/target-data/ERVISS/snapshots) and are named `YYYY-MM-DD-ILI_incidence.csv`, with `YYYY-MM-DD` representing the date of the last data update (which occurs every Friday). It's important to note that the [latest file](https://github.com/european-modelling-hubs/flu-forecast-hub/blob/main/target-data/ERVISS/latest-ILI_incidence.csv) not only includes new data points but also the entire available history.

**Note**: To access additional datasets for informing your model, please visit the [Respiratory Viruses Weekly Data](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/tree/main) repository published by the ECDC.

Each ground truth CSV file contains the following columns:

| column | column type | description |
| -------- | -------- | ------- |
| `location` | string | **ISO-2** code identifying the country |
| `truth_date` | date | Date in format **YYYY-MM-DD**: the last day of the truth week (Sunday)|
| `year_week` | string | A string denoting the year and week to which the truth data corresponds |
| `value ` | decimal | ILI incidence per $100,000$ population (except for Finland, Malta, Luxembourg, where it is reported per $100,000$ consultations)|


ERVISS covers the following countries: 

    AT, BE, HR, CZ, DK, EE, FI, FR, GR, HU, IS, IE, IT, LV, LT, LU, MT, NL, NO, PL, PT, RO, SK, SI
