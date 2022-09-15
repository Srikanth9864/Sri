from json import loads
from requests import  request
from json import loads
from pytest import mark
#loads---->load a Json String
headers = "code ,expected_branch"
data = [
    ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
    ("SBIN0003238", "KALUVOY"),
    ("ICIC0000002", "BANGALORE - M G ROAD")
    ]
@mark.parametrize(headers,data)
def test_API(code,expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    response = request("GET",url)
    #  Deserialisation(Converting a Json string into a Python Data Structure)
    d = loads(response.text)
    actual_branch = d["BRANCH"]
    assert actual_branch == expected_branch
    # Parse the Response
    