from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from durak import DECK

PORT_NO = 37020
PORT_NO_AUX = 37021


class Card(Button):
    nominal = StringProperty()
    suit = StringProperty()
    opened = BooleanProperty(True)
    selected = BooleanProperty(False)
    counter = NumericProperty(-1)
    rotation = NumericProperty(0)

    def update_text(self, *_):
        if self.counter >= 0:
            # это колода. текст = кол-во карт
            self.text = str(int(self.counter))
            if self.counter > 1:
                self.background_normal = 'images/deck.png'
                self.background_down = 'images/deck.png'
            else:
                self.background_normal = 'images/back.png'
                self.background_down = 'images/back.png'
            # self.color = (1, 1, 1, 1)
        elif not self.opened:
            # карта закрыта (рука соперника)
            self.background_normal = 'images/back.png'
            self.background_down = 'images/back.png'
            # self.color = (0, 0.5, 0, 1)
        else:
            # карта открыта
            s, n = self.suit, self.nominal
            self.background_normal = f'images/cards/{s}{n}.png'
            self.background_down = f'images/cards/{s}{n}.png'

    def update_prediction(self, n_text):
        self.text = n_text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.target_position = (100, 100)
        self.target_rotation = 0
        self.bind(counter=self.update_text)
        self.bind(opened=self.update_text)

    def set_animated_targets(self, x, y, ang):
        self.target_position = x, y
        self.target_rotation = ang

    def set_immeditate_attr(self, x, y, ang):
        self.pos = x - self.width / 2, y - self.height / 2
        self.rotation = ang

    def bring_to_front(self):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(self)

    @property
    def as_tuple(self):
        return self.nominal, self.suit

    def destroy_card_after_delay(self, delay):
        def finisher(*_):
            if self and self.parent:
                self.parent.remove_widget(self)

        Clock.schedule_once(finisher, delay)

    @classmethod
    def make(cls, card, opened=True):
        card_widget = Card()
        card_widget.nominal, card_widget.suit = card
        card_widget.opened = opened
        card_widget.update_text()
        return card_widget


