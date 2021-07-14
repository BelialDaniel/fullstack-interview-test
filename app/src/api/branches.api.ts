import axios from "axios"
import BranchList from "@/models/branchList"
import Branch from "@/models/branch"

const HOST = "http://localhost:8000/git_api/"
const ENDPOINT = "branches"

const getBranches = (): Promise<Array<BranchList>> =>
  axios.get(`${HOST}${ENDPOINT}`)

const getBranch = (pk: string): Promise<Branch> =>
  axios.get(`${HOST}${ENDPOINT}/${pk}`)

export { getBranches, getBranch }
