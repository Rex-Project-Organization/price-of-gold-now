"""
Price of Gold Now App
"""
import priceofgold as pog

if __name__ == '__main__':
    print('Aplikasi utama')
    result = pog.data_extract()
    pog.show_data(result)
