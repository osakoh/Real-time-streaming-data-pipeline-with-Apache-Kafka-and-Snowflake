# import dependencies
import random
from datetime import datetime
from json import dumps
from time import sleep

from faker import Faker
from kafka import KafkaProducer


def generate_customer_data(num_of_customers):
    """
    Function that generates the customers data

    num_of_customers: # represents the number of customers to be generated
    """
    fake = Faker('en_US')
    # initializes an empty dictionary named customers, which will be used to store the generated customer data
    customers = dict()
    #  name of the Kafka topic where the data will be sent
    topic_name = 'sales-data'

    # creates an instance of the KafkaProducer class with the bootstrap servers set to ['localhost:9092']
    # sets the value serializer to convert the Python object into a JSON-encoded string.
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

    for customers_id in range(num_of_customers):
        # Create transaction date
        #  creates a datetime object d1 by parsing the string '1/1/2021', using the format '%m/%d/%Y' (month/day/year)
        first_date = datetime.strptime(f'1/1/2022', '%m/%d/%Y')
        # creates a datetime object d2 by parsing the string '8/10/2021', using the format '%m/%d/%Y' (month/day/year)
        second_date = datetime.strptime(f'20/12/2022', '%m/%d/%Y')
        # generates a random date between d1 and d2 using the date_between() method from the fake object
        transaction_date = fake.date_between(first_date, second_date)

        # line generates a random name customers' name using the name() method
        name = fake.name()

        # Create gender: randomly selects a gender from the list ["M", "F"]
        gender = random.choice(["M", "F"])

        # Create email: generates a random email address using the ascii_email()
        email = fake.ascii_email()

        # Create city: generates a random city name using the city()
        city = fake.city()

        # create product ID in 8-digit barcode: generates a random 8-digit barcode using the ean()
        product_id = fake.ean(length=8)

        # creates amount spent: generates a random float number with 2 DPs between 1 and 100 using the pyfloat()
        amount_spent = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=100)

        # representing the generated customer data
        customers = {
            'transaction_date': str(transaction_date),
            'name': name, 'gender': gender, 'city': city,
            'email': email, 'product_id': product_id,
            'amount_spent': amount_spent
        }

        # print the customers' data
        print(f"customers => {customers}")

        # sends the generated customer data as a JSON-encoded string to the Kafka topic
        producer.send(topic_name, value=dumps(customers))
        # runs every 3 secs
        sleep(3)
