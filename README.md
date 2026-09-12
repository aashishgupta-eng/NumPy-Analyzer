# Project 8 – NumPy Analyzer

## Objective
Develop a menu-driven NumPy Analyzer using NumPy and Object-Oriented Programming (OOP). The program performs array creation, indexing, slicing, mathematical operations, combining/splitting, searching, sorting, filtering, aggregation, and statistical calculations.

## Features

### 1. Array Management
- Create 1D, 2D, and 3D NumPy arrays.
- Index array elements.
- Slice arrays using ranges.

### 2. Mathematical Operations
- Element-wise addition
- Element-wise subtraction
- Element-wise multiplication
- Element-wise division
- Dot product
- Matrix multiplication

### 3. Combine / Split
- Combine 2D arrays vertically using `np.vstack()`.
- Split 2D arrays using `np.vsplit()`.

### 4. Search, Sort, and Filter
- Search for a value and display its indices.
- Sort arrays in ascending order.
- Apply row-wise sorting to 2D/3D arrays.
- Filter values using conditions such as `>30`, `<50`, `==20`.

### 5. Aggregates and Statistics
- Sum
- Mean
- Median
- Standard deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation coefficient

### 6. OOP Concepts Used
- Class and object
- Constructor (`__init__`)
- Encapsulation
- Private methods
- Class method (`@classmethod`)
- Static method (`@staticmethod`)

## Requirements
- Python 3.x
- NumPy

## Installation

```bash
pip install numpy
```

## Run

```bash
python main.py
```

## Example 2D Array

Input:

```text
10 20 30 40 50 60
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

## Project Structure

```text
Project_8_NumPy_Analyzer/
│
├── main.py
└── README.md
```
