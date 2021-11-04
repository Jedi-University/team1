"""
Используя GitHub API для организаций (https://docs.github.com/en/rest/reference/orgs)
для первых 200 организаций нужно подсчитать ТОП-20 самых "звездных"
репозиториев(т.е. те репозитории у которых больше всего звездочек среди всех организаций).
Полученный ТОП нужно сохранить в базу используя SQLAlchemy в следующем
формате Top(id, org_name, repo_name, stars_count).
В приложение должно быть 2 команды 1 команда: fetch, которая забирает
данные с github, находит ТОП и сохраняет его в базу; 2 команда: show достает
из базы ТОП и выводит на экран. В качестве базы нужно использовать sqllite.
"""


import os
import requests
from beautifultable import BeautifulTable
import logging
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config


logging.basicConfig(level=logging.DEBUG, filename='github_api/app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


FILE_DB_NAME = "github_api/top_repos.sqlite"
DB_PATH = f"sqlite:///{FILE_DB_NAME}"
QUANTITY_ORGS = 200
GITHUB_TOKEN = config("github_token", default="")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

Base = declarative_base()


class Top(Base):
    __tablename__ = "top"

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    org_name = sa.Column(sa.TEXT)
    repo_name = sa.Column(sa.TEXT)
    stars_count = sa.Column(sa.INTEGER)


def connect_db():
    engine = sa.create_engine(DB_PATH, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def fetch(quantity_orgs=0):
    if quantity_orgs == 0:
        logging.error("Not quantity organizations.")
        exit()

    start_org_id = 1
    max_orgs_on_page = 100
    quantity_iter = 0

    quantity_iter += quantity_orgs // max_orgs_on_page
    leftover_page = quantity_orgs % max_orgs_on_page
    if leftover_page > 0:
        quantity_iter += 1

    logging.info("Start get info about organisations.")
    list_orgs = []
    for _ in range(quantity_iter):
        github_api_orgs = f"https://api.github.com/organizations?since={start_org_id}&per_page={max_orgs_on_page}"
        batch_orgs = requests.get(github_api_orgs, headers=headers).json()
        list_orgs.extend(batch_orgs)
        if list_orgs:
            start_org_id = list_orgs[-1]["id"]

    list_orgs = list_orgs[:quantity_orgs]
    logging.info("Organizations list got.")

    logging.info("Start get info about repo each organization.")
    list_repos = []
    for orgs in list_orgs:
        orgs_list_repo = requests.get(orgs["repos_url"], headers=headers).json()
        list_repos.extend(orgs_list_repo)

    sort_objects_list = sorted(list_repos, key=lambda repo: repo["stargazers_count"], reverse=True)
    twenty_repos_max_stars = sort_objects_list[:20]
    logging.info("Repo list got.")

    logging.info("Start write data in the db.")
    if os.path.exists(FILE_DB_NAME):
        os.remove(FILE_DB_NAME)

    session = connect_db()

    list_add_db = []
    for repo in twenty_repos_max_stars:
        top_item = Top(
            org_name=repo["owner"]["login"],
            repo_name=repo["name"],
            stars_count=repo["stargazers_count"]
        )
        list_add_db.append(top_item)

    session.add_all(list_add_db)
    session.commit()
    logging.info("Data about top repo stars successfully wrote.")


def show():
    logging.info("Show top repo stars.")
    session = connect_db()
    top_repos = session.query(Top).all()

    logging.info("--------> Print results. <-----------")
    print(f"All quantity: {len(top_repos)}")
    logging.info(f"All quantity: {len(top_repos)}")

    table = BeautifulTable()
    table.columns.header = ["id", "org_name", "repo_name", "stars_count"]
    for repo in top_repos:
        table.rows.append([repo.id, repo.org_name, repo.repo_name, repo.stars_count])

    print(table)
    logging.info(table)


if __name__ == "__main__":

    if requests.get("https://api.github.com/organizations", headers=headers).status_code != 200:
        logging.critical("No access to api.")
        exit()
    else:
        fetch(QUANTITY_ORGS)

    show()

    logging.info("App successfully passed.")