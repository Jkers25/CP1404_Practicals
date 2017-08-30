NAME_AND_COLOURS_DICT = {"AliceBlue": "#f08ff", "aquamarine2": "#7fffd4", "azure1": "#f0ffff", "bisque1": "#ffe4c4",
                         'GhostWhite': '#f8f8ff', 'gold1': '#ffd700', 'green1': '#00ff00', 'a': '#000000'}
input_colour = input('Input a color')
if input_colour in NAME_AND_COLOURS_DICT:
    print(NAME_AND_COLOURS_DICT[input_colour])
