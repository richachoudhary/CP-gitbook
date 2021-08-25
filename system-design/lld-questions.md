# LLD:Questions

## 0. Template 🔖

```text
# Name: <app_name>

# Objective:

# Features:
* 

# ====================================================

# Classes: (nouns)

* class1
    * attr1
    * attr2
    * method1(attr1, attr2)
    * method2(attr1)

# ==================================================== [forSelf]

## Steps for LLD:

1. create Project in VSCode
2. `Req Gathering` create `design.md` file as ^
3. `Creating Frames` create all the empty classes & their attrs, methods; (some things might change during as interview discussion moves).
    * NOTE: add basic `doc_string` descripiton as many places as you can - leaves good impression
4. `Implementation + UnitTesting` : do your thing. Also introduce abstraction/inheritance etc as per the need.
    * NOTE: Splint the screen & keep `main.py` open on right(along with what you're coding on left) => to continueously checking for bugs & correctness(hence avoinding the rabbit-hole-debugging in the end)
5. `Run + Integration Tests + Edge Cases + Bonus Features`
6. `Writing UTs` : if time permits
```



## 1. CardWars

{% tabs %}
{% tab title="main.py" %}
```python
from player import Player
from deck import Deck
from war_card_game import WarCardGame

player = Player("Nora", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_coumputer=True)
deck = Deck()

game = WarCardGame(player,computer, deck)

game.print_welcome_msg()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()
    
    # NOTE: comment out below to run till end of game
    ans = input("\n Are you ready for next round? Press ENTER to continue.Enter X to Stop.")
    
    if ans.lower() == 'x':
        break
    
```
{% endtab %}

{% tab title="card.py" %}
```python
class Card:

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self):
        return 11 <= self.value <= 14

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")
            

```
{% endtab %}

{% tab title="deck.py" %}
```python
import random
from card import Card
from suit import Suit


class Deck:

    SUITS = ("club", "diamond", "heart", "spade")

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for value in range(2, 15):
            for suit in Deck.SUITS:
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        self._cards.insert(0, card)

```
{% endtab %}

{% tab title="player.py" %}
```python
class Player:
    def __init__(self, name, deck, is_coumputer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_coumputer

    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        return self._deck.size == 0
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None
        
    def add_card(self,card):
        self._deck.add(card)
```
{% endtab %}

{% tab title="suit.py" %}
```python
class Suit:
    SYMBOLS = {"club": "♣", "diamond": "♦", "heart": "♥", "spade": "♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
```
{% endtab %}

{% tab title="war\_card\_game.py" %}
```python
class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, user):
        for i in range(26):
            card = self._deck.draw()
            user.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("\n === Lests start the battle ===\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f'Your Card:', end = ' ')
        player_card.show()
        print(f'Computer Card:', end = ' ')
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou've won this Round")
            self.add_cards_to_user(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe Computer has won this Round")
            self.add_cards_to_user(self._computer, cards_won)
        else:  # tie
            print("\n\n Its a Tie. This is a war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    # returns list
    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_user(self, user, list_of_cards):
        for card in list_of_cards:
            user.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for _ in range(3):
            player_card = self._player.draw_card()
            computer_card = self._computer.draw_card()

            player_cards.append(player_card)
            computer_cards.append(computer_card)

        print("Six Hidden cards: XXX XXX")
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("=========================================")
            print("|            Game Over                  |")
            print("=========================================")
            print("Try Again. The Computer Won")
            return True
        elif self._computer.has_empty_deck():
            print("=========================================")
            print("|            Game Over                  |")
            print("=========================================")
            print(f"Congrats {self._player.name}, you won!!")
            return True
        return False

    def print_stats(self):
        print("\n------")
        print(f"You have {self._player.deck.size} cards on your deck")
        print(f"The Computer has {self._computer.deck.size} cards on your deck")
        print("------")

    def print_welcome_msg(self):
        print("=========================================")
        print("|          War Card Game                 |")
        print("=========================================")

```
{% endtab %}
{% endtabs %}

## 2. TicTacToe\(Naive\)

{% tabs %}
{% tab title="main.py" %}
```python
from board import Board
from player import Player


print("**************")
print(" Tic-Tac-Toe!")
print("**************")

board = Board()
player = Player()
computer = Player("O", False)

board.print_board()

while True:
    # Ask human user move
    move = player.get_player_move()
    # Submit move
    board.submit_move(move, player)
    # Print board
    board.print_board()

    if board.is_move_valid(move) and board.is_winner(player, move[0], move[1]):
        print("You win!")
        break

    # Ask computer player move
    comp_move = computer.get_player_move()
    # Submit move
    board.submit_move(comp_move, computer)
    # Print board
    board.print_board()

    if board.is_winner(computer, comp_move[0], comp_move[1]):
        print("The Computer Won!")
        break

    if board.check_tie():
        print("There was a tie!")
        break
```
{% endtab %}

{% tab title="board.py" %}
```python
class Board:
    
    EMPTY = 0
    COLUMNS = {"A": 0, "B": 1, "C": 2}
    ROWS = (1, 2, 3)

    def __init__(self, game_board=None):
        if game_board:
            self.game_board = game_board
        else:
            self.game_board = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]

    def print_board(self):
        print("    A   B   C")
        for i, row in enumerate(self.game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end=" | ")
                else:
                    print("  | ", end="")
            print("\n---------------")

    def submit_move(self, move, player):
        if not self.is_move_valid(move):
            print("Invalid Input: Please Enter the row and column of your move (Example: 1A)")
            return
        else:
            row_index = int(move[0])-1
            col_index = Board.COLUMNS[move[1]]

            value = self.game_board[row_index][col_index]

            if value == Board.EMPTY:
                self.game_board[row_index][col_index] = player.marker
            else:
                print("This space is already taken.")

    def is_move_valid(self, move):
        return ((len(move) == 2)
            and (int(move[0]) in Board.ROWS)
            and (move[1] in Board.COLUMNS))

    def is_winner(self, player, row, col):
        if self.check_row(row, player):
            return True
        elif self.check_col(col, player):
            return True
        elif self.check_diagonal(player):
            return True
        elif self.check_antidiagonal(player):
            return True
        else:
            return False

    def check_row(self, row, player):
        row_index = int(row)-1
        board_row = self.game_board[row_index]

        if board_row.count(player.marker) == 3:
            return True
        else:
            return False

    def check_col(self, col, player):
        col_index = Board.COLUMNS[col]
        total_markers = 0

        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False
        
    def check_diagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False

    def check_antidiagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False

    def check_tie(self):
        total_empty = 0
        
        for row in self.game_board:
            total_empty += row.count(Board.EMPTY)

        if total_empty == 0:
            return True
        else:
            return False
```
{% endtab %}

{% tab title="player.py" %}
```python
import random

class Player:

    def __init__(self, marker="X", is_human=True):
        self._marker = marker
        self._is_human = is_human

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    def get_player_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
            
    def get_human_move(self):
        move = input("Player move (X): ")
        return move

    def get_computer_move(self):
        row = random.choice([1, 2, 3])
        col = random.choice(["A", "B", "C"])
        move = str(row) + col

        print("Computer move (O): ", move)

        return move
```
{% endtab %}

{% tab title="requirements.txt" %}
```
* The game shallstart by displaying a welcome message and an empty 3x3 board.

* There will be two players: the userand the computer player.
* The user will have the X marker.
* The computer player will have the Omarker.
* The user will be promptedto enter his/her move with theformat rowcolumn(e.g 1A) where:
    * Row can be 1, 2, or 3(top to bottom)* Column can be A, B, or C(left to right).
    These values shall be displayed on the board as a reference.

* If the user or the computer player selectsa position that is already taken, a descriptive message shouldbe displayed. * The updated board shallbe displayed after entering or generating the move.

* For a player towinthe gamethere must be a full row, column, or diagonal with its corresponding marker.

*The game ends when there is a tie (full board) or when the user or the computer player wins.

* The program shall assume that the user input will be in a correct format. 
```
{% endtab %}
{% endtabs %}

## 3. Parking Lot ☑️

{% tabs %}
{% tab title="main.py" %}
```python
from parking_lot import ParkingLot, Car, Bike, Bus

if __name__ == '__main__':
    parkingLotObj = ParkingLot(3, 10)
    
    parkingLotObj.parkVehicle(Car(10, "Google"))
    parkingLotObj.companyParked("Google"), [Car(10, "Google")]
    parkingLotObj.leaveOperation(Car(10, "Google"))
    parkingLotObj.companyParked("Google"), []
    
```
{% endtab %}

{% tab title="parking\_lot.py" %}
```python
from enum import Enum


# Vehicle type class for what all type of vehicles can come for parking
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3


# Vehicle class for license plate, company name and their type
class Vehicle:
    def __init__(self, licensePlate, companyName, type_of_vehicle):
        self.licensePlate = licensePlate
        self.companyName = companyName
        self.type_of_vehicle = type_of_vehicle

    def getType(self):
        return self.type_of_vehicle

    """overwrite __eq__ methods to correctly check if two vehicle objects are same. Otherwise, they will be 
    checked at hashcode level not at content level."""

    def __eq__(self, other):
        if other is None:
            return False
        if self.licensePlate != other.licensePlate:
            return False
        if self.companyName != other.companyName:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True


# Car class inherited from Vehicle class for license plate, company name and their type
class Car(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.CAR)


# Bike class inherited from Vehicle class for license plate, company name and their type
class Bike(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BIKE)


# Bus class inherited from Vehicle class for license plate, company name and their type
class Bus(Vehicle):
    def __init__(self, licensePlate, companyName):
        Vehicle.__init__(self, licensePlate, companyName, VehicleType.BUS)


class Slots:
    def __init__(self, lane, spotNumber, type_of_vehicle):
        # self.level = level
        self.lane = lane
        self.spotNumber = spotNumber
        self.vehicle = None
        self.type_of_vehicle = type_of_vehicle

    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle

    def getVehicle(self):
        return self.vehicle


"""Level class - Each level is an independent entity with a floor number, its lanes and the slots within it. 
The number of lanes are designed based on the number of slots. 10 slots make one lane"""


class Levels:
    def __init__(self, floorNumber, no_of_slots):
        self.floorNumber = floorNumber
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parkingSlots = set()
        self.availableSpots = []

        # Check available spots in a lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                import random

                # We will randomly assign a type to each slot.
                self.availableSpots.append(
                    Slots(lane, i, random.choice(list(VehicleType)))
                )
                # self.availableSpots.append(Slots(lane, i, type_of_vehicle))

    # Park vehicle is spot is available
    def park(self, vehicle):
        for slot in self.availableSpots:
            if slot.park(vehicle):
                return True
        return False

    # Remove vehicle from a spot
    def remove(self, vehicle):
        for spot in self.availableSpots:
            if spot.getVehicle() == vehicle:
                spot.removeVehicle()
                return True
        return False

    # Company name for the vehicle parked at the available spots
    def companyParked(self, companyName):
        all_vehicles = []
        for spot in self.availableSpots:
            vehicle = spot.getVehicle()
            if (vehicle is not None) and (vehicle.companyName == companyName):
                all_vehicles.append(vehicle)
                # print(all_vehicles)
        return all_vehicles


# A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
class ParkingLot:
    def __init__(self, no_of_floor, no_of_slot):
        self.levels = []
        for i in range(no_of_floor):
            self.levels.append(Levels(i, no_of_slot))

    # This operation inserts a vehicle accordingly, also takes care of what company vehicle it is.
    def parkVehicle(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    # This operation exits a vehicle 'C' in a level 'm'.
    def leaveOperation(self, vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True

    # This operation allows the user to view the list of vehicles parked for a particular company.
    def companyParked(self, companyName):
        all_vehicles = []
        for level in self.levels:
            all_vehicles.extend(level.companyParked(companyName))
        return all_vehicles

```
{% endtab %}

{% tab title="test\_parking\_lot.py" %}
```python
import unittest
from parking_lot import ParkingLot, Car, Bike, Bus


class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car(10, "Amazon"))
        res3 = parkingLotObj.parkVehicle(Bike(20, "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus(30, "Microsoft"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        self.assertEqual(res4, True)


    def test_leave_operation(self):
        parkingLotObj = ParkingLot(6, 30)
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        #self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        self.assertTrue(parkingLotObj.leaveOperation(Car(20, "Google")))
        self.assertEqual(parkingLotObj.leaveOperation(Car(20, "Google")), None)


    def test_companyParked(self):
        parkingLotObj = ParkingLot(6, 30)
        # res1 = parkingLotObj.parkVehicle(Car(20, "Google"))
        # res2 = parkingLotObj.companyParked("Google")
        self.assertTrue(parkingLotObj.parkVehicle(Car(20, "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(20, "Google")])
        #self.assertEqual(parkingLotObj.companyParked("Google"), Car(10, "Google"))
        print(parkingLotObj.companyParked("Google"))

        
    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        # Atleast 1 parking spot for car.
        # First park a car, it should return True.
        self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))
        # Get the list of cars, it should give one car we parked.
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car(10, "Google")])
        # Remove that car successfully.
        self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
        # Now the list of cars should be empty.
        self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()
```
{% endtab %}
{% endtabs %}

## 4. BookMyShow \(ticket booking\)

* Done in HLD

## 5. Elevator

{% tabs %}
{% tab title="Design.md" %}
```text
# Features:
* Extenal Request: press button outside(Up/Down) lift to call it
* Internal Request: press floor button inside(0...N) lift to make a drop request

# ====================================================

# Classes: (nouns)

* Direction(enum)
    * UP
    * DOWN

* State(enum)
    * IDLE
    * MOVING

* ReqType       -> in future: Alaram etc.
    * EXTERNAL
    * INTERNAL
    
* Elevator:
    * id
    * curr_direction
    * curr_state
    * curr_floor
    * curr_jobs[SortedList]           -> jobs which are being processed
    * up_pending_jobs[SortedList]     -> up jobs which cannot be processed now so put in pending queue
    * down_pending_jobs[SortedList]   -> down jobs which cannot be processed now so put in pending queue
    * move()    -> simulation: sleep for 5 seconds
    -----------[Phase#2]------------
    * is_elevator_free()
    * ...
    * start_evelator()

* Request:  #interface
    * elevator_id
    * req_type

* ExternalRequest(Request):
    * source_floor
    * direction(enum)

* InternalRequest(Request):
    * destination_floor



# [Design Discussion Points]===================================

* Implement with single elevator for now=> scale up later

* How to resolve conflicts?
    * 1. Keep requests sorted by timestamp & porcess by them
        * => Doesnt really make sense; elevator will keep moving to-n-frow
    * 2. Better: if an elevator is moving up-it'll keep moving up till last req floor
        * if anyone presses button on 'above' floors; he can hop in

* Give priority to InternalReqs > ExtRequests
    * person outside lift can wait=> is free/has other options+wifi
    * But, person stuck inside lift will frustrate more=> claustrophobia/suffocation+no internet

* Multiple Elevators in building
    * All free elevators will start rushing towards single req

## SRC: https://www.youtube.com/watch?v=FptCbX7fRHw&ab_channel=JavaStructures


```
{% endtab %}

{% tab title="Constants.py" %}
```python
from enum import Enum

class State(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    NONE = "NONE"


class ReqType(Enum):
    EXTERNAL = "EXTERNAL"
    INTERNAL = "INTERNAL"
```
{% endtab %}

{% tab title="Request.py" %}
```python
from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, elevator_id, req_type):
        self._elevator_id = elevator_id
        self._req_type = req_type

    @property
    def elevator_id(self):
        return self._elevator_id

    @property
    def req_type(self):
        return self._req_type


class InternalRequest(Request):
    def __init__(self, req_type, elevator_id, destination_floor):
        Request.__init__(self, elevator_id, req_type)
        self._destination_floor = destination_floor

    @property
    def destination_floor(self):
        return self._destination_floor

    @destination_floor.setter
    def destination_floor(self, floor):
        self._destination_floor = floor


class ExternalRequest(Request):
    def __init__(self, elevator_id, req_type, source_floor, direction):
        Request.__init__(self, elevator_id, req_type)
        self._source_floor = source_floor
        self._direction = direction

    @property
    def source_floor(self):
        return self._source_floor

    @source_floor.setter
    def source_floor(self, floor):
        self._source_floor = floor

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
```
{% endtab %}

{% tab title="Elevator.py" %}
```python
import uuid
from sortedcontainers import SortedList
import time

class Elevator:

    ids = 1

    def __init__(self,curr_direction=Direction.UP,
        curr_state=State.IDLE,
        curr_floor=0,
        curr_jobs=SortedList([]),
        up_pending_jobs=SortedList([]),
        down_pending_jobs=SortedList([])):
            self._id = Elevator.ids
            self._curr_direction = curr_direction
            self._curr_state = curr_state
            self._curr_floor = curr_floor
            self._curr_jobs = curr_jobs
            self._up_pending_jobs = up_pending_jobs
            self._down_pending_jobs = down_pending_jobs

        Elevator.ids += 1

    """ getters/setters"""

    @property
    def curr_direction(self):
        return self._curr_direction

    @curr_direction.setter
    def curr_direction(self, dir):
        self._curr_diection = dir

    @property
    def curr_state(self):
        return self._curr_state

    @curr_state.setter
    def curr_state(self, state):
        self._curr_state = state

    @property
    def curr_floor(self):
        return self._curr_floor

    @curr_floor.setter
    def curr_floor(self, floor):
        self._curr_floor = floor

    @property
    def curr_jobs(self):
        return self._curr_jobs

    """ ------------------------- [Phase#2]------------------------- """
    """ ---------- methods ---------- """

    def move(self):
        time.sleep(5)

    # checks if elevator has any CURRENTLY Processing jobs
    def is_elevator_free(self):
        return len(self.curr_jobs) == 0

    def add_to_curr_job(self, job):
        self._curr_jobs.append(job)

    # TOOD: make these methods private

    def add_to_pending_reqs(self, req):
        if req.direction == Direction.UP:
            self._up_pending_jobs.add(req)  # add because SortedList
        else:
            self._down_pending_jobs.add(req)  # add because SortedList

    def add_new_req(self, req):
        if self.curr_state == State.IDLE:  # khali baitha hua hai
            self.curr_state = State.MOVING

            # first req has to be an external req
            if req.req_type == ReqType.INTERNAL:
                print("Invalid Move OR a person was stuck inside somehow!")
                return
            else:
                self.add_to_curr_job(req)
                self.curr_direction = req.direction
                self.curr_state = State.MOVING

        else:  # khali nhi baitha hua
            # 1. this req is NOT in the same dirn as elevator - for both EXT/INT req
            if req.direction != self.curr_direction:
                self.add_to_pending_reqs(req)
            # handle internal requests - business logic goes here
            elif req.req_type == ReqType.INTERNAL:
                if (
                    req.direction == Direction.UP
                    and req.destination_floor > self.curr_floor
                ):
                    self.add_to_curr_job(req)
                elif (
                    req.direction == Direction.DOWN
                    and req.destination_floor < self.curr_floor
                ):
                    self.add_to_curr_job(req)

    def process_up_req(self, req):
        # move from curr -> src --> destination
        start_floor = self.curr_floor
        for i in range(start_floor, req.source_floor):
            self.curr_floor = start_floor
            print(f"@ Floor : {i}")
            self.move()

        print("---------- Opening Door: welcome ------------")
        start_floor = self.curr_floor
        for i in range(start_floor, req.destination_floor):
            print(f"@ Floor : {i}")
            self.curr_floor = start_floor
            self.move()

    def process_down_req(self, req):
        # move from curr -> src --> destination
        start_floor = self.curr_floor
        for i in range(start_floor, req.source_floor):
            self.curr_floor = start_floor
            print(f"@ Floor : {i}")
            self.move()

        print("---------- Opening Door: welcome ------------")
        start_floor = self.curr_floor
        for i in range(start_floor, req.destination_floor,-1):
            print(f"@ Floor : {i}")
            self.curr_floor = start_floor
            self.move()

    def add_pending_up_reqs_to_curr_req(self):
        if self._up_pending_jobs:
            self.curr_jobs = self._up_pending_jobs
            self.curr_direction = Direction.UP
            self.curr_state = State.MOVING
        else:
            self.curr_state = State.IDLE

    def add_pending_down_reqs_to_curr_req(self):
        if self._down_pending_jobs:
            self.curr_jobs = self._down_pending_jobs
            self.curr_direction = Direction.DOWN
            self.curr_state = State.MOVING
        else:
            self.curr_state = State.IDLE

    # process curr jobs
    def start_elevator(self):
        while not self.is_elevator_free():

            if self.curr_direction == "UP":  # process all UP requests
                req_to_be_served = self.curr_jobs.pop(0)
                self.process_up_req(req_to_be_served)
                if len(self.curr_jobs) == 0:
                    self.add_pending_up_reqs_to_curr_req()

            elif self.curr_direction == "DOWN":
                req_to_be_served = self.curr_jobs.pop(-1)
                self.process_down_req(req_to_be_served)
                if len(self.curr_jobs) == 0:
                    self.add_pending_down_reqs_to_curr_req()
            else:
                self.curr_state = "IDLE"
                return
```
{% endtab %}
{% endtabs %}

## 6. Logger

## 7. Stock Exchange



## Chess

## Snake & Ladder

## Splitwise

## ATM

## Amazon

## Facebook



## LinkedIn















