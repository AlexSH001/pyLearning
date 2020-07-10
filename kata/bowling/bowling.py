class Frame(object):
	def __init__(self):
		self.score = 0
		self.max_scoring_roll = 2
		self.roll_scores = list()
		self.active = True
		self.scoring_enable = True

	def add_score(self, roll_score):
		if len(self.roll_scores) < self.max_scoring_roll:
			self.roll_scores.append(roll_score)
			self.score = sum(self.roll_scores)
			self.handle_for_bonus()
		self.check_frame_active()

	def check_frame_active(self):
		if len(self.roll_scores) >= self.max_scoring_roll:
			self.scoring_enable = False
			self.active = False

	def handle_for_bonus(self):
		if self.is_strike() or self.is_spare():
			self.active = False
			self.max_scoring_roll = 3
		elif len(self.roll_scores) >= 2:
			self.active = False

	def is_strike(self):
		return len(self.roll_scores) == 1 and self.roll_scores[0] == 10

	def is_spare(self):
		return len(self.roll_scores) == 2 and sum(self.roll_scores) == 10


class Game(object):
	def __init__(self):
		self.score = 0
		self.max_frame = 10
		self.num_frame = 0
		self.scoring_frames = list()
		self.frame = None
		self.start()

	def start(self):
		frame = Frame()
		self.scoring_frames.append(frame)
		self.num_frame = 1

	def play(self, score):
		if not self.is_game_over():
			for f in self.scoring_frames:
				f.add_score(score)
			if self.num_frame < self.max_frame and not self.scoring_frames[-1].active:
				frame = Frame()
				self.scoring_frames.append(frame)
				self.num_frame += 1
			self.calc_score()

	def calc_score(self):
		scoring_completed_frames = list()
		for frame in self.scoring_frames:
			if not frame.scoring_enable:
				scoring_completed_frames.append(frame)
		for frame in scoring_completed_frames:
			self.scoring_frames.remove(frame)
			self.score += frame.score

	def is_game_over(self):
		if self.num_frame > self.max_frame and len(self.scoring_frames) == 0:
			return True
		else:
			return False


if __name__ == "__main__":
	def test_strike():
		game = Game()
		for i in range(10):
			game.play(10)
		game.play(10)
		game.play(10)
		print(game.score)

	def test_spare():
		game = Game()
		for i in range(10):
			game.play(5)
			game.play(5)
		game.play(5)
		print(game.score)


	def test_miss():
		game = Game()
		for i in range(10):
			game.play(9)
			game.play(0)
		print(game.score)

	test_strike()
	test_spare()
	test_miss()
