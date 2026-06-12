from analytics.reports import (
    get_total_candidates,
    get_shortlisted_candidates,
    get_rejected_candidates
)

print(
    "Total Candidates:",
    get_total_candidates()
)

print(
    "Shortlisted:",
    get_shortlisted_candidates()
)

print(
    "Rejected:",
    get_rejected_candidates()
)