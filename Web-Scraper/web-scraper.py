import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["value1", "value2", "value3"])

webpage = requests.get("")
soup = BeautifulSoup(webpage.content, "html.parser")
container = soup.select_one("")

for con in container:
    value1 = container.select_one("")
    value2 = container.select_one("")
    value3 = container.select_one("")
    
    sheet.append([value1, value2, value3])


wb.save("File.xlsx")
