import numpy as np


class DataAnalytics:
    """Object-oriented NumPy Analyzer."""

    def __init__(self):
        self.array = None

    # -------------------- Internal / Private Methods --------------------

    def __validate_array(self):
        if self.array is None:
            print("\nNo array has been created yet.")
            return False
        return True

    def __read_elements(self, count):
        while True:
            try:
                values = list(map(float, input(
                    f"Enter {count} elements separated by space: "
                ).split()))

                if len(values) != count:
                    print(f"Please enter exactly {count} elements.")
                    continue

                return values
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    @staticmethod
    def _format_array(arr):
        if np.all(np.isfinite(arr)) and np.all(arr == np.floor(arr)):
            return arr.astype(int)
        return arr

    @classmethod
    def project_title(cls):
        print("\n" + "=" * 42)
        print("           NUMPY ANALYZER")
        print("=" * 42)

    # -------------------- Array Creation --------------------

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                n = int(input("Enter the number of elements: "))
                if n <= 0:
                    raise ValueError
                values = self.__read_elements(n)
                self.array = np.array(values)

            elif choice == "2":
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))

                if rows <= 0 or cols <= 0:
                    raise ValueError

                values = self.__read_elements(rows * cols)
                self.array = np.array(values).reshape(rows, cols)

            elif choice == "3":
                layers = int(input("Enter the number of layers: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))

                if layers <= 0 or rows <= 0 or cols <= 0:
                    raise ValueError

                values = self.__read_elements(layers * rows * cols)
                self.array = np.array(values).reshape(layers, rows, cols)

            else:
                print("Invalid choice.")
                return

            self.array = self._format_array(self.array)

            print("\nArray created successfully:")
            print(self.array)

        except ValueError:
            print("Invalid dimensions or input.")

    # -------------------- Indexing and Slicing --------------------

    def array_access(self):
        if not self.__validate_array():
            return

        while True:
            print("\nIndexing and Slicing:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.indexing()
            elif choice == "2":
                self.slicing()
            elif choice == "3":
                return
            else:
                print("Invalid choice.")

    def indexing(self):
        try:
            print("\nCurrent Array:")
            print(self.array)

            if self.array.ndim == 1:
                index = int(input("Enter index: "))
                print("Element:", self.array[index])

            elif self.array.ndim == 2:
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))
                print("Element:", self.array[row, col])

            elif self.array.ndim == 3:
                layer = int(input("Enter layer index: "))
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))
                print("Element:", self.array[layer, row, col])

        except (ValueError, IndexError):
            print("Invalid index.")

    def slicing(self):
        try:
            print("\nCurrent Array:")
            print(self.array)

            if self.array.ndim == 1:
                value = input(
                    "Enter range (start:end), e.g. 1:3: "
                ).strip()

                start, end = self.__parse_range(value)
                result = self.array[start:end]

            elif self.array.ndim == 2:
                row_range = input(
                    "Enter the row range (start:end), e.g. 0:2: "
                ).strip()

                col_range = input(
                    "Enter the column range (start:end), e.g. 1:3: "
                ).strip()

                rs, re = self.__parse_range(row_range)
                cs, ce = self.__parse_range(col_range)

                result = self.array[rs:re, cs:ce]

            else:
                layer_range = input(
                    "Enter the layer range (start:end), e.g. 0:2: "
                ).strip()

                row_range = input(
                    "Enter the row range (start:end), e.g. 0:2: "
                ).strip()

                col_range = input(
                    "Enter the column range (start:end), e.g. 1:3: "
                ).strip()

                ls, le = self.__parse_range(layer_range)
                rs, re = self.__parse_range(row_range)
                cs, ce = self.__parse_range(col_range)

                result = self.array[ls:le, rs:re, cs:ce]

            print("\nSliced Array:")
            print(result)

        except (ValueError, IndexError):
            print("Invalid range. Use format such as 0:2.")

    @staticmethod
    def __parse_range(value):
        parts = value.split(":")

        if len(parts) != 2:
            raise ValueError

        start = int(parts[0].strip())
        end = int(parts[1].strip())

        return start, end

    # -------------------- Mathematical Operations --------------------

    def mathematical_operations(self):
        if not self.__validate_array():
            return

        print("\nMathematical Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        print("7. Go Back")

        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2", "3", "4"}:
            self._elementwise_operation(choice)
        elif choice == "5":
            self._dot_product()
        elif choice == "6":
            self._matrix_multiplication()
        elif choice == "7":
            return
        else:
            print("Invalid choice.")

    def _get_same_shape_array(self):
        values = self.__read_elements(self.array.size)
        return np.array(values).reshape(self.array.shape)

    def _elementwise_operation(self, choice):
        print(
            f"\nEnter the same-size array elements "
            f"({self.array.size} elements separated by space):"
        )

        try:
            second = self._get_same_shape_array()

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(self._format_array(second))

            if choice == "1":
                result = self.array + second
                name = "Addition"
            elif choice == "2":
                result = self.array - second
                name = "Subtraction"
            elif choice == "3":
                result = self.array * second
                name = "Multiplication"
            else:
                if np.any(second == 0):
                    print("Division by zero is not allowed.")
                    return
                result = self.array / second
                name = "Division"

            print(f"\nResult of {name}:")
            print(self._format_array(result))

        except ValueError:
            print("Invalid input.")

    def _dot_product(self):
        if self.array.ndim != 2:
            print("Dot product is supported for 2D arrays.")
            return

        rows, cols = self.array.shape
        print(
            f"\nEnter {rows * cols} elements for the second "
            f"{rows}x{cols} array:"
        )

        try:
            second = self._get_same_shape_array()
            result = np.dot(self.array, second)

            print("\nDot Product:")
            print(self._format_array(result))

        except ValueError:
            print("Invalid input.")

    def _matrix_multiplication(self):
        if self.array.ndim != 2:
            print("Matrix multiplication is supported for 2D arrays.")
            return

        rows, cols = self.array.shape

        print(
            f"\nFirst matrix shape: {rows} x {cols}"
        )
        print(
            f"Second matrix must have {cols} rows."
        )

        try:
            second_rows = int(input("Enter number of rows: "))
            second_cols = int(input("Enter number of columns: "))

            if second_rows != cols or second_rows <= 0 or second_cols <= 0:
                print("Invalid matrix dimensions.")
                return

            values = self.__read_elements(second_rows * second_cols)
            second = np.array(values).reshape(second_rows, second_cols)

            result = self.array @ second

            print("\nSecond Matrix:")
            print(self._format_array(second))

            print("\nMatrix Multiplication Result:")
            print(self._format_array(result))

        except ValueError:
            print("Invalid input.")

    # -------------------- Combine / Split --------------------

    def combine_or_split(self):
        if not self.__validate_array():
            return

        if self.array.ndim != 2:
            print("Combine and Split are supported for 2D arrays.")
            return

        while True:
            print("\nCombine or Split Arrays:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.combine_arrays()
            elif choice == "2":
                self.split_array()
            elif choice == "3":
                return
            else:
                print("Invalid choice.")

    def combine_arrays(self):
        print(
            f"\nEnter the elements of another array to combine "
            f"({self.array.size} elements separated by space):"
        )

        try:
            second = self._get_same_shape_array()

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(self._format_array(second))

            result = np.vstack((self.array, second))

            print("\nCombined Array:")
            print(result)

        except ValueError:
            print("Invalid input.")

    def split_array(self):
        try:
            sections = int(input("Enter number of sections: "))

            if sections <= 0:
                print("Number of sections must be greater than 0.")
                return

            if self.array.shape[0] % sections != 0:
                print(
                    "Number of sections must divide "
                    "the number of rows exactly."
                )
                return

            result = np.vsplit(self.array, sections)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSplit Arrays:")

            for i, part in enumerate(result, start=1):
                print(f"\nPart {i}:")
                print(part)

        except ValueError:
            print("Invalid number of sections.")

    # -------------------- Search, Sort, Filter --------------------

    def search_sort_filter(self):
        if not self.__validate_array():
            return

        while True:
            print("\nSearch, Sort, and Filter:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.search_value()
            elif choice == "2":
                self.sort_array()
            elif choice == "3":
                self.filter_values()
            elif choice == "4":
                return
            else:
                print("Invalid choice.")

    def search_value(self):
        try:
            value = float(input("Enter value to search: "))
            positions = np.argwhere(self.array == value)

            if positions.size == 0:
                print(f"{value:g} was not found in the array.")
            else:
                print(f"{value:g} found at index/indices:")
                print(positions)

        except ValueError:
            print("Invalid value.")

    def sort_array(self):
        print("\nOriginal Array:")
        print(self.array)

        result = np.sort(self.array)

        print("\nSorted Array:")
        print(result)

    def filter_values(self):
        try:
            condition = input(
                "Enter filter condition (e.g. >30, <50, ==20): "
            ).strip()

            operators = [">=", "<=", "==", "!=", ">", "<"]

            operator = next(
                (op for op in operators if condition.startswith(op)),
                None
            )

            if operator is None:
                print("Invalid condition.")
                return

            value = float(condition[len(operator):].strip())

            if operator == ">":
                mask = self.array > value
            elif operator == "<":
                mask = self.array < value
            elif operator == ">=":
                mask = self.array >= value
            elif operator == "<=":
                mask = self.array <= value
            elif operator == "==":
                mask = self.array == value
            else:
                mask = self.array != value

            print("\nFiltered Values:")
            print(self.array[mask])

        except ValueError:
            print("Invalid filter value.")

    # -------------------- Aggregates and Statistics --------------------

    def aggregates_statistics(self):
        if not self.__validate_array():
            return

        while True:
            print("\nAggregates and Statistics:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentiles")
            print("9. Correlation Coefficient")
            print("10. Go Back")

            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    print("\nSum of Array:", np.sum(self.array))

                elif choice == "2":
                    print("\nMean of Array:", np.mean(self.array))

                elif choice == "3":
                    print("\nMedian of Array:", np.median(self.array))

                elif choice == "4":
                    print(
                        "\nStandard Deviation of Array:",
                        np.std(self.array)
                    )

                elif choice == "5":
                    print("\nVariance of Array:", np.var(self.array))

                elif choice == "6":
                    print("\nMinimum of Array:", np.min(self.array))

                elif choice == "7":
                    print("\nMaximum of Array:", np.max(self.array))

                elif choice == "8":
                    p = float(input("Enter percentile (0-100): "))

                    if not 0 <= p <= 100:
                        print("Percentile must be between 0 and 100.")
                        continue

                    print(
                        f"\n{p:g}th Percentile:",
                        np.percentile(self.array, p)
                    )

                elif choice == "9":
                    print(
                        f"\nEnter {self.array.size} elements for "
                        "the second array:"
                    )

                    second = np.array(
                        self.__read_elements(self.array.size)
                    )

                    first_flat = self.array.flatten()
                    corr = np.corrcoef(first_flat, second)[0, 1]

                    print("\nCorrelation Coefficient:", corr)

                elif choice == "10":
                    return

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

    # -------------------- Main Menu --------------------

    def run(self):
        self.project_title()

        while True:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Indexing and Slicing")
            print("3. Perform Mathematical Operations")
            print("4. Combine or Split Arrays")
            print("5. Search, Sort, or Filter Arrays")
            print("6. Compute Aggregates and Statistics")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_array()

            elif choice == "2":
                self.array_access()

            elif choice == "3":
                self.mathematical_operations()

            elif choice == "4":
                self.combine_or_split()

            elif choice == "5":
                self.search_sort_filter()

            elif choice == "6":
                self.aggregates_statistics()

            elif choice == "7":
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.run()
