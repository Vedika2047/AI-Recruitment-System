from database.db import (
    get_connection
)

from analytics.ats_score import (
    calculate_ats_score
)

from database.candidate_model import (
    update_ats_score
)


conn = get_connection()

cursor = conn.cursor(
    dictionary=True
)

cursor.execute(
    """
    SELECT id,skills
    FROM candidates
    """
)

rows = cursor.fetchall()

for row in rows:

    score = calculate_ats_score(
        row["skills"]
    )

    update_ats_score(
        row["id"],
        score
    )

    print(
        row["id"],
        score
    )

cursor.close()
conn.close()