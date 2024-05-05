# Expense Sharing Application

The Expense Sharing Application is a web application designed to help users manage and track shared expenses among a group of people. It allows users to create and manage expenses, view their balances, and settle debts with other users.

## Features

- **User Management**: Users can create accounts and manage their personal information.
- **Expense Creation**: Users can create expenses, specifying the type (equal, exact, or percent) and participants involved.
- **Balance Tracking**: The application tracks balances between users, showing how much each user owes or is owed by others.
- **API Endpoints**: Provides APIs for creating expenses, retrieving user expenses, and getting user balances.

## Technologies Used

- **Django**: Backend framework for building the web application.
- **PostgreSQL**: Database management system for storing user data, expenses, and balances.

## Note: Setup your PostgreSQL database in your system to run this application.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kumarawanish/splitwise.git
```

2. Navigate to the project directory:

```bash
cd expense-sharing-app
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

1. POST /api/users/: Create a new user.
2. POST /api/expenses/: Create a new expense.
3. GET /api/users/int:user_id/expenses/: Retrieve expenses for a specific user.
4. GET /api/users/int:user_id/balances/: Retrieve balances for a specific user.
