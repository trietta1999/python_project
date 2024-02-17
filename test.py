from modules import color
from solver import BallSortPuzzle, play_moves

def test():
	data_in = [
		[color.RED, color.GREEN, color.PINK, color.BLUE],
		[color.L_BLUE, color.GREEN, color.GREEN, color.ORANGE],
		[color.RED, color.ORANGE, color.GRAY, color.PINK],
		[color.L_BLUE, color.BLUE, color.RED, color.GREEN],
		[color.L_BLUE, color.GRAY, color.PINK, color.L_BLUE],
		[color.GRAY, color.BLUE, color.ORANGE, color.PINK],
		[color.ORANGE, color.BLUE, color.RED, color.GRAY],
		[],
		[],
	]
	
	for data in data_in:
		data.reverse()

	puzzle = BallSortPuzzle(data_in)
	result = puzzle.solve()
	# ~ assert result is False
	return play_moves(data_in, puzzle.moves)

if __name__ == "__main__":
	print("Start")
	for data in test():
		print(data)
	print("End")
