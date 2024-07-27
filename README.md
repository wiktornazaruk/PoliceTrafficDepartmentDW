# Police Traffic Department Data Warehouse

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Scripts](#scripts)
6. [Visualization](#visualization)
7. [Contributing](#contributing)
8. [License](#license)

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

2. **Database Management**: Use SQL scripts for database setup and cache clearing:
    ```sql
    -- Run these in your SQL environment
    clear_cache.sql
    ```

3. **ETL Process**: Follow the instructions in the `ETL` directory to load and transform data.

## File Structure

- **DB/**: Contains database-related files and SQL scripts.
- **DW/**: Data warehouse schema and related files.
- **ETL/**: Scripts and tools for Extract, Transform, Load processes.
- **README.md**: Project documentation.
- **clear_cache.sql**: Script to clear the database cache.
- **clear_cache_xml.xmla**: XMLA script for cache clearing.
- **generate_data.py**: Script to generate sample data.
- **optimization.R**: R script for optimization tasks.
- **queries.mdx**: MDX queries for data analysis.
- **visualizations.pbix**: Power BI file for data visualization.

## Scripts

### `generate_data.py`
A Python script to generate sample traffic data for the data warehouse.

### `clear_cache.sql`
SQL script to clear cache in the database.

### `optimization.R`
An R script for performing optimization tasks on the data.

## Visualization

The project includes a Power BI file (`visualizations.pbix`) for data visualization. Open this file in Power BI to explore the visualized data and gain insights.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
