# import constats
# from app import app
# from flask import render_template, request
# @app.route('/hello', methods=['GET'])
# def hello():
#  # для каждого передаваемого параметра формы нужно задать
#  # значение по умолчание, на случай если пользователь ничего не введет
#  name = ""
#  gender = ""
#  program_id = 0
#  # список из номеров выбранных пользователем дисциплин
#  subject_id = []
#  # список из выбранных пользователем дисциплин
#  subjects_select = []
#
#  olympiad_id = []
#  olympiad_select = []
#
#  name = request.values.get('username')
#  gender = request.values.get('gender')
#  program_id = request.values.get('program')
#  subject_id = request.values.getlist('subject[]')
#  olympiad_id = request.values.getlist('olympiads[]')
#
#  # формируем список из выбранных пользователем дисциплин
#  subjects_select = [constats.subjects[int(i)] for i in subject_id]
#  olympiad_select = [constats.olympiads[int(i)] for i in olympiad_id]
#
#  html = render_template(
#  'hello.html',
#  name = name,
#  gender = gender,
#  program = constats.programs[int(program_id)],
#  program_list = constats.programs,
#  len = len,
#  subjects_select = subjects_select,
#  subject_list = constats.subjects,
#  olympiad_list = constats.olympiads,
#  olympiad_select = olympiad_select,
#  )
#  return html
