import jinja2
import pdfkit
import data

if __name__ == '__main__':
    data.main()

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("pdf.html")
output_data = template.render(data.order_data)
options = {
    'page-width': '117mm',
    'page-height' : '85mm',
    'margin-bottom' : '0',
    'margin-left' : '0',
    'margin-right' : '0',
    'margin-top' : '0'
}

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_string(output_data, f'{data.order_data["order_no"]}-certifikat.pdf', configuration=config, options=options, css='pdf1.css')


