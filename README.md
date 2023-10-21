<img src="https://s3.us-west-2.amazonaws.com/polae.io/static/polae_logo_text_label_white_256.png"  width="64">

## flet-route-async
This is a working project template for Flet using [its new FastAPI engine](https://flet.dev/blog/flet-for-fastapi) and [flet-route](https://github.com/saurabhwadekar/flet_route) for async routing.

It sets up the FletFastAPI app with its assets directory, so you can store and use static files. 

The code has been formatted using the default settings in [Black](https://black.readthedocs.io/en/stable/#).

### Setup

---

Here is the deployed [multipage Flet app using the new FastAPI server](https://enroute.fly.dev/).

To run this locally, clone the repo to `YOUR_PROJECT_ROOT_DIRECTORY`.

Navigate to this directory in your terminal.



```
cd path_to/project_root_directory/
```
Set up your virtual environment in the project root directory `/{PROJECT_ROOT_DIRECTORY}`:

```
python3.10 -m venv .venv
source .venv/bin/activate 
```
> *You may use a different version of python, but the Docker container (below) uses* `python:3.10-slim-bullseye`

The virtual environment now activated, install the required packages:



```
pip install -r requirements.txt
```


You should now be able to run the app:

```
uvicorn async:app --reload
```

View the app at [localhost](http://0.0.0.0:8080): http://0.0.0.0:8080.


### Docker
---


 If you have [Docker](https://www.docker.com/) installed on your system, you can run a container locally.

 From the project's root directory, build the docker container:

 ```
docker build -t async .
```

And run the container locally:

```
docker run -p 127.0.0.1:8080:8080 async
```

Again, you can view the app at [localhost](http://0.0.0.0:8080): http://0.0.0.0:8080.


 ### Deployment

 I have been using by the recommendation in the Flet docs, Fly.io. 


### Docs

[Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)

[Flet-Route](https://github.com/saurabhwadekar/flet_route)