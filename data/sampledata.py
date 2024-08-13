import os
import csv
from datetime import datetime, timedelta
import random


local_path = "/Users/mac/AZDEC/script"  
file_name = "kowope-daily-reports.csv"

os.makedirs(local_path, exist_ok=True)

# Generate sample data
def generate_sample_data(num_records=100):
    headers = ["Date", "TransactionID", "CustomerID", "Amount", "Currency", "Status"]
    data = []

    for i in range(num_records):
        date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        transaction_id = f"TID-{random.randint(1000, 9999)}"
        customer_id = f"CID-{random.randint(10000, 99999)}"
        amount = round(random.uniform(10.0, 1000.0), 2)
        currency = random.choice(["USD", "EUR", "GBP", "NGN"])
        status = random.choice(["Completed", "Pending", "Failed"])
        
        data.append([date, transaction_id, customer_id, amount, currency, status])
    
    return headers, data


def write_to_csv(local_path, file_name, headers, data):
    file_path = os.path.join(local_path, file_name)
    
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"Sample data written to {file_path}")


headers, data = generate_sample_data()
write_to_csv(local_path, file_name, headers, data)
