from curve import RememberList

if __name__ == '__main__':
    r = RememberList(31, start_vocab=11, remember_per_day=4)
    r.generate()