import Author from "./author";

export default interface PullRequest {
  id?: number;
  author: Author;
  title: string;
  description: string;
  status: string;
  from_branch: string;
  to_branch: string;
}
