import datetime
import numpy as np

class DateCalculator():
    def __init__(
            self,  
            endDate: tuple, 
            startDate: tuple = None,
            weekmask: str | list = None, 
            holidays: list = None
        ):
        if startDate is None:
            self.start = start = datetime.datetime.now().date()
        else:
            startDay = startDate[2]
            startMonth = startDate[1]
            startYear = startDate[0]
            self.start = datetime.date(startYear, startMonth, startDay)
        endDay = endDate[2]
        endMonth = endDate[1]
        endYear = endDate[0]        
        self.end = datetime.date(endYear, endMonth, endDay)
        if weekmask is not None:
            self.weekmask = weekmask
        else:
            self.weekmask = "1111111"
        if holidays is not None:
            self.holidays = holidays
        else:
            self.holidays = []
    def __str__(self) -> str:
        return str(self.calculate())
    def calculate(self) -> int:
        return np.busday_count(self.start, self.end, holidays=self.holidays, weekmask=self.weekmask)