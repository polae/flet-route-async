
# <img src="https://s3.us-west-2.amazonaws.com/polae.io/static/polae_logo_text_label_white_256.png"  width="48">  Multipage Async Flet App
#### using [Flet-Route](https://github.com/saurabhwadekar/flet_route)

## This Repo: flet-route-async 
This is a working project template for [Flet](https://flet.dev/) using [its new FastAPI engine](https://flet.dev/blog/flet-for-fastapi) and [flet-route](https://github.com/saurabhwadekar/flet_route) for async routing.

It sets up the FletFastAPI flet app server with its assets directory, so you can store and use static files, and load fonts, etc.

The code has been formatted using the default settings in [Black](https://black.readthedocs.io/en/stable/#).

>Your comments are very welcome.

### Setup

---

Here is the deployed [Multipage Async Flet App using the new FletFastAPI server](https://flet-route-async.fly.dev/) on [Fly.io](https://fly.io/).

To run this locally, [clone the repo](https://github.com/polae/flet-route-async) to your `PROJECT_ROOT_DIRECTORY`.

Navigate to this directory in your terminal.


```
cd path_to/project_root_directory/
```
Now in the project root directory, create your virtual environment.

```
python3.10 -m venv .venv
```
> You may use a different version of python, but the Docker container (below) uses `python:3.10-slim-bullseye`.

Activate the virtual environment.
```
source .venv/bin/activate 
```


And install the required packages:


```
pip install -r requirements.txt
```


You should now be able to run the app:

```
uvicorn async:app --reload
```

View the app at localhost: http://0.0.0.0:8080.


### Docker
---

 If you have [Docker](https://www.docker.com/) installed on your system, you can run a container locally by building and running the container with the `Dockerfile` from the project root directory.

 `Dockerfile`

   ```
   FROM python:3.10-slim-bullseye

  ENV PYTHONUNBUFFERED True

  WORKDIR /app

  COPY ./requirements.txt ./
  RUN pip install --no-cache-dir -r requirements.txt

  COPY . .

  EXPOSE 8080

  CMD ["uvicorn", "enroute:app", "--host", "0.0.0.0", "--port", "8080"]
   ```

 From the project's root directory, build the docker container:

 ```
docker build -t async .
```

And run the container locally:

```
docker run -p 127.0.0.1:8080:8080 async
```

Again, you can view the app at localhost: http://0.0.0.0:8080.


## Further

I would also like to understand [the best way to deploy this app](docs/deployment.md).  

### Docs

[Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)

[Flet-Route](https://github.com/saurabhwadekar/flet_route)