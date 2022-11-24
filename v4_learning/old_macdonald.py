"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
"""

def old_macdonald(strg):
    if len(strg) > 3:
        return strg[:3].capitalize() + strg[3:].capitalize()
    else:
        return "Name is too short"

print(old_macdonald('macdonald'))