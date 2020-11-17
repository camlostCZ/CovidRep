# Covid-19 Stats for The Czech Republic

## Purpose
The official web site of Czech Ministry of Health doesn't provide reasonably
accessibile visualization of recent Covid-19 spreading among citizens in
each individual city.

This project aims to fullfil the gap at least for several selected cities.

## Data Sources
Only oficially published datasets has been used.

## Workflow
The dataset is being downloaded each 4 hours - the volume od the data downloaded
is quite large (~ 200 MB at the time of writing) and I don't want to create
unnecessary load to the source web site.

This task is performed by a scheduled job. It's code is out of scope of this
project (actually it's just a simple wget command).

Then, this project comes into play.

The dataset is processed and divided into individual CSV files - each for a city.
The files are published to be ready for importing into a Google Spreadsheet
where a chart is generated and published for further use.

Example:
https://bit.ly/38FMKM0
