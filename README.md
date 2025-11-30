# Suggestions — Restaurant recommender for Rome

A small command-line Python script that lets you search and display restaurants in Rome by category (e.g. "Italian", "Japanese", "Pizzeria") using the initial letters of the category.

The main script is `recommendations.py` and it relies on a `dataset.py` file containing the categories and restaurant data.

## Requirements
- Python 3.7+
- No external dependencies

## How to use

1. Make sure the repository contains a `dataset.py` file exporting two variables:
   - `categories`: a list of category names (e.g. `["Italian", "Pizzeria", "Japanese"]`)
   - `restaurants`: a dictionary that maps each category to its list of restaurants

2. Run the script:
```bash
python recommendations.py
```

The script is interactive: it will ask for the starting letters of the category you want to search. If it finds a single matching category it will show the restaurants for that category.

## Expected dataset format

Minimal example for `dataset.py`:

```python
categories = [
    "Italian",
    "Pizzeria",
    "Japanese",
    "Vegetarian"
]

restaurants = {
    "Italian": [
        ("Osteria da Mario", "4.5", "$$", "Via Roma 1, Rome"),
        ("Trattoria Bella",  "4.2", "$",  "Via Milano 12, Rome")
    ],
    "Pizzeria": [
        ("Pizzeria Da Luigi", "4.6", "$", "Via Napoli 3, Rome")
    ],
    "Japanese": [
        ("Sushi Roma", "4.7", "$$$", "Via Veneto 7, Rome")
    ],
    "Vegetarian": [
        ("Verde e Buono", "4.3", "$$", "Piazza Navona 4, Rome")
    ]
}
```

- `categories` is a list of strings.
- `restaurants` is a dictionary: key = category name (matching the entries in `categories`), value = list of tuples for each restaurant.
- Each restaurant tuple should follow this order: (Name, Rating, Price, Address).

Note: the script capitalizes the user's input with `.capitalize()`, so it's recommended that category names in `categories` start with an uppercase letter.

## Example session

Example terminal interaction:

```
*********************************************************
* Welcome to our restaurat's recommadatios app for Rome *
*********************************************************

What type of food do you like to eat?
Enter the beginning letters of the categories of food you want to choose:
I

This is all categories in database with your beginning letters.
---> Italian

The only option with those beginning letters is Italian.
Do you want to look a Italian restaurants? Enter 'y' for yes and 'n' for no:
y

The best 5 restaurants in Rome for your choice are:

*********************************************************

Name: Osteria da Mario
Rating: 4.5
Price:   $$
Address:  Via Roma 1, Rome
...
```

## Notes on the code and suggestions
This script is a simple demo/utility. Some points you may want to improve:

- The class name has a typo: `Recommadations`. Consider renaming it to `Recommendations`.
- The method `get_iems` likely has a typo (should be `get_items`) and currently returns a value that doesn't match its expected behavior; you can remove or fix it.
- `show_all_items` is passed a key converted to lowercase (`results[0].lower()`), so ensure dictionary keys in `restaurants` match that casing or normalize keys inside the script.
- Input validation is minimal (e.g. responses other than `y`/`n` are not handled). You could add robust validation and reprompting.
- Consider adding a non-interactive mode (pass category as a CLI argument) to support automation and testing.

If you want, I can:
- prepare a corrected and slightly improved version of the script (fix typos, add input validation and case-insensitivity),
- add a sample `dataset.py`,
- or add CLI argument support and simple tests.

## Contributing
To contribute:
- Open a pull request with your changes.
- Or open an issue first to discuss larger changes or new features.

## License
Add the license of your choice (e.g. MIT). If none is specified, consider adding a `LICENSE` file.

Author: Gianfy

