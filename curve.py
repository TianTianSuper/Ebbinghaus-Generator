import numpy as np
import datetime
from datetime import timedelta


class RememberList:
    def __init__(self, vocabulary_size, start_date=None, remember_per_day=3):
        self.vocabulary_size = vocabulary_size
        self.rules = [0,1,2,4,7,15]
        period_length = self.vocabulary_size + self.rules[-1]
        self.records = dict()
        self.remember_per_day = remember_per_day

        if start_date is None:
            self.start_date = datetime.datetime.now()
        elif isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        elif isinstance(start_date, datetime.datetime):
            self.start_date = start_date
        self.end_date = self.start_date + timedelta(days=period_length)

    def order_dict(self, old_dict):
        new_dict = dict()
        ordered_keys = sorted(old_dict)
        for index in ordered_keys:
            new_dict[index] = self.records[index]
        return new_dict

    def generate(self):
        all_list_index = np.arange(1, self.vocabulary_size + 1)
        group_list_index = [all_list_index[i-1:i-1+self.remember_per_day].tolist()\
                                for i in all_list_index[::self.remember_per_day]]
        new_day = 0
        for group in group_list_index:
            today = self.start_date + timedelta(days=new_day)
            review_days = [(today + timedelta(day)).strftime('%Y-%m-%d') for day in self.rules]
            for day in review_days:
                if day == today.strftime('%Y-%m-%d'):
                    if day in self.records.keys():
                        self.records[day][0].extend(group.copy())
                    else:
                        self.records[day] = [group.copy(), []]
                else:
                    if day in self.records.keys():
                        self.records[day][-1].extend(group.copy())
                    else:
                        self.records[day] = [[], group.copy()]
            new_day += 1
        print(self.order_dict(self.records))
      
