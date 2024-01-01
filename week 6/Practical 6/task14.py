colours = ["red", "green", "yellow", "blue", "red"]  
colours_copy = colours.copy()

colours.append("black")
colours.remove("green")

print("Original colours list after changes:", colours)
print("Copied colours list:", colours_copy)