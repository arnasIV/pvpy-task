from forms import CalculateEnergyForm
from flask import Flask, flash, render_template, request, redirect, url_for, session
from rq import Queue
from cell_power import *
import datetime
import redis
from rq.registry import FinishedJobRegistry

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PVcase'

r = redis.Redis()
q = Queue(connection=r)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculateEnergyForm(request.form)
    if request.method == 'POST' and form.validate():
        log("Adding task to the queue: {}, {}, {}, {}".format(form.name.data, form.binary.data, form.power.data, form.grid_input.data))
        job = q.enqueue(calculate_power_task, form.name.data, form.binary.data, form.power.data, form.grid_input.data)
        session['message'] = "Request submitted"
        return redirect(url_for("index"))
    saved = session.pop('message', None)
    return render_template('index.html', form=form, message=saved)

@app.route('/overview')
def show_results():
    registry = FinishedJobRegistry(queue=q)
    ids = registry.get_job_ids()
    print("Got finished jobs:", len(ids))
    res = []
    for j in ids:
        job = q.fetch_job(j)
        if job.result and job.result is not None and isinstance(job.result, ResultField):
            print("Result:", job.result.name, job.result.power, job.result.duration)
            res.append(job.result)
    return render_template('overview.html', rows=res)

if __name__ == '__main__':
    app.run(port=5555, threaded=True)
