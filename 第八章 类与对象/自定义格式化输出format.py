_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self,code):
        val = _formats.get(code,'{d.year}-{d.month}-{d.day}')
        return val.format(d=self)

d = Date(2011,5,11)
print(format(d))
format()
