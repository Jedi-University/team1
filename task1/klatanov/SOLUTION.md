git mkdir klatanov
cd klatanov
git clone --branch=v1-8-stable https://github.com/apache/airflow
git add *
git commit -m "Add airflow"
git checkout v1-8-stable
git add *
git commit -m "WIP: Testing working with git"
git checkout main
git branch -f fix
git log --since='2017-06-16'
git rebase --onto 9831f4 4e370f
git checkout main
git cd ..
git add *
git commit -m "upd"
git push
git checkout main
git push