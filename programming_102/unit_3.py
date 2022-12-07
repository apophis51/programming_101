measurements = {
    "ft" : .3048,
    "mi" : 1609.34,
    "m"  : 1,
    "km" : 1000,
    "yard" : 0.9144,
    "inch" : 0.0254
}


print("what is the distance? ", end=""); distance = int(input())
print("what are the units? ", end=""); units = input()
print(f"{distance} {units} is {measurements[units]*distance} m")