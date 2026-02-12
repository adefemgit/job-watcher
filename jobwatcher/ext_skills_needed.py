from typing import Dict, List


def extract_skills(text: str)-> list[str]:

    skills = ['aws', 'python', 'sql', 'django']

    skills_found = []
    text = text.lower()

    for skill in skills:
        if skill in text:
            skills_found.append(skill)


    return skills_found


def job_skill_counter(jobs: List[str])-> Dict[str, int]:
    skill_counts = {}

    for job in jobs:
        found_skills = extract_skills(job)

        for skill in found_skills:
            if skill not in skill_counts:
                skill_counts[skill] = 1
            else:
                skill_counts[skill] += 1
    return skill_counts











