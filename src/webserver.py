from sanic import Sanic, response
from src.utils.logger import SANIC_CONFIG

app = Sanic(__name__, log_config=SANIC_CONFIG)


app.static("/assets", "src/web/assets/")
app.static("/favicon.ico", "src/web/favicon.ico")


@app.route("/")
async def main(req):
    return response.html(open("src/web/index.html").read())
