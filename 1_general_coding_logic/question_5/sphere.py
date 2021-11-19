import math


def volume_of_sphere(diameter):
    """Returns the volume of a sphere with given diameter."""
    if diameter <= 0:
        return 0

    radius = diameter / 2

    return (4 / 3) * math.pi * (radius ** 3)
