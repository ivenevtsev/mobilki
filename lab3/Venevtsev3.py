import csv
import time
from num2t4ru import num2text, decimal2text
from docxtpl import DocxTemplate
from docx2pdf import convert
from win32com import client
import decimal

filename = input("Enter the path to the csv file: ")
ip = input("Enter the Numder to check: ")

rows1 = []
teleint = 0
teleout = 0
sms = 0
with open(filename, 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows1.append(row)
        
def check_teleint():
    global teleint
    for row in rows1[:reader.line_num]:
        if ip in row[1]:
            teleint += float(row[3])
    return teleint
def check_teleout():
    global teleout
    for row in rows1[:reader.line_num]:
        if ip in row[2]:
            teleout += float(row[3])
    return teleout
def check_sms():
    global sms
    for row in rows1[:reader.line_num]:
        if ip in row[1]:
            sms += int(row[4])
    return sms
x = 3*check_teleint()+check_teleout()
z = check_sms()

filename = input("Enter the path to the csv file: ")
ip = input("Enter the IP address to check: ")

rows = []
fields = []
k = 1.0
bonus = 1000.0
inp = 0
out = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows.append(row)
        
def inp_trf():
    global inp
    for row in rows[:reader.line_num]:
        if ip in row[4]:
            inp += int(row[12])            
    return inp

def out_trf():
    global out
    for row in rows[:reader.line_num]:
        if ip in row[3]:
            out += int(row[12])
    return out
traf_sum_mb = (inp_trf() + out_trf()) / 1048576
All = (traf_sum_mb - bonus)*k
while All<0:
    bonus /= 1024
    All = (traf_sum_mb - bonus)*k
y= All
x = float('{:.2f}'.format(x))
y = float('{:.2f}'.format(y))
z = float('{:.2f}'.format(z))
nds = (z+x+y)*0.2
nds = float('{:.2f}'.format(nds))
int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')
summ = str(decimal2text(
        decimal.Decimal(str(x+y+z)),
        int_units=int_units,
        exp_units=exp_units))
doc = DocxTemplate("template.docx")
context = {'bank' : 'АО "Четыре папочки" г. Санкт-Петергург','inn' : "4444444444", 
           'kpp' : "4440000444", 'name' : 'АО "Четыре папочки холдинг"', 'bik' : '101404101',
           'sch1' : "44444444444444440000", 'sch2' : "11111111111111000000",
           'postav' : 'АО "Четыре папочки холдинг", ИНН 4444444444, КПП 4440000444, 111444, Санкт-Перербург г Лучшая ул, дом №4, строение 1', 'schetnum' : 444,
           'day' : 4, 'month' : "апреля", 'year' : 20, 'pokup' : 'ООО "На созвоне", ИНН 5555500000, КПП 555111155, 11155, Санкт-Перербург г Потоковая ул, дом №1, строение 2', 'ocnov' : "№44004400 от 4.04.2014", 'telesum' : x, 'intsum' : y,
           'sum' : x+y+z , 'nds' : nds , 'all' : summ, 'director' : "Веневцев И.В.", 'buh' : "Милосердов Д.И.", 'tele' : "Телефония", 'smssum' : z, 'sms' : "СМС", 'int' : "Интернет траффик"}
doc.render(context)
doc.save("schet.docx")
convert("schet.docx")