import time
from git import Repo

class GitRepo:
    path = '../'
    repo = None

    def __init__(self, path=None):
        if path:
            self.path = path
        self.repo = Repo(self.path)

    def get_repo(self):
        if not self.repo:
            self.repo = Repo(self.path)
        return self.repo


class GitData(GitRepo):

    def _find_branch(self, name):
        repo = self.get_repo()
        branches = repo.branches

        if not branches:
            return

        branch = next((branch for branch in branches if branch.name == name), None)
        return branch
    
    def _get_date_formated(self, date):
        return time.strftime("%a, %d %b %Y %H:%M",
                             time.gmtime(date))
                            
    def _fix_name(self, name):
        return name
    
    def _get_commits(self, branch_name=None):
        repo = self.get_repo()
        if branch_name:
            return list(repo.iter_commits(branch_name))
        return list(repo.iter_commits())
    
    def _get_commit_dict(self, commit):
        return dict(message=commit.message,
                    key=commit.hexsha,
                    created_on=self._get_date_formated(commit.committed_date),
                    author=dict(name=commit.author.name, email=commit.author.email))

    def get_branches(self):
        try:
            repo = self.get_repo()
            return [dict(name=branch.name, pk=self._fix_name(branch.name))
                    for branch in repo.branches]
        except Exception as exception:
            print(exception)
    
    def get_branch(self, name):
        if not name:
            raise Exception('No branch name provided')
        
        branch = self._find_branch(name)
        if not branch:
            raise Exception(f'Branch {name} doest not exist')

        commits = [self._get_commit_dict(commit)
                   for commit in self._get_commits(name)]

        branch_info = dict(
            name=branch.name,
            commits=commits
        )
        return branch_info
    
    def get_commits(self):
        commits = [dict(message=commit.message,
                        key=commit.hexsha,
                        created_on=self._get_date_formated(commit.committed_date),
                        author=dict(name=commit.author.name, email=commit.author.email))
                    for commit in self._get_commits()]
        return commits
    
    def get_commit(self, hash):
        if not hash:
            raise Exception('No commit hash provided')
        
        commits = self._get_commits()
        commit = next((commit for commit in commits if commit.hexsha == hash), None)
        if not commit:
            raise Exception(f'No commit fount with hash {hash}')

        return self._get_commit_dict(commit)



