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

    def get_lose_option(self):
        if self.value == self.ROCK.value:
            return self.PAPER.value
        if self.value == self.PAPER.value:
            return self.SCISSORS.value
        if self.value == self.SCISSORS.value:
            return self.ROCK.value

    def get_draw_option(self):
        if self.value == self.ROCK.value:
            return self.ROCK.value
        if self.value == self.PAPER.value:
            return self.PAPER.value
        if self.value == self.SCISSORS.value:
            return self.SCISSORS.value

    def get_win_option(self):
        if self.value == self.ROCK.value:
            return self.SCISSORS.value
        if self.value == self.PAPER.value:
            return self.ROCK.value
        if self.value == self.SCISSORS.value:
            return self.PAPER.value


class ElfHand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    def __and__(self, response_hand: PlayerHand):
        """Validates the round game"""
        round_score = 0
        round_score += POINT_HAND[
            str(response_hand.name)
        ]
        if self.name == response_hand.name:
            round_score += POINT_HAND["DRAW"]
        elif Options(self.name) > Options(response_hand.name):
            round_score += POINT_HAND["LOSE"]
        else:
            round_score += POINT_HAND["WIN"]

        return round_score


# ====================== Second Part ==================
class GameCondition(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


with open("input.in", 'r') as file:
    final_game_score = 0
    for line in file:
        elf_hand = ElfHand(line[0])
        player_hand = PlayerHand[elf_hand.name]

        # Get the condition for the game
        if line[2] == GameCondition.LOSE.value:
            final_game_score += elf_hand & PlayerHand(player_hand.get_win_option())
        elif line[2] == GameCondition.DRAW.value:
            final_game_score += elf_hand & PlayerHand(player_hand.get_draw_option())
        else:  # The round must be won
            final_game_score += elf_hand & PlayerHand(player_hand.get_lose_option())

    print("Part 2:", final_game_score)
