# First-ML-Model-Deployment
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

And Voila !!!!! :)



