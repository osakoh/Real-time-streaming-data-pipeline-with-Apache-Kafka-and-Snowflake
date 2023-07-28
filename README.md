# Real-time-streaming-data-pipeline-with-Apache-Kafka-and-Snowflake

## Description: Real-time streaming data pipeline with Apache Kafka, Python, and Snowflake

## Tools/Technologies Used

* Windows 10
* [Python](https://www.python.org/downloads/release/python-3913/): for generating fake data
* [Snowflake](https://www.snowflake.com/en/)
* [Python Connector API](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#module-snowflake-connector)
* [Apache Kafka](https://kafka.apache.org/downloads):  distributed streaming platform used to build real-time data pipelines and streaming applications

## Installation
* Check [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-install-and-run-apache-kafka-on-windows/) for installation of Apache Kafka and configuration of zookeeper.properties and server.properties files.
* Configure the `zookeeper.properties` and `server.properties` file accordingly

## Usage
* Locate the [sample_env](./scripts/sample_env) script in the scripts folder and replace the dummy environment variables.
* Run the [initial_setup.py](./utils/sf_initial_setup.py) script to create the database and schema.