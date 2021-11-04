
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from beautifultable import BeautifulTable
import os
import logging
from github_api_cls.consts import DB_PATH, FILE_DB_NAME


logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

Base = declarative_base()


class Top(Base):
    __tablename__ = "top"

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    org_name = sa.Column(sa.TEXT)
    repo_name = sa.Column(sa.TEXT)
    stars_count = sa.Column(sa.INTEGER)


class DB:

    def __init__(self):
        self.db_path = DB_PATH
        self.session = self.connect_db()

    def connect_db(self):
        """Connect to the database"""
        logging.info("Start connect to the database")
        engine = sa.create_engine(self.db_path, echo=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(engine)
        logging.info("Session create")
        return session()

    def write_db(self, twenty_repos_max_stars):
        logging.info("Start write to the database.")
        list_add_db = []
        for repo in twenty_repos_max_stars:
            top_item = Top(
                org_name=repo["owner"]["login"],
                repo_name=repo["name"],
                stars_count=repo["stargazers_count"]
            )
            list_add_db.append(top_item)
        self.session.add_all(list_add_db)
        self.session.commit()
        logging.info("Data about top repo stars successfully wrote.")

    def show_all(self):
        logging.info("Show top repo stars.")
        top_repos = self.session.query(Top).all()

        logging.info("--------> Print results. <-----------")
        print(f"All quantity: {len(top_repos)}")
        logging.info(f"All quantity: {len(top_repos)}")

        table = BeautifulTable()
        table.columns.header = ["id", "org_name", "repo_name", "stars_count"]
        for repo in top_repos:
            table.rows.append([repo.id, repo.org_name, repo.repo_name, repo.stars_count])

        print(table)
        logging.info(table)

    @staticmethod
    def remove_db():
        """Remove database"""
        logging.info("Check the old database")
        if os.path.exists(FILE_DB_NAME):
            os.remove(FILE_DB_NAME)
            logging.info("Old file db remove.")