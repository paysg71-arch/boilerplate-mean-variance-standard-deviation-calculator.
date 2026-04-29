import mean_var_std
from unittest import main

print("Testing the calculate function with [0, 1, 2, 3, 4, 5, 6, 7, 8]...")
print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

print("\n--- Running unit tests ---")
# Run unit tests automatically
main(module='test_module', exit=False)
