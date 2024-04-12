import math

DATA_LIST = [
    []
]

def main():
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)

    print(storage_efficiency)

def compute_volume(radius, height):
    result = math.pi * (radius ** 2) * height
    return result

def compute_surface_area(radius, height):
    result = 2 * math.pi * radius * (radius + height)
    return result

def compute_storage_efficiency(volume, surface_area):
    result = volume / surface_area
    return result

main()