from requests import request
from json import loads
from pytest import mark
from csv import reader

def read_csv():
    with open("./data_files/bank.csv") as f:
        data = [ ]
        rows = reader(f)
        headers = next(rows)
        for row in rows:
            data.append(tuple(row))
    return data

headers = "code, expected_branch"
data = read_csv()

# data = [
#     ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
#     ("SBIN0040014", "GANDHI BAZZAR"),
#     ("ICIC0000002", "BANGALORE - M G ROAD")
#     ]

@mark.parametrize(headers, data)
def test_bank(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    print(url)
    # loads ----> Load a JOSN string
    # Hit the request
    response = request("GET", url)
    # Get the text from response object
    response_text = response.text
    print(response_text)
    # Deserilisation (Converting JSON String into Python Data Structure)
    d = loads(response_text)
    # Parse the Response
    actual_branch = d['BRANCH']
    assert actual_branch == expected_branch