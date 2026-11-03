import bcrypt

from config.database import get_connection


def register_user(full_name, email, password):

    connection = get_connection()

    if connection is None:
        return False, "Database connection failed."

    try:
        cursor = connection.cursor()

        # Check whether email already exists
        cursor.execute(
            "SELECT user_id FROM users WHERE email = %s",
            (email,)
        )

        if cursor.fetchone():
            return False, "Email already registered."

        # Hash password
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        # Insert user
        query = """
            INSERT INTO users (full_name, email, password)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (full_name, email, hashed_password.decode("utf-8"))
        )

        connection.commit()

        return True, "Registration successful!"

    except Exception as error:
        connection.rollback()
        return False, f"Registration failed: {error}"

    finally:
        cursor.close()
        connection.close()


def authenticate_user(email, password):

    connection = get_connection()

    if connection is None:
        return False, None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT user_id, full_name, email, password
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()

        if user is None:
            return False, None

        stored_password = user["password"].encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), stored_password):

            user.pop("password")

            return True, user

        return False, None

    except Exception as error:
        print(f"Login Error: {error}")
        return False, None

    finally:
        if cursor:
            cursor.close()

        connection.close()