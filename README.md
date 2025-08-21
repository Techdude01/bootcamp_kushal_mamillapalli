# Bootcamp Repository

## Folder Structure

- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
  GitHub.
- **data/** → Local storage for data. Most Data pushed to github, except large data sources

## Homework Folder Rules

- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.

## Project Folder Rules

- Keep project files organized and clearly named.

## Data Rules

- Homework will have its own data folders for easier separation and less clutter around the project data
- raw/ stores raw unprocessed data from donwload/api/scrape
- processed/ stores cleaned and processed data (CSV,Parquet)
- plots/ stores visualizations of data for analysis and cleaning

## Data Cleaning Strategy

### Functions

- **fill_missing_median()**: Fills numeric missing values with column medians - reduce NaNs in column
- **drop_missing()**: Removes rows with missing values based on threshold or specific columns - if too many missing values remove it
- **normalize_data()**: Scales numeric data using MinMax or Standard scaling - scale the data for better visualization/training

## Assumptions

- Normalizatoin improves model performance
- Median usage improves the dataset
- Threshold based dropping is more clear, as high NaN's in a row leads to bad data
