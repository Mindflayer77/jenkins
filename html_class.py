
class HTML:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create(data):
        name = "data_visualization.html"
        html_file = open(name,"w")
        title = ""
        with html_file as hf:
            hf.write('<!doctype html>\n')
            hf.write('<html>\n')
            hf.write('<head>\n')
            hf.write('<title>'+title+'</title>\n')
            hf.write('<meta name="description" content="Our first page">\n')
            hf.write('<meta name="keywords" content="html tutorial template">\n')
            hf.write('</head>\n')
            hf.write('<body>\n')

            for name,num_of_commits in data.items():
                hf.write(name + ": " + str(num_of_commits) + '<br>\n')

            hf.write('</body>\n')
            hf.write('</html>\n')