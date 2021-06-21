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

const merge = (pk: string | number): Promise<any> =>
  axios.patch(`${HOST}${ENDPOINT}/${pk}/merge`);

const close = (pk: string | number): Promise<any> =>
  axios.patch(`${HOST}${ENDPOINT}/${pk}/close`);

export { getPullRequests, getPullRequest, createPullRequest, merge, close };
