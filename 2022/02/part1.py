from enum import Enum


POINT_HAND = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6
}


class Options(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"

    def __gt__(self, other):
        return self.value == self.ROCK.value and other.value == self.SCISSORS.value \
            or self.value == self.SCISSORS.value and other.value == self.PAPER.value \
            or self.value == self.PAPER.value and other.value == self.ROCK.value


class PlayerHand(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class ElfHand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    def __and__(self, player_hand: PlayerHand):
        """Validates the round game"""
        round_score = 0
        round_score += POINT_HAND[
            str(player_hand.name)
        ]
        if self.name == player_hand.name:
            round_score += POINT_HAND["DRAW"]
        elif Options(self.name) > Options(player_hand.name):
            round_score += POINT_HAND["LOSE"]
        else:
            round_score += POINT_HAND["WIN"]

        return round_score


with open("input.in", 'r') as file:
    final_game_score = 0
    for line in file:
        final_game_score += ElfHand(line[0]) & PlayerHand(line[2])
    print("Part 1:", final_game_score)
