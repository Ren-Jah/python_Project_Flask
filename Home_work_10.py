import requests
from flask import Flask

app = Flask(__name__)

cand = 'https://jsonkeeper.com/b/70OY'
res = requests.get(cand)
data = res.json()
splitter = "---------------------------------"
#skills_list = ["go", "python", "Delphi", "pascal", "fortran", "basic", "html", "Django", "flask"]


@app.route("/")
def main_page():
    """Вывод на главную страницу всех кандидатов"""
    candidates = data
    all_cand = ""
    for candidate in candidates:
        all_cand += f"Имя кандидата - {candidate['name']}\n"
        all_cand += f"Позиция кандидата {candidate['position']}\n"
        all_cand += f"Навыки: {candidate['skills']}\n"
        all_cand += splitter + "\n"

    return "<pre>" + all_cand + "<pre>"


@app.route('/candidates/<int:x>')
def profile_page(x):
    """Вывод профиля кандидата"""
    candidates = data
    cand_profile = ""
    if x in range(len(candidates) + 1):
        cand_profile += f"<img src= \"{candidates[x - 1]['picture']}\">\n"
        cand_profile += f"\n"
        cand_profile += f"Имя кандидата - {candidates[x - 1]['name']}\n"
        cand_profile += f"Позиция кандидата {candidates[x - 1]['position']}\n"
        cand_profile += f"Навыки: {candidates[x - 1]['skills']}\n"
    else:
        cand_profile += f"Такого кандидата нет"

    return "<pre>" + cand_profile + "<pre>"


@app.route('/skills/<skill>')
def cand_skills(skill):
    """Выводит кандидатов по запрашиваемым скиллам"""
    candidates = data
    cands_by_skill = ""
    skill_lower = skill.lower()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_lower in skills:
            cands_by_skill += f"Имя кандидата - {candidate['name']}\n"
            cands_by_skill += f"Позиция кандидата {candidate['position']}\n"
            cands_by_skill += f"Навыки: {candidate['skills']}\n"
            cands_by_skill += splitter + "\n"
        else:
            continue

    if len(cands_by_skill) == 0:
        cands_by_skill += "Подходящих кандидатов нет"

    return "<pre>" + cands_by_skill + "<pre>"


if __name__ == '__main__':
    app.run()
