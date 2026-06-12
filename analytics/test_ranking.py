from analytics.reports import (
    get_candidate_ranking
)

candidates = (
    get_candidate_ranking()
)

rank = 1

for candidate in candidates:

    print(
        rank,
        candidate["name"],
        candidate["ats_score"]
    )

    rank += 1