import random
from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

#create list with cards, we want to have 16 cards - 8 paris
card_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
random.shuffle(card_values)


#define the root file, not sure why pycharm isn't able to detect the file (?)
@app.route("/")
def home():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)