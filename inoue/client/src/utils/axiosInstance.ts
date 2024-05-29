import axios from 'axios'

const baseURL = "http://127.0.0.1:5000/api";

export const axiosInstance = axios.create({
  baseURL
});

axiosInstance.interceptors.request.use(config => {
  const accessToken = 'accessToken';
  config.headers.Authorization = accessToken ? `Bearer ${accessToken}` : '';
  return config;
});

axiosInstance.interceptors.response.use(
  response => response,
  error => {
    return Promise.reject(error);
  }
);
