# requests/

Request queue for the `analyze` workflow. Pushing a new or changed `requests/*.txt` file to a `claude/**` branch runs the workflow. It analyzes each URL in the file and commits the outputs to `main`.

Each line holds one request (blank lines and `#` comments are ignored):

```
https://youtu.be/VIDEO_ID [--force] [--low-res] [--engine=agentic|--engine=static]
```

Push-triggered runs install the code from the pushed commit, so a fix on a branch can be tried before it is merged. Re-queue a request by editing its file (for example, adding a `#` comment line).

This exists so an agent that can push commits but can't dispatch workflows can still queue videos. The files also serve as a log of what was requested.
