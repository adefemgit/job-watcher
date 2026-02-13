import json
from pathlib import Path
from typing import List

from jobwatcher.job_model import JobPost



def load_jobs_from_file(filepath: str) -> List[JobPost]:
    filepath = Path(filepath)

    with filepath.open("r") as file:
        data = json.load(file)

    jobs: List[JobPost] = []

    for item in data:
        job = JobPost(
            title=item["title"],
            company=item["company"],
            location=item["location"],
            description=item["description"],
            url=item["url"],
        )
        jobs.append(job)

    return jobs
