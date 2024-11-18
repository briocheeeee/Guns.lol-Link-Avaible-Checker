## Description

This Python script checks the availability of usernames on the website [guns.lol](https://guns.lol). It generates combinations of usernames based on alphabetic letters and tests each one to determine whether it is **available** or **taken**. Available usernames are saved to a text file and displayed in green in the terminal, while taken usernames are displayed in red.

## Features

- **Username availability check**: Sends HTTP requests to verify if a username is available.
- **Username generation**: Creates combinations of usernames between 3 and 8 characters long.
- **Color-coded output**: Displays results in color using the **Colorama** library:
  - **Green**: Available.
  - **Red**: Taken.
- **Result saving**: Available usernames are saved in a `text.txt` file.
- **Request management**: Limits the number of requests to avoid server bans.

## Prerequisites

Before running the script, ensure the following Python libraries are installed:

- `requests`
- `beautifulsoup4`
- `colorama`

Install them using:

```bash
pip install requests beautifulsoup4 colorama
```

## Usage

1. Download the script and place it in a directory of your choice.
2. Run the script with Python:

   ```bash
   python main.py
   ```

3. The script will generate usernames, check their availability, and display the results in the terminal. Available usernames will also be saved in the `text.txt` file.

## Code Structure

- **`check_status(username)`**: Checks if a username is available on the website.
- **`print_colored_and_save(status, username)`**: Displays the status in the terminal with colors and saves available usernames to a file.
- **`generate_usernames()`**: Generates username combinations and manages requests.

## Customization

- **Username length**: Modify the `min_len` and `max_len` variables in the `generate_usernames` function to change the length of generated usernames.
- **Request throttling**: Adjust the request limit or waiting duration (currently 60 seconds after 50 requests) as needed.

## Warnings

- **Respect the servers**: This script sends repeated requests to the site. Ensure you do not overload the server or violate the site's terms of use.
- **Output file**: The `text.txt` file will be overwritten if the script is run multiple times.

## Example Output

In the terminal:

```
https://guns.lol/abc : Taken
https://guns.lol/xyz : Available
```

In `text.txt`:

```
https://guns.lol/xyz : Available
```

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request. 😊
