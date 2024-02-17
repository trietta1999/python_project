from typing import List, Set

from modules import Flask, Move
from modules.color import Color

class BallSortPuzzle:
	def __init__(self, columns: List[List[Color]]):
		self.flask_size = len(columns[0])  # here an assertion, that the first flask is always full
		self.flasks = [Flask(column, i, self.flask_size) for i, column in enumerate(columns)]
		self.moves: List[Move] = []
		self.states: Set[str] = set()

	def get_possible_moves(self) -> List[Move]:
		moves = []
		for flask in self.flasks:
			if flask.is_solved:
				continue

			if flask.same_three_balls:
				continue

			upper_ball = flask.upper_ball
			for potential_flask in self.flasks:
				if flask is potential_flask:
					continue
				if potential_flask.can_receive(upper_ball):
					moves.append(Move(flask.num, potential_flask.num, upper_ball.color))

		return moves

	def commit_move(self, move: Move) -> str:
		ball = self.flasks[move.i].pop()
		self.flasks[move.j].push(ball)
		self.moves.append(move)
		return self.calculate_state()

	def rollback_move(self, move: Move):
		ball = self.flasks[move.j].pop()
		self.flasks[move.i].push(ball)
		self.moves.pop()

	@property
	def is_solved(self):
		return all(flask.is_solved for flask in self.flasks)

	def solve(self) -> bool:
		if self.is_solved:
			return True

		for move in self.get_possible_moves():
			new_state = self.commit_move(move)
			if new_state in self.states:  # Cycle!
				self.rollback_move(move)
				continue

			self.states.add(new_state)
			if self.solve():
				return True
			self.rollback_move(move)

		return False

	def calculate_state(self) -> str:
		return '|'.join(flask.state for flask in self.flasks)

	def __str__(self) -> str:
		result = '\n'
		for ball_idx in range(self.flask_size - 1, -1, -1):
			for flask in self.flasks:
				try:
					ball = flask[ball_idx]
				except IndexError:
					ball = ' '  # type: ignore
				result += f'|{ball}| '
			result += '\n'
		for flask in self.flasks:
			result += f' {flask.num}   '
		result += '\n'
		return result

def play_moves(data_in: List[List[Color]], moves: List[Move]) -> list:
	output = []
	puzzle = BallSortPuzzle(data_in)
	for move in moves:
		output.append(str(move))
		puzzle.commit_move(move)
	
	return output
