from flask import Flask, render_template
from livereload import Server
boreholeAPI = Flask(__name__)


@boreholeAPI.route('/')
def serve_location_selection():
  return render_template('location_selection_page.html')


@boreholeAPI.route('/cutaway_view/<location>')
def show_cutaway(location):
  # TODO use location to get borehole data
  bore_hole_data = {"lithological_data": ["blah", "blah", "blob"]}
  return render_template('cutaway_view.html', bore_hole_data=bore_hole_data)


# Wrapper to enable live-reload
boreholeAPI.debug = True
server = Server(boreholeAPI)

if __name__ == '__main__':
  server.serve()
