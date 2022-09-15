from requests import request
from pytest import mark

headers = "page"
pages = [ ('login',), ('register', ), ('cart',), ('iphone', ), ('electronics',),
        ('wishlist',), ('books', ), ('computers', ), ('desktops', ), 
        ('notebooks', ), ('accessories',), ('hello',),
        ('electronics,'),('camera-photo',), 
        ('cell-phones',), ('apparel-shoes',), 
        ('digital-downloads',), ('jewelry',), 
        ('gift-cards',), ('iphone',)
        ]

@mark.parametrize("page", pages)
def test_api_sanity(page):
    url = f"http://demowebshop.tricentis.com/{page[0]}"
    response = request("GET", url)
    assert response.status_code == 200