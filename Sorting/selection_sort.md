🔹 Selection Sort Algorithm

1. For each index `i` in the list:

    * Find the minimum element from the unsorted part.

    * Swap it with the element at index `i`.

2. Continue until the array is sorted.

### When to Use Selection Sort

✅ Swaps are expensive (e.g., working with flash memory or databases where writing is costly).

Selection Sort does only `~n` swaps total.

✅ You want a simple, predictable algorithm for small datasets.

❌ Not good if you care about stability (it can shuffle equal elements).

❌ Always `O(n²)`, even if the list is already sorted.

👉 Example use: Sorting a small array stored in EEPROM/flash memory where writes wear out the memory.