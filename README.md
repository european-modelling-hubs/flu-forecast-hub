# European Flu Forecasting Hub
The European Flu Forecasting Hub collates weekly forecasts on Influenza-Like-Illness (ILI) incidence in EU/EEA countries. To view the latest forecast visit the [Hub Website](https://respicast.ecdc.europa.eu/forecasts/).

## Forecasting Targets and Update Frequency
During the influenza season, participating teams submit weekly probabilistic forecasts from their models regarding ILI incidence for the upcoming four weeks. This data is communicated every week by the ECDC through the [ERVISS report](https://erviss.org/). Data is updated generally on Friday, and it reports ILI incidence related up to the previous week. Forecast submission opens right after updated data are uploaded to this repository and closes on the next Wednesday at 23:59 CET. In the event of changes in the timelines of data availability, the day of the week for forecast submissions may be adjusted accordingly. In such instances, participants will receive notifications at least one week in advance. Following the submission deadline, forecasts and the ensemble are published on the [Hub website](LINK) every Thursday. They cover the preceding week (which lacks consolidated public data), the current week, and the two subsequent weeks.

## Quick Start
This is a brief outline for anyone considering contributing a forecast. For a detailed guide on how to structure and submit a forecast, please read the technical [Wiki](https://github.com/european-modelling-hubs/flu-forecast-hub/wiki).


#### Setup
To prepare for your initial submission, consult the [Preparing to Submit](https://github.com/european-modelling-hubs/flu-forecast-hub/wiki/Preparing-to-submit) guide. This guide provides details on forking the repository, creating a team folder, and uploading a team metadata file.

#### Targets
After completing the preceding steps, you are now prepared to submit your first forecast. We are currently focused on the forecast target of Weekly ILI Incidence (notified cases per $100,000$) in EU/EEA countries. Forecasts are evaluated against ILI incidence stored in the `target-data` folder of this repository. 


#### Forecast Submission
Forecast can be submitted to the Hub either via [GitHub website](https://github.com/european-modelling-hubs/flu-forecast-hub/wiki/Submitting-using-GitHub-Website) or [GitHub Command Line](https://github.com/european-modelling-hubs/flu-forecast-hub/wiki/Submitting-using-GitHub-Command-Line). The submission will trigger automatic validations that check the forecast have the [required format](https://github.com/european-modelling-hubs/flu-forecast-hub/wiki/Submission-Format). Incorrect formatting will lead to errors, resulting in submission failure. If this occurs, kindly review and rectify your format. Should you encounter persistent issues, feel free to reach out to us via email at [European.Modelling.Hub@ecdc.europa.eu](mailto:European.Modelling.Hub@ecdc.europa.eu) or by opening an issue in this repository.


## About European Flu Forecasting Hub
The European Flu Forecasting Hub is part of the European Respiratory Diseases Forecasting Hubs consortium (RespiCast), which combines multiple forecasting hubs for several respiratory disease indicators, including influenza-like-illness (ILI), acute respiratory infection (ARI), and COVID-19. This consortium of hubs is run in collaboration between the European Centre for Disease Control and Prevention (ECDC), the [ISI Foundation](https://www.isi.it/en/home), and the [London School of Hygiene & Tropical Medicine](https://epiforecasts.io/). Teams from anywhere in the world are invited to submit weekly forecasts for one or more disease indicators and for one or more countries. For more information visit the [RespiCast website](https://respicast.ecdc.europa.eu/)

## Get in Touch
If you have any questions or encounter issues at any stage, please don't hesitate to reach out to us via [email](mailto:European.Modelling.Hub@ecdc.europa.eu).

