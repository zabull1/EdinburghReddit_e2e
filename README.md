# Edinburgh Reddit E2E Data Pipeline Project

<p align="center">
<img src="assets/architecture/edinburgh_city.jpeg" width="1000">
</p>

I recently finished my MSc in Data Science at Heriot-Watt University. Being an international student, I was keen to connect with the vibrant city of Edinburgh on a deeper level. To achieve this, I undertook a data engineering project that explores the vast amount of information available on the r/Edinburgh subreddit using the Reddit API. This project not only provides an exciting opportunity to apply my data engineering skills but also offers a unique perspective on the pulse of the local community and gives me insights into the current happenings around me.

This project offers a data pipeline solution that enables the extraction, transformation, and loading (ETL) of data from the Reddit (r/Edinburgh subreddit) API into a Redshift data warehouse. The pipeline utilizes tools and services such as Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, and Amazon Athena, and finally, the data is visualized in a dashboard with Tableau.

## Table of Content

- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [API Data Description](#api-data-description)
- [Project Structure](#Project-Structure)
- [Prerequisite](#prerequisites)
- [Usage](#usage)
- [DashBoard](#dashboard)
- [Improvements](#improvements)
- [Reference](#reference)
- [License](#license)

## Overview

The pipeline is designed to:

1. Extract data from r/Edinburgh subreddit using Reddit API.
2. Store the raw data into an S3 bucket from Airflow.
3. Transform the data using AWS Glue and Amazon Athena.
4. Load the transformed data into Amazon Redshift for analytics and querying.
5. Visualised the data in Tableau

## Architecture

<p align="center">
<img src="assets/architecture/EdinburghRedditArchitecture_.drawio.png" width="1000">
</p>

## Technologies

- Cloud: `AWS`
- Infrastructure: `Terraform`
- Orchestration: `Airflow`
- Data lake: `Amazon S3`
- Data transformation: `Amazon Athena`
- Data warehouse: `Amazon Redshift`
- Data visualization: `Tableau`

## API Data Description

| Column           | Description                                      |
|------------------|--------------------------------------------------|
| `id`        | Unique identifier for the Reddit post            |
| `title`          | Title of the Reddit post                         |
| `score`          | Score associated with the post                   |
| `num_comments`   | Number of comments on the post                   |
| `author`         | Username of the post author                      |
| `created_utc`    | UTC timestamp when the post was created         |
| `url`            | URL associated with the post                     |
| `over_18`    | Indicates whether the post contains mature content (18+) |
| `edited`     | Timestamp indicating when the post was last edited |
| `spoiler`    | Indicates if the post contains spoiler content    |
| `stickied`   | Indicates if the post is stickied at the top of the subreddit |

<!-- ## Project Structure

project-root
 ├── assets
 ├── config
 ├── dags
 ├── data
 ├── iaas
 ├── logs
 ├── plugins
 ├── notebooks
 ├── scripts
 ├── src
 ┃ ├── etl
 ┃ ┃ ├── reddit_etl.py
 ├── tests
 ├── venv
 ├── requirements.txt
 ├── airflow.env
 ├── docker-compose.yml
 ├── Dockerfile
 ├── README.md
 ├── requirements.txt

project-root
 ├── notebooks         # Jupyter notebooks for exploratory data analysis and development
 ├── src               # Source code for data processing, ETL, and analysis
 ┃ ├── etl            # ETL (Extract, Transform, Load) scripts and modules
 ┃ ┃ ├── reddit_etl.py # Reddit data extraction and transformation script
 ├── data              # Data directory for storing raw and processed datasets
 ├── docs              # Documentation, project reports, and relevant resources
 ├── requirements.txt  # List of project dependencies and their versions
 ├── README.md         # Project overview, documentation, and instructions -->

## Prerequisites

- Access to AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation
- Python 3.9 or higher
- Tableau Installation
- Basic knowledge of Python programming
- Familiarity with data engineering concepts
- Basic knowledge of command-line

## Usage

1. Clone the repository.

   ```bash
    git clone https://github.com/zabull1/EdinburghReddit_e2e.git
   ```

2. Create a virtual environment.

   ```bash
    python3 -m venv venv
   ```

3. Activate the virtual environment.

   ```bash
    source venv/bin/activate
   ```

4. Install the dependencies.

   ```bash
    pip install -r requirements.txt
   ```

5. Rename the configuration file and the credentials to the file.

   ```bash
    mv config/config.conf.example config/config.conf
   ```

6. Starting the containers

   ```bash
    docker-compose up airflow-init
    docker-compose up -d 
   ```

7. Launch the Airflow web UI.

   ```bash
    open http://localhost:8080

## DashBoard

## Improvements

- 1. Unit testing
- 2. Infrastructure as code
- 3. Tableau dashboard

<!-- ## Reference -->

## License

This project is licensed under the MIT License - see the [LICENSE](https://mit-license.org/) file for details.
