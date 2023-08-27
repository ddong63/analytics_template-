from jinja2 import Environment, FileSystemLoader
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

def generate_hive_template(table_name):
    template_file = 'hive_template.sql'  # Replace with your actual template filename
    template = env.get_template(template_file)
    rendered_template = template.render(table_name=table_name)

    project_folder = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(project_folder, f'{table_name}_template.sql')

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_template)
    
    return output_path

def generate_excel_template(output_path, results):
    # Generate Excel template
    pass  # Replace with your Excel template generation code
    
