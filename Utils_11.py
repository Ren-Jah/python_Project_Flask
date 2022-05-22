import requests
from pprint import pprint as pp

PATH = 'https://jsonkeeper.com/b/KKRV'


def load_candidates_from_json(path=PATH):
    """возвращает список всех кандидатов"""
    res = requests.get(path)
    data = res.json()
    return data


def get_candidate(id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == id:
            return candidate


def get_candidates_by_name(name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    cands_by_name = []
    for candidate in candidates:
        if name.lower() in candidate["name"].lower():
            cands_by_name.append(candidate)
            continue
    return cands_by_name


def get_candidates_by_skill(skill):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json()
    cands_by_skill = []
    skill_lower = skill.lower()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_lower in skills:
            cands_by_skill.append(candidate)
            continue
    return cands_by_skill


