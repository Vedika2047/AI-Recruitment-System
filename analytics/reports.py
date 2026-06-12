from database.db import get_connection


def get_total_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM candidates"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_shortlisted_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM candidates
        WHERE status = 'Shortlisted'
        """
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_rejected_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM candidates
        WHERE status = 'Rejected'
        """
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

import pandas as pd
from database.db import get_connection

def export_candidates_csv():

    conn = get_connection()

    query = """
    SELECT *
    FROM candidates
    """

    df = pd.read_sql(
        query,
        conn
    )

    df.to_csv(
        "exports/candidates.csv",
        index=False
    )

    conn.close()

    return len(df)

def get_top_skills():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT skills
        FROM candidates
        """
    )

    rows = cursor.fetchall()

    skill_count = {}

    for row in rows:

        skills = row["skills"]

        if not skills:
            continue

        skill_list = skills.split(",")

        for skill in skill_list:

            skill = skill.strip()

            if skill in skill_count:

                skill_count[skill] += 1

            else:

                skill_count[skill] = 1

    cursor.close()
    conn.close()

    return dict(
        sorted(
            skill_count.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

def get_candidate_ranking():

    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT
            id,
            name,
            email,
            ats_score
        FROM candidates
        ORDER BY ats_score DESC
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def get_top_candidate():

    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM candidates
        ORDER BY ats_score DESC
        LIMIT 1
        """
    )

    candidate = cursor.fetchone()

    cursor.close()
    conn.close()

    return candidate

def get_dashboard_summary():

    return {
        "total_candidates": get_total_candidates(),
        "shortlisted": get_shortlisted_candidates(),
        "rejected": get_rejected_candidates(),
        "top_skills": get_top_skills(),
        "top_candidate": get_top_candidate()
    }