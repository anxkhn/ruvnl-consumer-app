from ruvnl_consumer_app.app import fetch_data
DEFAULT_DATA_URL = "http://sldc.rajasthan.gov.in/rrvpnl/read-sftp?type=overview"
data = fetch_data(DEFAULT_DATA_URL)
print(data)


