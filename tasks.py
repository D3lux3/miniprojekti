from invoke import task

@task
def crawler(ctx):
    ctx.run("python3 crawler/crawler.py")

@task
def crawlmost(ctx):
    ctx.run("python3 crawler/crawler.py &sp=CAM%253D")