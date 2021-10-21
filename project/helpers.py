from flask import Flask, redirect, session, render_template
from functools import wraps


def login_required(f):
  """
  Decorate routes to require login.
  https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
  """
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
      return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function


def error(message, code=400):
  """Render error message"""
  return render_template("error.html", msg=message, code=code)


#*******************************************
#* Data Validation
#*******************************************
#TODO: write generic check blank field function
#TODO: write generic check positive integer field function

def add_goal_validation(title, description, completions_required, reward):

  # Title
  if not title: # check if blank
    return False, "Title field cannot be blank"
  
  # Description
  if not description:
    return False, "Description field cannot be blank"

  # Completions required
  if not completions_required:
    return False, "Number of completions required field cannot be blank"
  try:
    completions_required = int(completions_required)
  except ValueError:
    return False, "Number of completions required field can only include whole numbers"
  if completions_required <= 0:
    return False, "Number of completions required field must be a positive value"

  return True, ""
  