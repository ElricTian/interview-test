import mongoengine


class DoubanSpider(mongoengine.Document):
    title = mongoengine.StringField()
    director = mongoengine.StringField()
    actors = mongoengine.StringField()
    region = mongoengine.StringField()
    score = mongoengine.StringField()
    release = mongoengine.StringField()
    duration = mongoengine.StringField()
    buy_url = mongoengine.StringField()

