# flet-route-async
This is a template for running Flet with its new FastAPI engine, using flet-route for async routing 

<img src="https://s3.us-west-2.amazonaws.com/polae.io/static/polae_logo_text_label_white_256.png"  width="64">

### Setup
After cloning this repo, set up your virtual environment in the project root directory /{YOUR_ROOT_DIRECTORY}:

```
python3.10 -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
```

From the root directory run:

```
uvicorn async:app --reload
```

