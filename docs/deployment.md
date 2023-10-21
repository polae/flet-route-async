# <img src="https://s3.us-west-2.amazonaws.com/polae.io/static/polae_logo_text_label_white_256.png"  width="48">  Multipage async Flet app

<!-- ## Deploy: flet-route-async 
This is a working project template for Flet using [its new FastAPI engine](https://flet.dev/blog/flet-for-fastapi) and [flet-route](https://github.com/saurabhwadekar/flet_route) for async routing. -->

The Dockerfile provides for a container to run the app locally, or in the cloud.

### Deployment

I have deployed this app on [Fly.io](https://fly.io), which is a recommended service provider in the Flet docs. 

If you have an account and installed fly on your system, you can run (from your root directory):

```
fly auth login
```

From your root directory, create an app:

```
fly launch
```

You will be led through a series of questions:

```
q
q
q
```

This process will configure and write a fly.toml file in your working directory:
>See [Fly Docs](https://fly.io/docs/reference/configuration/) for information about how to use this file.

```
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






