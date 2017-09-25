import random


class Player:
    def __init__(self, name, sequence_number, score_list):
        self.n = name
        self.sn = sequence_number
        self.sl = score_list


class Roster:
    def __init__(self):
        self.score_sum_list =list()
        self.score_list = list()
        self.sequence_list = list()
        self.list_players = list()
        self.number_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen']

    def get_player_name_list(self):
        return ['Robo ' + word for word in self.number_list]

    def get_player_sequnce_number(self):
        return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))

    def get_player_score_list(self):
        return [int(random.choice('123456')) for i in range(3)]

    def get_player_list(self):
        while len(self.score_list) < 15:
            if len(self.score_list) == 0:
                score = self.get_player_score_list()
                sequence = self.get_player_sequnce_number()
                self.score_list.append(score)
                self.score_sum_list.append(sum(score))
                self.sequence_list.append(sequence)
            else:
                score = self.get_player_score_list()
                sequence = self.get_player_sequnce_number()
                self.score_sum_list.append(sum(score))
                if sequence not in self.sequence_list and \
                                sum(score) not in self.score_sum_list[:-1] and \
                                sum(self.score_sum_list) < 175:
                    self.score_list.append(score)
                    self.sequence_list.append(sequence)
                else:
                    self.score_sum_list.pop()

        for x in range(15):
            self.list_players.append(Player(self.get_player_name_list()[x],
                                       self.sequence_list[x], self.score_list[x]))
        return self.list_players

'''
Roster = Roster()

for player in Roster.get_player_list():
    print(player.n, player.sn, player.sl)

print(sum(Roster.score_sum_list))
'''
# end of code
