class Roll(object):
	def __init__(self):
		self.score = 0

	def set_score(self, score):
		self.score = score


class Frame(object):
	def __init__(self):
		self.score = 0
		self.num_scoring_roll = 2
		self.rolls = list()
		self.active = True
		self.scoring_enable = True

	def add_roll(self, roll):
		if len(self.rolls) < self.num_scoring_roll:
			self.rolls.append(roll)
			self.score = sum(r.score for r in self.rolls)
			self.handle_for_bonus()
		else:
			self.scoring_enable = False
			self.active = False

	def handle_for_bonus(self):
		if self.is_strike() or self.is_spare():
			self.active = False
			self.num_scoring_roll = 3
		elif len(self.rolls) >= 2:
			self.active = False

	def is_strike(self):
		if len(self.rolls) == 1 and self.rolls[0].score == 10:
			return True
		else:
			return False

	def is_spare(self):
		if len(self.rolls) == 2 and sum([self.rolls[0].score, self.rolls[1].score]) == 10:
			return True
		else:
			return False


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
		if not self.is_game_over:
			roll = Roll()
			roll.set_score(score)
			for frame in self.scoring_frames:
				frame.add_roll(roll)
			if not self.scoring_frames[-1].active:
				frame = Frame()
				self.scoring_frames.append(frame)
				self.num_frame += 1

	def calc_score(self):
		scoring_disabled_frames = list()
		for frame in self.scoring_frames:
			if not frame.scoring_enable:
				scoring_disabled_frames.append(frame)
		for frame in scoring_disabled_frames:
			self.scoring_frames.remove(frame)
			self.score += frame.score

	def is_game_over(self):
		if self.num_frame >= self.max_frame and len(self.scoring_frames) == 0:
			return True
		else:
			return False
