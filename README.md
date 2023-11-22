# First-ML-Model-Deployment

[![Express Logo](https://storage.googleapis.com/kaggle-datasets-images/19/19/default-backgrounds/dataset-card.jpg)](https://archive.ics.uci.edu/dataset/53/iris)

This is my first ML model deployment using [Flask](https://flask.palletsprojects.com/en/3.0.x/).

Make sure to install [Python](https://www.python.org/).

First I created a simple model to predict the flower species. I used the Random Forest Algorithm for prediction.

Clone this repository to Desktop.

```console
$ git clone https://github.com/soumyamandal007/First-ML-Model-Deployment.git
```

Then go into the Directory. Create a virtual environment.

```console
$ python -m venv env
```

Activate the Virtual environment.

```console
$ .\env\Scripts\activate
```

Install all the requirements.

```console
$ pip install -r requirements.txt
```

Then Run the model.py file in the same directory. It will create the model.pickle file, which will later on be used in app.py file to send 
prediction to frontend.

```console
$ python model.py
```

When you get the model.pickle file. Then run the app.py file.

```console
$ python app.py
```

Then in the terminal, you will see localhost server has been started. Copy the link to any browser.

```console
http://127.0.0.1:5000
```

And Voila !!!!! :)



