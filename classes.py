# This is the beginning of ShulerOnline project

import random


class CardDeck:

    def __init__(self):
        self.amount = 36

        # D - diamonds, H - hearts, C - clubs, S - spades
        # A - 10, B - knave, C - queen, D - king, E - A
        self.cards = [
            'D6', 'D7', 'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'DE',
            'H6', 'H7', 'H8', 'H9', 'HA', 'HB', 'HC', 'HD', 'HE',
            'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE',
            'S6', 'S7', 'S8', 'S9', 'SA', 'SB', 'SC', 'SD', 'SE'
        ]

        self.trump = self.cards[0]

    def mix(self):
        for i in range(256):
            ind1 = random.randint(0, self.amount - 1)
            ind2 = random.randint(0, self.amount - 1)
            self.cards[ind1], self.cards[ind2] = self.cards[ind2], self.cards[ind1]

        self.trump = self.cards[0]

    def get(self) -> str:
        ans = ''

        if self.amount:
            self.amount -= 1
            ans = self.cards.pop(-1)

        return ans


class Player:

    def __init__(self, name):
        # name of a player
        self.name = name
        # num of cards in player's hand
        self.amount = 0
        # cards in player's hand
        self.hand_deck = []

    def get_card(self, *cards):
        for card in cards:
            self.amount += 1
            self.hand_deck.append(card)

    def put_card(self, card):
        if card in self.hand_deck:
            self.amount -= 1
            self.hand_deck.remove(card)

# c_on_t - card on table, inp - player's input
def check_card(c_on_t, inp, tr):
    if inp[0] == c_on_t[0]:
        return inp[1] > c_on_t[1]
    else:
        return inp[0] == tr


class Lobby:

    def __init__(self, max_lobby: int, lobby_id: int, cheats_allowed: bool):

        self.max_lobby = max_lobby
        self.lobby_id = lobby_id
        self.cheats_allowed = cheats_allowed
        self.current_deck = CardDeck()
        self.table = {}
        self.used = []
        self.current_players = []
        self.player_index = 0

    def start_new_game(self):

        self.current_deck.mix()
        self.player_index = random.randint(0, len(self.current_players))

    def put_on_table(self, player: Player, card: str):

        player.put_card(card)
        self.table.update({card: 0})

    def cover_card(self, player: Player, t_card: str, c_card: str):

        if check_card(t_card, c_card, self.current_deck.trump):
            player.put_card(c_card)
            self.table.update({c_card: 0, t_card: 0})
            self.used.append(c_card)
            self.used.append(t_card)





