import axios from "axios"

const HOST = "http://localhost:8000/git_api/"
const ENDPOINT = "commits"

const getCommits = (): Promise<Array<any>> => axios.get(`${HOST}${ENDPOINT}`)

const getCommit = (pk: string): Promise<any> =>
  axios.get(`${HOST}${ENDPOINT}/${pk}`)

export { getCommits, getCommit }
