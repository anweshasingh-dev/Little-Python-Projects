# Fancy Forest

I kept seeing tree-printing questions and thought: why print only one plain tree? Around the same time I discovered Python’s `center()` function and realised it makes text alignment so much easy. That led to this tiny experiment — generate multiple trees with random heights and leaf styles and let them grow into a little forest.

## Idea

Generate several trees side by side where each tree has:

- A random height
- A random leaf character (`*`, `^`, `o`, `@`)
- Automatic alignment
- Slight trunk variation

Each execution creates a different forest.

Example output:

```text
               o                       ^           @
    *         ooo                     ^^^         @@@
   ***       ooooo                   ^^^^^       @@@@@
  *****     ooooooo     ^     ^     ^^^^^^^     @@@@@@@
 *******   ooooooooo   ^^^   ^^^   ^^^^^^^^^   @@@@@@@@@
********* ooooooooooo ^^^^^ ^^^^^ ^^^^^^^^^^^ @@@@@@@@@@@
    |          |        |     |        |           |
    |          |                       |           |
```

## My Approach

### 1. Generate tree properties

For each tree:

- Random height
- Random leaf character
- Width based on height

```python
width = height * 2 - 1
```

---

### 2. Build the forest row by row

Instead of drawing one full tree at a time, the forest is printed level by level.

The tallest tree determines the total number of rows, and each tree decides whether it should appear in that row.

Leaf count grows using odd numbers:

```text
1 → 3 → 5 → 7 ...
```

`center()` handles spacing and alignment without manual padding calculations.

---

### 3. Using `zip()` to keep trees together

One thing I liked here was using `zip()`.

Since heights, widths, and leaf characters are stored in separate lists, `zip()` lets the program iterate over matching tree properties together:

```python
for h, w, char in zip(heights, widths, leaves):
```

So each loop works on one complete tree at a time instead of tracking indexes manually.

---

### 4. Draw trunks

After printing leaves:

- Print trunk rows
- Smaller trees skip the second trunk row

This adds a little variation across the forest.

## Features

- Random forest generation
- Variable tree heights
- Different leaf styles
- Alignment using `center()`
- Cleaner iteration using `zip()`
- Pure Python
