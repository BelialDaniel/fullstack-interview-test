from git import Repo


class GitRepo:
    path = '../'

    def __init__(self, path=None):
        if path:
            self.path = path

    def get_repo(self):
        return Repo(self.path)


class GitData(GitRepo):
    def get_branches(self):
        try:
            repo = self.get_repo()
            return [branch.name for branch in repo.branches]
        except Exception:
            pass
    
    def get_branch(name):
        pass