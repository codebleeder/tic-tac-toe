class Board:
    def __init__(self, human_symbol, ai_symbol):
        self.arr = [' ']*9
        self.human_symbol = human_symbol
        self.ai_symbol = ai_symbol

    def print_board(self):
        for i in range(9):
            if i == 0 or i == 1 or i == 4 or i == 7:
                print self.arr[i], '|',
            elif i == 3 or i == 6:
                print '---------'
                print self.arr[i], '|',
            elif i == 2 or i == 5 or i == 8:
                print self.arr[i]

    def make_human_entry(self, cell_num):
        if self.arr[cell_num-1] == ' ':
            self.arr[cell_num-1] = self.human_symbol
            return True
        else:
            return False

    def is_board_full(self):
        if ' ' in self.arr:
            return False
        else:
            print 'Its a Draw!'
            return True

    def get_arr(self):
        return self.arr

    def get_symbols(self):
        return {'human_symbol': self.human_symbol, 'ai_symbol': self.ai_symbol}

    def make_entry(self, index, symbol):
        self.arr[index] = symbol
