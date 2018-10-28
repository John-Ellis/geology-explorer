from flask import Flask, render_template
boreholeAPI = Flask(__name__)


@boreholeAPI.route('/')
def serve_location_selection():
  return render_template('location_selection_page.html')


@boreholeAPI.route('/cutaway_view')
def show_cutaway():
  return render_template('cutaway_view.html')

if __name__ == '__main__':
  boreholeAPI.run()
