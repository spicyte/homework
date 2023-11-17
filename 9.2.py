import sys

print("Before modification: ")
print(sys.path)


new_path = "/path/to/your/directory"
sys.path.append(new_path)


print("\nAfter modification:")
print(sys.path)
