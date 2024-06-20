import axios from "axios";

// const HOST = "https://vertexai-search-demo-xiswadvybq-as.a.run.app" ;
const HOST = "http://localhost:8000";
/**
 * Sends a search request to the backend API.
 *
 * @param {string} query The search query to use.
 * @returns {Promise<object|null>} A promise that resolves with the search results, or null if an error occurred.
 */

async function search(payload) {
  try {
    const response = await axios.post(`${HOST}/search`, {
      query: payload.query,
      pageSize: payload.page_size,
      summary_result_count: payload.summary_result_count,
      max_snippet_count: payload.max_snippet_count,
      max_extractive_segment_count: payload.max_extractive_segment_count,
      max_extractive_answer_count: payload.max_extractive_answer_count,
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching search results:", error);
    return null;
  }
}

export { search };
