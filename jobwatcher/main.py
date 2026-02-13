from pathlib import Path
from typing import Dict

from  jobwatcher.job_model import JobPost
from jobwatcher.jsonloader import load_jobs_from_file

from jobwatcher.ext_skills_needed import job_skill_counter


def print_report(counts: Dict[str, int]) -> None:
    print("--- Skill Report ---")

    if not counts:
        print("No skills found")
        return

    for skill, count in sorted(counts.items()):
        print(f"{skill}: {count}")


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent  # project root
    json_path = base_dir / "jobs.json"

    jobs = load_jobs_from_file(json_path)
    counts = job_skill_counter(jobs)
    print_report(counts)

if __name__ == "__main__":
    main()