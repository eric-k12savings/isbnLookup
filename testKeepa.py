import keepa

key = '2j4bf6lfiv208j4k6uucipohij1n91g56705ov38our7c1jn4igegseb4n6tcf1p'
api = keepa.Keepa(key)

# Single ASIN query
products = api.query('9781256745440', product_code_is_asin=False, domain='US', buybox= True, rating= True) # returns list of product data
#products = api.query('B0CP9Z1S51') # returns list of product data
print(products[0].keys())
print(products[0]['isB2B'])
print(products[0]['data']['NEW'][0])


