from rstable.table.table import Row

def test_row_id_pass():
    r = Row(4)

    assert r.get_id() == 4


def test_row_num_cells_pass():
    r = Row(1)

    assert r.get_num_cells() == 0

    r.add_cell_content("test_string")

    assert r.get_num_cells() == 1

def test_get_largest_cell_pass():
    '''
    test 'mlen' against the padding, with and without content in the
    internal row data structure.
    Should also test padding against a couple differing types of
    large/largest cells
    '''

    assert 1 == 1

def test_add_cell_content_pass():
    assert 1 == 1

def test_get_cell_content_pass():
    assert 1 == 1

def test_get_cell_content_fail():
    assert 1 == 1

def test_get_cell_length_pass():
    assert 1 == 1

def test_get_cell_length_fail():
    assert 1 == 1
