import git
import time


def main():
    print('hello')
    repo = git.Repo("/home/mateusz/Documents/python")
    assert not repo.bare
    headcommit = repo.head.commit
    commit_time = time.asctime(time.gmtime(headcommit.committed_date))
    print(commit_time)
    file_list = repo.tree()
    for file in file_list:
        commits = list(repo.iter_commits('--all', max_count=100, since='10.days.ago', paths=file.name))
        print(file.name + " : " + str(len(commits)) + " commits")
        
if __name__ == "__main__":
    main()

