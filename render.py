from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("."))
print(env.get_template("test.j2").render(user="Nash"))