from model.core import find_mand_coords
from ui.ascii import create_ascii


coords = find_mand_coords()
print(create_ascii(coords))