import gradio as gr
gr.close_all()

def greet(name):
  return "Hello, "+ name + "!"

demo =gr.Interface(
  fn=greet,
  inputs=[gr.Textbox(label="Name: "),
  gr.Slider(label="Age: "),
  gr.Radio(labelo="Subject Preference: ", choices=['C', 'C#', 'Java', 'Python']),
  gr.Checkboxgroup(label='Hobbies:', choices=['Painting', 'Singing', 'Reading', 'Gaming'])
         ],
  outputs=[gr.Textbox()],
)

demo.launch
