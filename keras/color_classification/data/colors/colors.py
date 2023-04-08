import numpy as np

colors = np.array([
        [255, 0, 0, 0],  # Red - 0
        [0, 255, 0, 1],  # Green - 1
        [0, 0, 255, 2],  # Blue - 2
        [255, 255, 0, 3],  # Yellow - 3
        [255, 0, 255, 4],  # Purple - 4
        [0, 255, 255, 5],  # Cyan - 5
        [255, 255, 255, 6],  # White - 6
        [0, 0, 0, 7],  # Black - 7
        [128, 128, 128, 8],  # Gray - 8
        [128, 0, 0, 9],  # Dark Red - 9
        [0, 128, 0, 10],  # Dark Green - 10
        [0, 0, 128, 11],  # Dark Blue - 11
        [128, 128, 0, 12],  # Dark Yellow - 12
        [128, 0, 128, 13],  # Dark Purple - 13
        [0, 128, 128, 14],  # Dark Cyan - 14
        [128, 128, 128, 15],  # Dark Gray - 15
        [192, 192, 192, 16],  # Light Gray - 16
        [139, 0, 0, 17],  # Dark Brown - 17
        [0, 139, 0, 18],  # Dark Olive Green - 18
        [0, 0, 139, 19],  # Dark Navy - 19
        [139, 139, 0, 20],  # Dark Khaki - 20
        [139, 0, 139, 21],  # Dark Magenta - 21
        [0, 139, 139, 22],  # Dark Teal - 22
        [210, 105, 30, 23],  # Chocolate - 23
        [244, 164, 96, 24],  # Sandy Brown - 24
        [178, 34, 34, 25],  # Fire Brick - 25
        [255, 140, 0, 26],  # Dark Orange - 26
        [218, 165, 32, 27],  # Goldenrod - 27
        [189, 183, 107, 28],  # Dark Khaki - 28
        [188, 143, 143, 29],  # Rosy Brown - 29
        [0, 255, 0, 30],  # Lime - 30
        [0, 128, 128, 31],  # Teal - 31
        [0, 0, 255, 32],  # Blue - 32
        [127, 255, 212, 33],  # Aquamarine - 33
        [47, 79, 79, 34],  # Dark Slate Gray - 34
        [64, 224, 208, 35],  # Turquoise - 35
        [0, 139, 139, 36],  # Dark Cyan - 36
        [0, 206, 209, 37],  # Dark Turquoise - 37
        [95, 158, 160, 38],  # Cadet Blue - 38
        [176, 196, 222, 39],  # Light Steel Blue - 39
        [70, 130, 180, 40],  # Steel Blue - 40
        [100, 149, 237, 41],  # Cornflower Blue - 41
        [30, 144, 255, 42],  # Dodger Blue - 42
        [0, 0, 139, 43],  # Dark Blue - 43
        [0, 191, 255, 44],  # Deep Sky Blue - 44
        [135, 206, 250, 45],  # Light Sky Blue - 45
        [70, 130, 180, 46],  # Steel Blue - 46
        [176, 224, 230, 47],  # Powder Blue - 47
        [173, 216, 230, 48],  # Light Blue - 48
        [176, 196, 222, 49],  # Light Steel Blue - 49
        [0, 128, 0, 50],  # Green - 50
        [124, 252, 0, 51],  # Lawn Green - 51
        [127, 255, 0, 52],  # Chartreuse - 52
        [173, 255, 47, 53],  # Green Yellow - 53
        [50, 205, 50, 54],  # Lime Green - 54
        [152, 251, 152, 55],  # Pale Green - 55
        [144, 238, 144, 56],  # Light Green - 56
        [0, 250, 154, 57],  # Medium Spring Green - 57
        [0, 255, 127, 58],  # Spring Green - 58
        [60, 179, 113, 59],  # Medium Sea Green - 59
        [46, 139, 87, 60],  # Sea Green - 60
        [34, 139, 34, 61],  # Forest Green - 61
        [0, 128, 128, 62],  # Teal - 62
        [0, 100, 0, 63],  # Dark Green - 63
        [154, 205, 50, 64],  # Yellow Green - 64
        [107, 142, 35, 65],  # Olive Drab - 65
        [128, 128, 0, 66],  # Olive - 66
        [85, 107, 47, 67],  # Dark - 67
        [128, 128, 128, 68],  # Gray - 68
        [220, 220, 220, 69],  # Gainsboro - 69
        [211, 211, 211, 70],  # Light Gray - 70
        [169, 169, 169, 71],  # Dark Gray - 71
        [0, 0, 0, 72],  # Black - 72
        [105, 105, 105, 73],  # Dim Gray - 73
        [119, 136, 153, 74],  # Light Slate Gray - 74
        [112, 128, 144, 75],  # Slate Gray - 75
        [47, 79, 79, 76],  # Dark Slate Gray - 76
        [128, 0, 0, 77],  # Maroon - 77
        [220, 20, 60, 78],  # Crimson - 78
        [255, 99, 71, 79],  # Tomato - 79
        [255, 69, 0, 80],  # Orange Red - 80
        [255, 140, 0, 81],  # Dark Orange - 81
        [255, 215, 0, 82],  # Gold - 82
        [184, 134, 11, 83],  # Dark Goldenrod - 83
        [218, 165, 32, 84],  # Goldenrod - 84
        [238, 232, 170, 85],  # Pale Goldenrod - 85
        [189, 183, 107, 86],  # Dark Khaki - 86
        [240, 230, 140, 87],  # Khaki - 87
        [255, 255, 0, 88],  # Yellow - 88
        [255, 255, 224, 89],  # Light Yellow - 89
        [255, 255, 240, 90],  # Ivory - 90
        [255, 250, 205, 91],  # Lemon Chiffon - 91
        [250, 250, 210, 92],  # Light Goldenrod Yellow - 92
        [255, 228, 196, 93],  # Bisque - 93
        [255, 235, 205, 94],  # Blanched Almond - 94
        [245, 222, 179, 95],  # Wheat - 95
        [255, 192, 203, 96],  # Pink - 96
        [255, 182, 193, 97],  # Light Pink - 97
        [255, 105, 180, 98],  # Hot Pink - 98
        [255, 20, 147, 99],  # Deep Pink - 99
        [219, 112, 147, 100]  # Pale Violet Red - 100
    ])
