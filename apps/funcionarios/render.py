import io

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile



class Render:

    @staticmethod
    def render(template_uri: str, params: dict, name_file: str):
        response = None
        template_string = render_to_string(template_uri, params)
        html = HTML(string=template_string)
        result = html.render(stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css']).write_pdf()

        if result:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename=%s.pdf' % name_file
            # response['Content-Disposition'] = 'attachment; filename=%s.pdf' % name_file
            # response['Content-Transfer-Encoding'] = 'iso-8859-1'
            response['Content-Transfer-Encoding'] = 'binary'
            with tempfile.NamedTemporaryFile(delete=True) as output:
                output.write(result)
                output.flush()
                output = open(output.name, 'rb')
                response.write(output.read())
        else:
            response = HttpResponse("Error ao gerar PDF", status=400)

        return response




        # html_string = render_to_string(template_uri, params)
        # css = CSS(filename='static/bootstrap/css/bootstrap.css')
        # html = HTML(string=render_to_string(template_uri, params))
        # result = html.render(stylesheets=['static/bootstrap/css/bootstrap.css']).write_pdf()
        # response = None

        # if result:
        #     response = HttpResponse(content_type='application/pdf')
        #     response['Content-Disposition'] = 'filename=%s.pdf' % name_file
        #     # response['Content-Disposition'] = 'attachment; filename=%s.pdf' % name_file
        #     # response['Content-Transfer-Encoding'] = 'iso-8859-1'
        #     response['Content-Transfer-Encoding'] = 'binary'
        #     with tempfile.NamedTemporaryFile(delete=True) as output:
        #         output.write(result)
        #         output.flush()
        #         output = open(output.name, 'rb')
        #         response.write(output.read())
        # else:
        #     response = HttpResponse("Error ao gerar PDF", status=400)
        #
        # return response

        # template = get_template(template_uri)
        # html = template.render(params)
        # response = None
        # _io = io.BytesIO()
        # pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), _io)
        # if not pdf.err:
        #     response = HttpResponse(_io.getvalue(), content_type='application/pdf')
        #     response['Content-Disposition'] = 'attachment:filename=%s.pdf' % name_file
        #     return response
        # else:
        #     return HttpResponse("Error ao gerar PDF", status=400)

