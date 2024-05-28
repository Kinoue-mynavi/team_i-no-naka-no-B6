import useSWR, { SWRConfiguration } from "swr";
import { fetcher } from "../utils/fetcher";

export const useFetchData = <T>(url: string, options?: SWRConfiguration) => {
    const { data, error, isValidating, isLoading, mutate } = useSWR<T>(url, () => fetcher<T>(url), { ...options })
  
    return {
      data,
      isLoading,
      error,
      isValidating,
      mutate
    }
};