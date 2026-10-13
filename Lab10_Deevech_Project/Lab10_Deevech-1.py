"""
Program: Lab10_Deevech-1.py - Word Count
Author: Deevech
Purpose: Let the user select a text file and display alphabetical word counts
using a class, pathlib, string manipulation, and exception handling.
Starter code: No starter code used.
Date: October 13, 2026
"""

import pathlib
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        self.__frequencies.clear()
        translation_table = str.maketrans("", "", string.punctuation)

        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    line = line.translate(translation_table).lower()
                    for word in line.split():
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

        except FileNotFoundError:
            print(f"File not found: {self.__filepath.name}")
            print("Place the text file in the same folder as this program.")
            return False
        except (OSError, UnicodeError) as error:
            print(f"Unable to read the file: {error}")
            return False

        return True

    def print_report(self):
        words = sorted(self.__frequencies.keys())
        if not words:
            print("No words found in this file.")
        for word in words:
            print(f"{word:<20} :: {self.__frequencies[word]}")


def main():
    folder = pathlib.Path(__file__).resolve().parent
    files = {
        "1": folder / "monte_cristo.txt",
        "2": folder / "princess_mars.txt",
        "3": folder / "Tarzan.txt",
        "4": folder / "treasure_island.txt",
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for number, filepath in files.items():
            name = filepath.stem.replace("_", " ").title()
            print(f"{number}. {name}")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in files:
            filepath = files[choice]
            print(f"\nProcessing '{filepath.name}'...\n")
            analyzer = WordAnalyzer(str(filepath))
            if analyzer.process_file():
                analyzer.print_report()
        else:
            print("Invalid choice. Please select from 1-5.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
