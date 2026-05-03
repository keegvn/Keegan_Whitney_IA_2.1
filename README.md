# Shipping Cost Calculator (Problem 2)

A lightweight CLI (Command Line Interface) utility script written in Python to calculate shipping costs based on package quantity and delivery method.

---

## Features
*   **Two-Tier Pricing:** Supports different rates for Regular and Express shipping.
*   **Simple Input Handling:** Accepts integer inputs for package counts and character codes for shipping types.
*   **Direct Calculation:** Provides immediate cost feedback based on logic-driven formulas.

---

## Pricing Logic
The program applies the following business rules to determine the final cost:

| Shipping Code | Method | Cost Per Package |
| :--- | :--- | :--- |
| `r` | Regular | $10 |
| `e` | Express | $15 |

---

## Technical Details

### Code Logic
1.  **Input Collection:** The script prompts the user for the number of packages (`p`) and the shipping speed (`s`).
2.  **Conditional Processing:** 
    *   If the input is `r`, it calculates $p \times 10$.
    *   If the input is `e`, it calculates $p \times 15$.
3.  **Output:** Prints the formatted total cost to the console.

### Script Workflow
```python
# The script uses a straightforward procedural approach:
# 1. Type Conversion: int() for numeric calculations.
# 2. Comparison: String matching for 'r' or 'e'.
# 3. Output: String concatenation for the final display.
