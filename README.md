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

## Contributing
To contribute:
- Open a pull request with your changes.
- Or open an issue first to discuss larger changes or new features.

## License
Add the license of your choice (e.g. MIT). If none is specified, consider adding a `LICENSE` file.

Author: Gianfy

