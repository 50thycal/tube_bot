# requests/

Request queue for the `analyze` workflow. Pushing a new or changed `requests/*.txt` file to a `claude/**` branch runs the workflow. It analyzes each URL in the file and commits the outputs to `main`.

Each line holds one request (blank lines and `#` comments are ignored):

```
https://youtu.be/VIDEO_ID [--force] [--low-res]
```

This exists so an agent that can push commits but can't dispatch workflows can still queue videos. The files also serve as a log of what was requested.
