from typing import Dict, List
from job_model import JobPost


def extract_skills(text: str)-> list[str]:

    skills = ['aws', 'python', 'sql', 'django']

    skills_found = []
    text = text.lower()

    for skill in skills:
        if skill in text:
            skills_found.append(skill)


    return skills_found


def job_skill_counter(jobs: List[JobPost])-> Dict[str, int]:
    skill_counts: Dict[str, int] = {}

    for job in jobs:
       for skill in extract_skills(job.description):
           skill_counts[skill] = skill_counts.get(skill, 0) + 1


    return skill_counts










