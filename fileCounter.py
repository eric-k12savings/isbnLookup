import pandas as pd
from isbnlib import to_isbn13
import keepa


key = '2j4bf6lfiv208j4k6uucipohij1n91g56705ov38our7c1jn4igegseb4n6tcf1p'
api = keepa.Keepa(key)
records = []

print("Starting Process -------------------------------")

with open("keepaDataComma.txt", "r") as file:
    print("...Reading File...")
    content = file.read()
    asins = content.split(',')


for asin in range(10):
    print(f'Iteration: {asin}')
    record = {}
    stringAsin = str(asins[asin])
    products = api.query(stringAsin, domain='US', progress_bar=False)
    usedPrice = products[0]['data']['NEW'] 
    percentageIncrease = (usedPrice[-1] * .25)
    print("...Getting Price...")   

    if to_isbn13(stringAsin) != '':
        print("...Has 978...")
        record ["ISBN"] = f'NBS{to_isbn13(stringAsin)}'
        record ["asin"] = asins[asin]
        record ["Price"] = round((usedPrice[-1] + percentageIncrease), 2)
    else:
        print("...No 978...")
        continue

    records.append(record)


print("...Stuffing Data into excel sheet...")
df = pd.DataFrame(records)
df.to_excel("keepaData.xlsx", index=False)
print("-------------------------------Ending Process")