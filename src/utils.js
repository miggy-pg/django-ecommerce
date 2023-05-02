import axios from 'axios';

import { endPoint, getAuthorizationHeader } from './constants';
export const authAxios = axios.create({
    baseURL: endPoint,
    headers: {
        Authorization: `Token ${localStorage.getItem("token")}`
    }
});