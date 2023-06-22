import os
import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = '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'

print(openai.Model.list())
#
# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)
#
#
# def generate_prompt(animal):
#     return """How should I recover from failure from {}""".format(
#         animal.capitalize()
#     )
#
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=generate_prompt('studying'),
#   temperature=1
# )
# print(response.choices[0]["text"])