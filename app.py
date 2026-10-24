import gradio as gr
gr.close_all()

def details(name, age, preference, hobbies, profile_pic):
  return "Hello, "+ name + "!"

demo =gr.Interface(
  fn=details,
  inputs=[gr.Textbox(label="Name: "),
  gr.Slider(label="Age: "),
  gr.Radio(labelo="Subject Preference: ", choices=['C', 'C#', 'Java', 'Python']),
  gr.Checkboxgroup(label='Hobbies:', choices=['Painting', 'Singing', 'Reading', 'Gaming']),
          gr.Image(label='Profile pic'),
         ],
  outputs=[gr.Textbox()],
)

demo.launch
