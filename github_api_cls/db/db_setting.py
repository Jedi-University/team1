
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from beautifultable import BeautifulTable

import logging
logger = logging.getLogger(__name__)


FILE_DB_NAME = "top_repos.sqlite"
DB_PATH = f"sqlite:///db/{FILE_DB_NAME}"
Base = declarative_base()


class Top(Base):
    __tablename__ = "top"

    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    org_name = sa.Column(sa.TEXT)
    repo_name = sa.Column(sa.TEXT)
    stars_count = sa.Column(sa.INTEGER)


class DB:

    def __init__(self):
        logger.info("Start connect to the database")
        self.db_path = DB_PATH
        self.engine = sa.create_engine(self.db_path, echo=True)
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(self.engine)()
        logger.info("Session create")

    def write_db(self, twenty_repos_max_stars):
        self.remove_db()
        logger.info("Start write to the database.")
        list_add_db = []
        for repo in twenty_repos_max_stars:
            top_item = Top(
                org_name=repo["owner"]["login"],
                repo_name=repo["name"],
                stars_count=int(repo["stargazers_count"])
            )
            list_add_db.append(top_item)
        self.session.add_all(list_add_db)
        self.session.commit()
        logger.info("Data about top repo stars successfully wrote.")
        self.close_connect_db()

    def show_all(self):
        logger.info("Show top repo stars.")
        top_repos = self.session.query(Top).all()

        logger.info("--------> Print results. <-----------")
        logger.info(f"All quantity: {len(top_repos)}")

        table = BeautifulTable()
        table.columns.header = ["id", "org_name", "repo_name", "stars_count"]
        for repo in top_repos:
            table.rows.append([repo.id, repo.org_name, repo.repo_name, repo.stars_count])

        logger.info(table)

    def close_connect_db(self):
        logger.info("Connect db close")
        self.engine.dispose()

    def remove_db(self):
        """Remove table"""
        logger.info("Remove all row in table top")
        self.session.query(Top).delete()

