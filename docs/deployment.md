# <img src="https://s3.us-west-2.amazonaws.com/polae.io/static/polae_logo_text_label_white_256.png"  width="48">  Multipage async Flet app

<!-- ## Deploy: flet-route-async 
This is a working project template for Flet using [its new FastAPI engine](https://flet.dev/blog/flet-for-fastapi) and [flet-route](https://github.com/saurabhwadekar/flet_route) for async routing. -->

The Dockerfile provides for a container to run the app locally, or in the cloud.

I am seeking advice on how to best deploy this app with a path to maximum (optimal) concurrency in the app and responsive scalabilty. Please share your thoughts.

### Deployment

I have deployed this app on [Fly.io](https://fly.io), which is a recommended service provider in the Flet docs. 

After you have created an account and [installed fly on your system](https://fly.io/docs/hands-on/install-flyctl/), you can run (from your root directory):

```
fly auth login
```

Now that you are logged in, from your root directory, create an app:

```
fly launch
```

You will be led through a series of questions. 
>N.B.: The app name will be used in the fly.toml file below. here are the [questions](https://fly.io/docs/hands-on/launch-app/), if you'd like a reference.

You don't need these ...

```
? Would you like to set up a Postgresql database now? No
? Would you like to set up an Upstash Redis database now? No
```

This process will configure and write a `fly.toml` file in your working directory:
>See [Fly Docs](https://fly.io/docs/reference/configuration/) for more information about how to use this file.

```
#fly.toml
app = "<YOUR-CREATED-FLY-APP-NAME"
primary_region = "iad"

[build]

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]
```

Now, deploy the app.

```
fly deploy
```

Visit your newly deployed app at https://--YOUR-CREATED-FLY-APP-NAME--.fly.dev/






