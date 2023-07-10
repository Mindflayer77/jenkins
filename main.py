import git
import time
from html_class import HTML


def main():
    print('hello')
    repo = git.Repo("/home/mateusz/Documents/python")
    assert not repo.bare
    headcommit = repo.head.commit
    commit_time = time.asctime(time.gmtime(headcommit.committed_date))
    num_of_all_commits = 0
    print(commit_time)
    data = {}
    file_list = repo.tree()
    for file in file_list:
        commits = list(repo.iter_commits('--all', max_count=100, since='10.days.ago', paths=file.name))
        data[file.name] = len(commits)
        num_of_all_commits += len(commits)
        print(file.name + " : " + str(len(commits)) + " commits")
    print('Number of all commits: ' + str(num_of_all_commits))
    HTML.create(data)

if __name__ == "__main__":
    main()

