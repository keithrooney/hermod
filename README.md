# Hermod

A simple project to learn more about load balancing using Docker and Python.

## Prerequisite(s)

The only prerequisite to run this project is `Docker` and `curl`.

## Getting Started

The quickest way to get started is running the below in one terminal.

```
$ docker-compose up --scale web=3
```

Then execute a `curl` request to `localhost:8080` at least three times.

```
$ curl "http://localhost:8080/health"
{"state":"up"}
$ curl "http://localhost:8080/health"
{"state":"up"}
$ curl "http://localhost:8080/health"
{"state":"up"}
```

You should see something like the following in the terminal you ran `docker-compose` in.

```
web_3    | 172.18.0.5 - - [07/Jul/2021 20:56:32] "GET /health HTTP/1.0" 200 -
nginx_1  | 172.18.0.1 - - [07/Jul/2021:20:56:32 +0000] "GET /health HTTP/1.1" 200 15 "-" "curl/7.68.0"
web_2    | 172.18.0.5 - - [07/Jul/2021 20:56:33] "GET /health HTTP/1.0" 200 -
nginx_1  | 172.18.0.1 - - [07/Jul/2021:20:56:33 +0000] "GET /health HTTP/1.1" 200 15 "-" "curl/7.68.0"
web_1    | 172.18.0.5 - - [07/Jul/2021 20:56:34] "GET /health HTTP/1.0" 200 -
nginx_1  | 172.18.0.1 - - [07/Jul/2021:20:56:34 +0000] "GET /health HTTP/1.1" 200 15 "-" "curl/7.68.0"
```

Since our NGINX is operating using round robin, it will hit all three web instances.

## Conclusion

* Docker is awesome!
* Python is awesome!
* Technology in general is awesome!
