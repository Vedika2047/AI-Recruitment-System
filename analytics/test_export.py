from analytics.reports import (
    export_candidates_csv
)

count = export_candidates_csv()

print(
    f"{count} Candidates Exported"
)