import re

class Row:
	def __init__(self, id):
		self.row_id = id
		self.cells = []
		self.cell_buffer = 1
		self.large_cell_regex_pattern = r"(\s[^|]+\s)"
		self.large_cell_regex = re.compile(self.large_cell_regex_pattern)

	def get_id(self):
		return self.row_id

	def get_num_cells(self):
		return len(self.cells)

	def get_largest_cell(self):
		mlen = self.cell_buffer * 2
		for cell in self.cells:
			mlen = max(mlen, len(cell) + (self.cell_buffer * 2))
		return mlen

	def get_size(self):
		num_buffs = len(self.cells) * (self.cell_buffer + 1)
		largest_cell = self.get_largest_cell()

		return (num_buffs + largest_cell) * len(self.cells)

	def add_cell_content(self, item: str):
		self.cells.append(item)

	def get_cell_content(self, cell_idx: int):
		if cell_idx < 0 or cell_idx >= len(self.cells):
			return None

		return self.cells[cell_idx]

class Table:
	def __init__(self, rows, cols):
		self.headers = []
		self.rows = []
		self.row_map = {}

		# TBD: Get rid of columns array in favor of a row's internal array
		self.columns = []
		self.cell_buffer = 1

		for i in range(rows):
			self.add_row()

		for i in range(cols):
			self.add_column(i+1)

	def add_row(self):
		row_id = len(self.rows) + 1
		rrow = Row(row_id)

		self.rows.append(rrow)
		self.row_map[row_id] = rrow

	# TBD: Refactor out in favor of a row's internal array
	def add_column(self, row_id):
		self.columns.append(Row(row_id))

	def add_item(self, strng, index):
		if index < 0 or index >= len(self.rows):
			return -1

		self.rows[index].add_cell_content(strng)
		return 0

	def get_row_by_id(self, id):
		try:
			return self.row_map[id]
		except KeyError as e:
			return None

	def get_longest_cell(self):
		lng = 1

		for row in self.rows:
			lng = max(lng, row.get_largest_cell())

		return lng

	def make_table_border(self):
		border = "+"
		longest_cell = self.get_longest_cell()

		for i in range(len(self.columns)):
			for j in range(longest_cell):
				border += "-"
			border += "+"

		return border

	def make_row(self):
		row_str = "|"
		longest_cell = self.get_longest_cell()

		for i in range(len(self.columns)):
			row_str += " " * self.cell_buffer
			# Cell content goes here
			row_str += " " * self.cell_buffer
			row_str += "|"

		return row_str

	def make_table(self):
		table_str = self.make_table_border()
		table_str += "\n"

		for i in range(len(self.rows)-1):
			table_str += self.make_row()
			table_str += "\n"
			table_str += self.make_table_border()
			table_str += "\n"

		table_str += self.make_row()
		table_str += "\n"
		table_str += self.make_table_border()

		return table_str

if __name__ == "__main__":
	table = Table(3,7)

	#print(table.add_item("asdf", 0))

	str_table = table.make_table()

	print(str_table)
