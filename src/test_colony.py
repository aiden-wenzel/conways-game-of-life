import conway.colony as colony

screen_width = 1280
screen_height = 720

colony_1 = colony.Colony(screen_width, screen_height)

for i in range(colony_1.rows):
    for j in range(colony_1.columns):
        assert not colony_1.get_cell(i, j).get_is_alive()
