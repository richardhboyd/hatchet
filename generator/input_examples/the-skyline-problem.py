def get_skyline(buildings):
    skyline = []
    heights = [0]
    
    for l, r, h in buildings:
        while skyline and skyline[-1][0] <= l:
            heights.pop()
            if skyline[-1][1] != heights[-1]:
                skyline.append([skyline[-1][0], heights[-1]])
            skyline.pop()
        heights.append(h)
        skyline.append([l, h])
        
    while len(skyline) > 1 and skyline[-1][1] == 0:
        skyline.pop()
        
    return skyline
