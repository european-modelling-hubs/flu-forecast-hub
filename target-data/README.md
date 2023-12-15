# Target Data

This `target-data` folder contains the ground truth information about ILI incidence in EU/EEA countries.

To access the latest data file, consider the [`latest-ILI_incidence.csv`]((https://github.com/european-modelling-hubs/flu-forecast-hub/blob/main/target-data/ERVISS/latest-ILI_incidence.csv)) in `target-data/ERVISS/`. Alternatively, historical data files are stored in the folder [`snapshots`](https://github.com/european-modelling-hubs/flu-forecast-hub/tree/main/target-data/ERVISS/snapshots) and are named `YYYY-MM-DD-ILI_incidence.csv`, with `YYYY-MM-DD` representing the date of the ERVISS data update (which occurs every Friday). It's important to note that the [latest file](https://github.com/european-modelling-hubs/flu-forecast-hub/blob/main/target-data/ERVISS/latest-ILI_incidence.csv) not only includes new data points but also the entire available history.

Each ground truth CSV file contains the following columns:

| column | column type | description |
| -------- | -------- | ------- |
| `location` | string | **ISO-2** code identifying the country |
| `truth_date` | date | Date in format **YYYY-MM-DD**: the last day of the truth week (Sunday)|
| `year_week` | string | A string denoting the year and week to which the truth data corresponds |
| `value ` | decimal | ILI incidence per $100,000$ |
