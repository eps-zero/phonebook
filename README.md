# Phonebook

The Phonebook is a command-line application implemented in Python that allows users to manage a list of contacts stored in a CSV file. The application provides features for displaying, adding, editing, and searching for contact entries.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
   - [Displaying Contacts](#displaying-contacts)
   - [Adding a Contact](#adding-a-contact)
   - [Editing a Contact](#editing-a-contact)
   - [Searching Contacts](#searching-contacts)
3. [File Structure](#file-structure)
4. [Functions](#functions)
   - [`display_entries`](#display_entries)
   - [`add_entry`](#add_entry)
   - [`edit_entry`](#edit_entry)
   - [`search_entries`](#search_entries)
5. [Main Program](#main-program)

## Introduction

The Phonebook provides a command-line interface for managing a list of contacts stored in a CSV file named `data.csv`. Users can navigate through the contact list, add new contacts, edit existing contacts, and search for specific contacts based on various criteria.

## Usage

### Displaying Contacts

The application displays contact entries in a paginated manner. Each page contains a specified number of entries (default: 5). Users can navigate through the pages using the following commands:

- `'n'`: Move to the next page.
- `'p'`: Move to the previous page.
- `'a'`: Add a new contact.
- `'e'`: Edit an existing contact.
- `'s'`: Search for contacts based on a search term.
- `'q'`: Quit the application.

### Adding a Contact

Users can add a new contact to the list by selecting the `'a'` option. The system will prompt the user to input details for the new contact, including their last name, first name, middle name, organization, work phone, and personal phone.

### Editing a Contact

To edit an existing contact, select the `'e'` option. You will be prompted to input the personal phone number of the contact you wish to edit. You can then choose to modify specific fields (last name, first name, middle name, organization, work phone, or personal phone). Changes will be saved upon confirmation.

### Searching Contacts

Select the `'s'` option to search for contacts based on a search term. The application will display matching entries and provide options to navigate through the search results in a paginated manner.

## File Structure

- `main.py`: The main program that manages user interactions and controls the flow of the application.
- `functions.py`: Contains functions for displaying, adding, editing, and searching contact entries.
- `csv_generator.py`: Provides a function for generating fake CSV data (used for demonstration purposes).
- `data.csv`: The CSV file where contact entries are stored.

## Functions

### `display_entries`

Displays contact entries in a paginated manner. Takes the list of entries, page number, and entries per page as parameters.

### `add_entry`

Prompts the user to input details for a new contact and adds the contact to the list of entries.

### `edit_entry`

Allows users to edit details of an existing contact. Prompts the user for the personal phone of the contact to be edited and provides options for modifying fields.

### `search_entries`

Searches for contacts that match a given search term. Returns a list of matching contact entries.

## Main Program

The `main()` function in `main.py` is the entry point of the application. It reads the CSV file, initializes the contact list, and manages user interactions based on their choices.
