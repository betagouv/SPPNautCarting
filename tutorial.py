import procrastinate

app = procrastinate.App(
    connector=procrastinate.Psycopg2Connector(host="localhost", user="user", password="password", port=5434)
)
app.open()


# at the bottom of the file
@app.task(name="sum", retry=3, pass_context=True)
def sum(context: procrastinate.JobContext, a, b):
    pass
    # time.sleep(random.random() * 5)  # Sleep up to 5 seconds
    # return a + b
