# IMDB-API-Project

## Introduction
This program lets you dive deep into any movie or series. Just enter the title you want to analyze, and we'll check if it's available in our database. You can choose to revisit a previous search or look up something new. Once you make your choice, you'll get a variety of options for the selected title.

### Features
1. Full overview
2. View ratings
3. View and download poster
4. View trailer
5. Compare two titles
6. Return to main menu
7. Exit

After each option, you can either exit the program or return to the main menu with all the options for that title. To enter a new title, restart the program. We use OMDB's API to fetch information for your analyses. More details about the API are below.

## About the OMDB API
The OMDB API key is free and needs to be obtained before you start coding. Set the key as a default parameter to avoid repeating it every time you use the OMDB functions. Install the OMDB library into your project to avoid going through the HTTPS route. Check out the [OMDB documentation on the PyPy website](https://pypi.org/project/omdb/) for more details.

The data types returned can be JSON or XML, but JSON is standard. Be aware of the data type being returned, as some functions return only a string or list, which can be an issue if you expect a JSON file. The most useful functions are `get`, `search_movie`, and `search_series`. The `get` function retrieves detailed information about a specified movie or series. Note that the Rotten Tomatoes parameter does not work due to legal reasons.

Pay attention to the data type returned for various keys. For example, the value rating returns information as a list of dictionaries, so you might need to use loops to process the data. The search functions return lists of dictionaries with details about movies or series matching the input string. These functions return multiple titles at once but with less detail than the `get` function.

## How to Use
1. Run the program and choose to either view your search history or look up a new movie.
2. If you choose to view previous searches, enter 'yes' and select from the list of previous searches. You'll then be shown the main menu.
3. If you choose to look up a new title, enter 'no' and type the title of the movie or series you want to look up. Specify if it's a movie or series by entering the corresponding number. Select the matching title from the list shown.
4. Once you're at the main menu, select the number corresponding to your desired option.

### Special Inputs
1. **View trailer:** Asks if you want to view the trailer in a new tab. Enter 'yes' or 'no'.
2. **View poster:** Similar to the view trailer option.
3. **Compare titles:** Prompts for another title to compare, following the same process as the initial title entry.

After each action, you'll see options to either exit or return to the main menu. If you choose to exit, a goodbye message will be shown, and the output will clear. To enter a new title, restart the program.

Thanks for using Movie Mania! Enjoy exploring your favorite movies and series.
