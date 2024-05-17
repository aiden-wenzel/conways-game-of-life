import pytest as pt
import colony


def test_colony():
    screen_width = 1280
    screen_height = 720
    colony_1 = colony.Colony(screen_width, screen_height)

    for i in range(colony_1.rows):
        for j in range(colony_1.columns):
            assert not colony_1.get_cell(i, j).get_is_alive()
            assert colony_1.get_cell(i, j).row == i
            assert colony_1.get_cell(i, j).column == j


def test_resurect():
    screen_width = 1280
    screen_height = 720
    colony_1 = colony.Colony(screen_width, screen_height)

    colony_1.resurect_cell_at(4, 5)

    assert colony_1.get_cell(4, 5).get_is_alive()


def test_boarder():
    screen_width = 48
    screen_height = 48
    colony_1 = colony.Colony(screen_width, screen_height)

    # check first row
    for i in range(colony_1.rows):
        assert colony_1.bit_map[0][i].is_boarder

    # check last row
    for i in range(colony_1.rows):
        assert colony_1.bit_map[colony_1.rows-1][i].is_boarder

    # check first column
    for j in range(colony_1.columns):
        assert colony_1.bit_map[j][0].is_boarder

    # check last column
    for j in range(colony_1.columns):
        assert colony_1.bit_map[j][colony_1.columns-1].is_boarder

    # check middle cell
    assert not colony_1.bit_map[1][1].is_boarder


def test_num_neighbors():
    screen_width = 64
    screen_height = 64
    colony_1 = colony.Colony(screen_width, screen_height)

    colony_1.resurect_cell_at(0, 2)
    colony_1.resurect_cell_at(1, 1)
    colony_1.resurect_cell_at(2, 0)

    assert colony_1.find_num_alive_neighbors(1, 1) == 2


def test_num_neighbors_corner_1():
    screen_width = 64
    screen_height = 64
    colony_1 = colony.Colony(screen_width, screen_height)

    colony_1. resurect_cell_at(0, 1)
    colony_1.resurect_cell_at(2, 0)

    assert colony_1.find_num_alive_neighbors(0, 0) == 1


def test_num_neighbors_corner_2():
    screen_width = 64
    screen_height = 64
    colony_1 = colony.Colony(screen_width, screen_height)

    colony_1.resurect_cell_at(0, 3)
    colony_1.resurect_cell_at(0, 2)
    colony_1.resurect_cell_at(1, 3)

    assert colony_1.find_num_alive_neighbors(0, 3) == 2

pt.main()
