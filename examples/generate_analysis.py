import os
from data_science_template.template_generator import generate_hive_template, generate_excel_template

def data_science_template(template, folder, client):
    if template == 'benchmark report':
        # Create folder structure
        if folder:
            folder_name = f'benchmark_report_{client}'
            os.makedirs(folder_name, exist_ok=True)

            code_folder = os.path.join(folder_name, 'code')
            os.makedirs(code_folder, exist_ok=True)

            # Generate Hive SQL template and save
            hive_template_path = generate_hive_template(table_name='customer_data')
            hive_template_filename = os.path.basename(hive_template_path)
            os.rename(hive_template_path, os.path.join(code_folder, hive_template_filename))

            # Generate Excel template and save
            excel_template_path = generate_excel_template(output_path=os.path.join(code_folder, 'excel_template.xlsx'), results=None)

            print(f'Generated folder and files for {template} analysis: {folder_name}')

if __name__ == '__main__':
    data_science_template(template='benchmark report', folder=True, client='ABC')
