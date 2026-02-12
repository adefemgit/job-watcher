from typing import Dict

from  jobwatcher.job_model import JobPost
from jobwatcher.ext_skills_needed import job_skill_counter


def print_report(counts: Dict[str, int]) -> None:
    print("--- Skill Report ---")

    if not counts:
        print("No skills found")
        return

    for skill, count in sorted(counts.items()):
        print(f"{skill}: {count}")


def main() -> None:

    jobs = [
        JobPost(
            title="Junior backend developer",
            company="google",
            location="Remote",
            description="Python and SQL required. Django is a plus.",
            url="www.indeed.com/jobs?q=python+django&start=0",
        ),
        JobPost(
            title="cloud engineer",
            company="oracle",
            location="Remote",
            description="aws and python  experience required.",
            url="linkedin.com",
        ),
    ]

    counts = job_skill_counter(jobs)
    print_report(counts)

if __name__ == "__main__":
    main()