# Bank Management System

This is a simple Bank Management System project implemented in Python. It allows users to create accounts, sign in, deposit and withdraw funds, perform balance inquiries, and transfer funds between accounts.

## Features

-   User registration and authentication
-   Account creation with unique account numbers
-   Balance inquiry
-   Cash deposit
-   Cash withdrawal
-   Fund transfer between accounts
-   Transaction history

## Requirements

-   Python 3.6+
-   MySQL database
-   `mysql-connector-python` library

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  Install the required Python libraries:

    ```bash
    pip install mysql-connector-python
    ```

3.  Set up the MySQL database:

    -   Create a database named `bank`.
    -   Run the [database.py](database.py) file to create the `customers` table:

        ```bash
        python database.py
        ```

## Configuration

-   Modify the database connection details in [database.py](database.py) to match your MySQL setup:

    ```python
    # filepath: e:\python projects\Bank Management System Project\database.py
    mydb = sql.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    ```

## Usage

1.  Run the [main.py](main.py) file:

    ```bash
    python main.py
    ```

2.  Follow the on-screen instructions to sign up or sign in.

3.  After successful sign-in, you can access the banking services menu.

## File Structure

-   [main.py](main.py): Main entry point of the application. Handles user interaction and calls other modules.
-   [register.py](register.py): Handles user registration and sign-in functionality.
-   [bank.py](bank.py): Implements banking services such as deposit, withdraw, fund transfer, and balance inquiry.
-   [customer.py](customer.py): Defines the [`Customer`](customer.py) class for creating and managing customer accounts.
-   [database.py](database.py): Manages the database connection and executes SQL queries.

## Database Schema

The `customers` table in the `bank` database has the following schema:

| Column         | Type          | Constraints       |
| -------------- | ------------- | ----------------- |
| username       | VARCHAR(20)   | NOT NULL, PRIMARY KEY |
| password       | VARCHAR(20)   | NOT NULL          |
| name           | VARCHAR(25)   | NOT NULL          |
| age            | INTEGER       | NOT NULL          |
| city           | VARCHAR(20)   | NOT NULL          |
| balance        | INTEGER       | NOT NULL          |
| account\_number | INTEGER       | NOT NULL          |
| status         | BOOLEAN       | NOT NULL          |

Each customer also has a transaction table named `<username>_transaction` with the following schema:

| Column         | Type          |
| -------------- | ------------- |
| timedate       | VARCHAR(30)   |
| account\_number | INTEGER       |
| remarks        | VARCHAR(30)   |
| amount         | INTEGER       |

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.