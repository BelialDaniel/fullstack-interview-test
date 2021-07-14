import Commit from "./commit"

export default interface Branch {
  name: string
  commits: Array<Commit>
}
