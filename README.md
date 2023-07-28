# Real-time-streaming-data-pipeline-with-Apache-Kafka-and-Snowflake

## Description: Real-time streaming data pipeline with Apache Kafka, Python, and Snowflake

## Tools/Technologies Used

* Windows 10
* [Python](https://www.python.org/downloads/release/python-3913/): for generating fake data
* [Snowflake](https://www.snowflake.com/en/)
* [Python Connector API](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#module-snowflake-connector)
* [Apache Kafka](https://kafka.apache.org/downloads):  distributed streaming platform used to build real-time data pipelines and streaming applications. Place Kafta folder in the C: drive

## Installation
* Check [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-install-and-run-apache-kafka-on-windows/) for installation of Apache Kafka and configuration of zookeeper.properties and server.properties files.
* Configure the `zookeeper.properties` and `server.properties` files located in the config folder of Kafka.
* Copy the Snowflake connect properties [file](./resources/snowflake_connect.properties) in resources folder and place in the config folder of Kafka.
* Modify the Snowflake connect properties [file](./resources/snowflake_connect.properties).

## Usage
* Locate the [sample_env](./scripts/sample_env) script in the scripts folder and replace the dummy environment variables.
* Run the [initial_setup.py](./utils/sf_initial_setup.py) script to create the database and schema.
* Generate the public and private key for Snowflake
  ```
    # private key 
    openssl genrsa -out rsa_key.pem 2048

    # private key
    openssl rsa -in rsa_key.pem -pubout -out rsa_key.pub
  
     -- apply the public key to your user in Snowflake
    ALTER USER <your_user>
    SET RSA_PUBLIC_KEY = ''
  ```
* Start the zookeeper-server, kafka-server, and the snowflake_standalone server in separate terminals
  ```
  # zookeeper-server
  .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
  
  # kafka-server
  .\bin\windows\kafka-server-start.bat .\config\server.properties
  
  # snowflake_standalone server
  .\bin\windows\connect-standalone.bat config/connect-standalone.properties config/snowflake_connect.properties
  ```
* Create, list, read or delete a topic
  ```
  # create a topic
  .\bin\windows\kafka-topics.bat --create --topic shop-data --bootstrap-server localhost:9092
  
  # list all topics
  .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
  
  # read topic
  .\bin\windows\kafka-console-consumer.bat --topic shop-data --from-beginning --bootstrap-server localhost:9092
  
  # delete topic
  .\bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --delete --topic shop-data
  
  ```
* Run the [generate_customer_data.py](./utils/generate_customer_data.py) to generate data
* Don't forget to stop the servers and drop the SHOP_DB after use.