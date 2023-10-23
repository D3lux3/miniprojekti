from invoke import task

@task
def start(ctx):
    ctx.run("export FLASK_APP=src.app && flask run", pty=True)

@task
def crawler(ctx):
    ctx.run("python3 crawler/crawler.py")

@task
def crawlmost(ctx):
    ctx.run("python3 crawler/crawler.py most")

@task
def wrangler(ctx):
    ctx.run("jupyter notebook wrangler/wrangler.ipynb")

@task
def eda(ctx):
    ctx.run("jupyter notebook eda/eda.ipynb")