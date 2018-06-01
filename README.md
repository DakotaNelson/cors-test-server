# CORS Test Server

This client/server demo can be used to play around with CORS to get a better understanding of how it works.

## To Use

In one terminal:

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

In another:
```
cd static
python -m http.server 8080
```

If you're using python 2, please consider upgrading (python 2 is officialy end-of-life on Jan. 1, 2020), or use `python -m SimpleHTTPServer` instead of `python -m http.server`.

Once everything is running, you can visit `localhost:8080/cors-test-table.html` (or whatever port you chose to host with the python static server) and watch the table of examples populate. If you open up the browser console, you'll see more detail there as well.

Play around with the code a little and see what's going on - keep in mind that you'll need to restart Flask every time you change something server-side, but you should only have to refresh if you change anything on the client.

Have fun!

### Project Ideas

- Add an endpoint that validates the `origin` header manually before reflecting it in the `Access-Control-Allow-Origin` header. Can you trick your validation?
- What happens if you inject strange things into the `origin` header, which is then reflected back from the server?
- What happens if you add the `Access-Control-Expose-Headers` header (see: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)?
- How do various cookie flags impact that cookie's use in cross-origin requests?
