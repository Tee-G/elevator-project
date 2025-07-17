def calculate_surface_area_cabin(L, B, H):
    top_bottom = 2 * L * B
    front_back = 2 * B * H
    sides = 2 * L * H
    return round(top_bottom + front_back + sides, 2)

def calculate_volume_of_cabin(area, thickness=0.2):
    return round(area * thickness, 2)

def calculate_weight_of_cabin(volume, density=7.85):
    return round((volume * density) / 1000, 2)

def calculate_counterweight(cabin_weight, payload):
    return round(cabin_weight + (0.5 * payload), 2)


