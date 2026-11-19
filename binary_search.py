#!/usr/bin/env python3
"""Find an integer in a sorted list using binary search."""


def binary_search(numbers: list[int], target: int) -> int:
    """Return the index of target, or -1 if it is not present.

    `numbers` must be sorted in ascending order.
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        value = numbers[middle]

        if value == target:
            return middle
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main() -> None:
    try:
        numbers = [int(value) for value in input(
            "Enter sorted integers separated by spaces: "
        ).split()]
        target = int(input("Enter the integer to find: "))
    except ValueError:
        print("Please enter integers only.")
        return

    if numbers != sorted(numbers):
        print("The list must be sorted in ascending order.")
        return

    index = binary_search(numbers, target)
    if index == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} was found at index {index}.")


if __name__ == "__main__":
    main()
