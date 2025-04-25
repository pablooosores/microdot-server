from microdot import Microdot
from microdot import send_file

app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'

@app.get('index.html')
async def index(request):
    return send_file('/index.html')

@app.get('styles.css')
async def index(request):
    return send_file('/styles/base.css')

@app.get('scripts.js')
async def index(request):
    return send_file('/scripts/base.js')

app.run()
