from app.models import Racing, db
from app.main.collect import main_func
from pathlib import Path

PATH_DATA = Path(__file__).absolute().parents[1] / 'data'
data = main_func(PATH_DATA)

def generate(db):
    with db:
        db.create_tables([Racing])
        for team in data:
            Racing.create(
                abbr=team,
                name=data[team]['name'],
                team=data[team]['team'],
                time=data[team]['time']
            )


if __name__ == '__main__':
    generate(db)