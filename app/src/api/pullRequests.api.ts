import PullRequest from "@/models/pullRequest";
import axios from "axios";

const HOST = "http://localhost:8000/git_api/";
const ENDPOINT = "pull_requests";

const getPullRequests = (): Promise<Array<any>> =>
  axios.get(`${HOST}${ENDPOINT}`);

const getPullRequest = (id: number): Promise<any> =>
  axios.get(`${HOST}${ENDPOINT}/${id}`);

const createPullRequest = (data: PullRequest): Promise<any> =>
  axios.post(`${HOST}${ENDPOINT}`, data);

export { getPullRequests, getPullRequest, createPullRequest };
