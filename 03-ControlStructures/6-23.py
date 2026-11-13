ean = input('Enter EAN-13 article number: ')

# najpierw sprawdzam długość i czy składa się z samych cyfr
if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')
    # zagnieżdżam drugi if: sprawdzam pierwsze trzy znaki tylko wtedy, gdy cały kod był poprawny
    if ean[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Incorrect article number')