from database.db import get_connection


def insert_candidate(data):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO candidates
    (
        name,
        email,
        phone,
        skills,
        education,
        experience
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        data["name"],
        data["email"],
        data["phone"],
        data["skills"],
        data["education"],
        data["experience"]
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

def get_all_candidates():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM candidates"
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def get_candidate_by_id(candidate_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM candidates
    WHERE id=%s
    """

    cursor.execute(
        query,
        (candidate_id,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def update_candidate_score(
    candidate_id,
    score
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE candidates
    SET ats_score=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            score,
            candidate_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def delete_candidate(candidate_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE FROM candidates
    WHERE id=%s
    """

    cursor.execute(
        query,
        (candidate_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

from database.db import get_connection


def update_ats_score(
    candidate_id,
    score
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE candidates
        SET ats_score=%s
        WHERE id=%s
        """,
        (
            score,
            candidate_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()
