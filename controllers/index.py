from app import app
from flask import render_template,request
import constats
@app.route('/', methods=['GET'])
def index():

    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    olympiad_id = request.values.getlist('olympiads[]')

    subjects_select = [constats.subjects[int(i)] for i in subject_id]
    olympiad_select = [constats.olympiads[int(i)] for i in olympiad_id]

    if not name:
        name = ''
    if program_id:
        program = constats.programs[int(program_id)]
    else:
        program = constats.programs[0]

 # выводим форму

    html = render_template('index.html',
                        program_list =constats.programs,
                        len = len,
                        subject_list=constats.subjects,
                        olympiad_list = constats.olympiads

                        )

    if program_id:
        #Добавляем вывод формы
        html += render_template(
            'hello.html',
            program_list=constats.programs,
            subject_list=constats.subjects,
            olympiad_list=constats.olympiads,
            len=len,
            name=name,
            gender=gender,
            program = program,
            subjects_select=subjects_select,
            olympiad_select=olympiad_select
    )

    return html