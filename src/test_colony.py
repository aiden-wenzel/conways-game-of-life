import pytest as pt
import numpy as np
import colony


def test_colony():
    screen_width = 1280
    screen_height = 720
    bit_map = np.zeros((45, 80))
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    for i in range(colony_1.rows):
        for j in range(colony_1.columns):
            assert not colony_1.get_cell(i, j).get_is_alive()
            assert colony_1.get_cell(i, j).row == i
            assert colony_1.get_cell(i, j).column == j


def test_boarder():
    screen_width = 48
    screen_height = 48
    bit_map = np.zeros((3, 3))
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

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
    bit_map = np.array([
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]])

    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(1, 1) == 2


def test_num_neighbors_corner_1():
    screen_width = 64
    screen_height = 64
    bit_map = np.array([
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]])

    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(0, 0) == 1


def test_num_neighbors_corner_2():
    screen_width = 64
    screen_height = 64
    bit_map = np.array([
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ])
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(0, 3) == 2


def test_num_neighbors_corner_3():
    screen_width = 64
    screen_height = 64
    bit_map = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
        ])
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(3, 0) == 1


def test_num_neighbors_corner_4():
    screen_width = 64
    screen_height = 64
    bit_map = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
        ])
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(3, 3) == 2


def test_edges():
    screen_width = 80
    screen_height = 80
    bit_map = np.array([
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0]
        ])
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    assert colony_1.find_num_alive_neighbors(0, 1) == 3
    assert colony_1.find_num_alive_neighbors(2, 0) == 2
    assert colony_1.find_num_alive_neighbors(4, 2) == 3
    assert colony_1.find_num_alive_neighbors(3, 4) == 2


def test_determine_fate():
    screen_width = 80
    screen_height = 80
    bit_map = np.array([
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        ])
    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    colony_1.determine_fate(1, 1)
    colony_1.determine_fate(0, 4)
    colony_1.determine_fate(4, 4)

    assert colony_1.cells_to_die == [(0, 4), (4, 4)]
    assert colony_1.cells_to_resurect == [(1, 1)]


def test_determine_fate_bit_map():
    screen_width = 48
    screen_height = 48
    bit_map = np.array([
        [1, 0, 0],
        [1, 0, 0],
        [0, 1, 0]
        ])

    colony_1 = colony.Colony(screen_width, screen_height, bit_map)

    colony_1.bit_map_determine_fate()

    cells_to_die_correct = [(0, 0), (0, 2), (1, 2), (2, 1), (2, 2)]
    cells_to_resurect_correct = [(1, 1)]

    assert colony_1.cells_to_die == cells_to_die_correct
    assert colony_1.cells_to_resurect == cells_to_resurect_correct

def test_generation():
    screen_width = 64
    screen_height = 64
    bit_map = np.array([
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        ])

    colony_1 = colony.Colony(screen_width, screen_height, bit_map)
    colony_1.bit_map_determine_fate()
    colony_1.kill_and_resurect_cells()

    tick_1_correct = np.array([
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        ])

    assert (colony_1.get_bool_bit_map() == tick_1_correct).all()
pt.main()
