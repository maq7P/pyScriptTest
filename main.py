import math
import random
# from utils import add_class

output_el = Element('output').element
input = Element('input').element
tasks = Element('tasks').element

task = []

def template_task_html(task):
    return f'<div class="mr-10">{task}</div><button pys-onClick="remove_task">Remove</button>'

def remove_task(*args):
    print("click")

def confirm_input(*args):
    text = input.value
    if len(text) > 0:
        task.append(text)
        input.value = ""

        output_html = ""
        for el in task:
            output_html += template_task_html(el)

        output_el.innerHTML = output_html