from flask import Flask, render_template
import Utils_11


app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = Utils_11.load_candidates_from_json()
    return render_template('list.html', candidates = candidates)

@app.route('/candidate/<int:id>/')
def profile_page(id):
    candidate = Utils_11.get_candidate(id)
    if candidate is None:
        return "Такого кандидата нет"
    return render_template('single.html', candidate=candidate)

@app.route('/search/<name>/')
def cand_by_name(name):
    candidates = Utils_11.get_candidates_by_name(name)
    number_of_cands = len(candidates)
    return render_template('search.html',
                           candidates=candidates,
                           number_of_cands=number_of_cands
                           )

@app.route('/skill/<skill>/')
def cand_skills(skill):
    candidates = Utils_11.get_candidates_by_skill(skill)
    number_of_cands = len(candidates)
    return render_template('skill.html',
                           skill=skill,
                           candidates=candidates,
                           number_of_cands=number_of_cands
                           )

if __name__ == '__main__':
    app.run()
