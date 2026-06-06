from database.candidate_model import (
    insert_candidate,
    get_all_candidates
)

candidate = {

    "name": "Vedika",

    "email": "vedika@gmail.com",

    "phone": "9876543210",

    "skills": "Python,SQL",

    "education": "BE Computer",

    "experience": "Fresher"
}

insert_candidate(candidate)

print(
    get_all_candidates()
)