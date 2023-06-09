Note/Disclaimer: This code is intended to generate a simulated DMF for testing or demonstration purposes. It does not access or replicate the real SSA's Death Master File. 
The generated file contains randomly generated data, including names, dates of birth, dates of death, SSNs, and verification statuses.

### Overview: 
The provided code is a program designed to imitate the Social Security Administration's Death Master File (DMF) by generating a simulated DMF with random data for a specified number of individuals.
The program allows the user to input the number of random generations to imitate the DMF and then creates a CSV file containing the simulated DMF data.

Here is an overview of the code's functionality:

#### Importing necessary modules:
- csv: Enables reading and writing CSV files.
- random: Provides functions for generating random values.
- date and timedelta: Provide date and time functionality.
- generate_ssn(existing_ssns): A function that generates a unique random Social Security Number (SSN) by combining random numbers. It ensures the generated SSN does not exist in the existing_ssns set.
- generate_date_of_birth(): A function that generates a random date of birth between January 1, 1900, and the current date.
- generate_date_of_death(date_of_birth): A function that generates a random date of death after the specified date of birth.
- generate_verification(): A function that generates a random verification status (either "Verified" or "Not Verified").
- generate_death_master_file(num_people): A function that generates the simulated Death Master File with the specified number of people.

It creates the field names and rows of data using random values generated by the helper functions. The SSNs are checked for uniqueness using the existing_ssns set.
The generated data is then saved to a CSV file with a filename containing the current date.

#### Main program loop:
- Asks the user to enter the number of random generations to imitate the DMF.
- Calls the generate_death_master_file() function with the provided number of people.
- If the generation is successful, the loop breaks; otherwise, the user is prompted to enter a valid number.
- Displays a completion message when the program finishes.

