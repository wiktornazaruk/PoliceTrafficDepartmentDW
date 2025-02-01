# Police Traffic Department Data Warehouse

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Scripts](#scripts)
6. [Visualization](#visualization)

## Introduction

The PoliceTrafficDepartmentDW project is designed to create a data warehouse for managing and analyzing police traffic department data. It includes various scripts and files for data extraction, transformation, and loading (ETL), database management, and data visualization.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/wiktornazaruk/PoliceTrafficDepartmentDW.git
   cd PoliceTrafficDepartmentDW
   ```

2. Ensure you have the necessary software installed:

   - SQL Server
   - Python (with required packages listed in `requirements.txt`)
   - R (if using the R scripts)

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Detailed instructions on how to use the project, including data loading and running ETL processes:

1. **Data Generation**: Use the `generate_data.py` script to create sample data.

   ```bash
   python generate_data.py
   ```

2. **Database**: Use SQL scripts in `DB` directory for database setup.

3. **Data Warehouse**: Use SQL scripts in `DW` directory for data warehouse setup.

4. **ETL Process**: Use SQL scripts in `ETL` directory for ETL process.

## File Structure

- **DB/**: Contains database-related files and SQL scripts.
- **DW/**: Data warehouse schema and related files.
- **ETL/**: Scripts and tools for Extract, Transform, Load processes.
- **visualizations/**: Contains files related to visualizations.
- **clear_cache/**: Contains scripts for cleaning cache files.
- **README.md**: Project documentation.
- **generate_data.py**: Script to generate sample data.
- **gdansk_districts.json**: Gdansk districts and streets.
- **rating_comments.json**: Comments about police interventions.
- **optimization.R**: An R script for comparing ROLAP, MOLAP and HOLAP approaches efficiency.
- **queries.mdx**: MDX queries for data analysis.

## Scripts

### `generate_data.py`

A Python script to generate sample traffic data for the data warehouse.

### `clear_cache.sql`

SQL script to clear cache in the database.

### `optimization.R`

An R script for comparing ROLAP, MOLAP and HOLAP approaches efficiency.

## Visualization

The project includes a Power BI file (`visualizations.pbix`) for data visualization. Open this file in Power BI to explore the visualized data and gain insights.

### Example visualizations

<a href="/visualizations/visualizations.pdf" target="_blank">See visualizations.pdf</a>
