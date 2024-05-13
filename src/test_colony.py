import pytest as pt
import colony


screen_width = 1280
screen_height = 720


def test_colony():
    colony_1 = colony.Colony(screen_width, screen_height)

    for i in range(colony_1.rows):
        for j in range(colony_1.columns):
            assert not colony_1.get_cell(i, j).get_is_alive()
            assert colony_1.get_cell(i, j).row == i
            assert colony_1.get_cell(i, j).column == j


def test_resurect():
    colony_1 = colony.Colony(screen_width, screen_height)

    colony_1.resurect_cell_at(4, 5)

    assert colony_1.get_cell(4, 5).get_is_alive


pt.main()
