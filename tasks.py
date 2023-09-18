from invoke import task

@task
def crawler(ctx):
    ctx.run("python3 crawler/crawler.py")

@task
def crawlmost(ctx):
    ctx.run("python3 crawler/crawler.py most")

@task
def wrangler(ctx):
    ctx.run("jupyter notebook wrangler/wrangler.ipynb")