from database.db import get_connection


def register_customer(name, phone, address, date_of_birth):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO customers
            (name, phone, address, date_of_birth)
            VALUES (?, ?, ?, ?)
        """, (name, phone, address, date_of_birth))

        connection.commit()

        # Get the ID of the newly created customer
        customer_id = cursor.lastrowid

        return True, customer_id

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        connection.close()


def get_customer(customer_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM customers
        WHERE customer_id = ?
    """, (customer_id,))

    customer = cursor.fetchone()

    connection.close()

    return customer