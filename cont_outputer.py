# -*- coding: utf-8 -*-
class ContOutputer(object):
    def __init__(self):
        pass

    def output_html_info(self, cont):
        with open ('movies_info.html', 'w', encoding='utf-8') as file:
            movies_list = sorted(cont, key=lambda movie: (movie.get('评分', 0)), reverse=True)

            file.write("<html>")
            file.write("<body>")
            file.write("<table>")

            for movie in movies_list:
                file.write("<tr>")
                file.write("<td>%s</td>" % movie['影片名'])
                file.write("<td>%s</td>" % movie['评分'])
                file.write("<td>%s</td>" % movie['链接'])
                file.write("</tr>")

            file.write("</table>")
            file.write("</body>")
            file.write("</html>")