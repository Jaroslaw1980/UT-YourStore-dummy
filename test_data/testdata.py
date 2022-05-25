

class DataFeeder:
    
    def data_feeder(cell):
        import openpyxl
        book = openpyxl.load_workbook('C:/Python/Selenium/UTYourStore/test_data/test.xlsx')
        sheet = book.active
        celldata = sheet[cell].value
        return celldata