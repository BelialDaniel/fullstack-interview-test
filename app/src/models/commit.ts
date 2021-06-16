import Author from "./author";
import Files from "./files";

export default interface Commit {
  message: string;
  key: string;
  created_on: string;
  author: Author;
  files?: Files;
}
