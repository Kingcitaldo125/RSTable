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

	def add_cell(self, item):
		self.cells.append(item)

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

class Table:
	def __init__(self, rows, cols):
		self.headers = []
		self.rows = []
		self.columns = []
		self.cell_buffer = 1
		
		for i in range(rows):
			self.add_row()

		for i in range(cols):
			self.add_column()

	def add_row(self):
		self.rows.append(Row(len(self.rows) + 1))

	def add_column(self):
		self.columns.append(Row(len(self.columns) + 1))

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
		row = "|"
		longest_cell = self.get_longest_cell()

		for i in range(len(self.columns)):
			row += " " * self.cell_buffer
			row += " " * self.cell_buffer
			row += "|"

		return row

	def make_table(self):
		table_str = self.make_table_border()
		table_str += "\n"

		for i in range(len(self.rows)):
			table_str += self.make_row()
			table_str += "\n"
			table_str += self.make_table_border()
			table_str += "\n"

		return table_str

if __name__ == "__main__":
	table = Table(3,7)
	print(table.make_table())
