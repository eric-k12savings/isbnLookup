import keepa





key = '2j4bf6lfiv208j4k6uucipohij1n91g56705ov38our7c1jn4igegseb4n6tcf1p'
api = keepa.Keepa(key)
# asins = api.best_sellers_query(283155, domain='US', wait=True)
# with open("keepaDataTab.txt", 'w') as file:
#     file.write('\t'.join(asins))






# Single ASIN query
#products = api.query('1686456964')
# print(products)
products = api.query('0241351820', domain='US', progress_bar=False)
usedPrice = products[0]['data']['NEW']
print(usedPrice[-1])



