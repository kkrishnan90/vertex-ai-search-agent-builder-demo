import React, { useState, useContext } from "react";
import ParameterInput from "./ParameterInput";
import LoadingModal from "./LoadingModal";
import { SearchContext } from "../context/SearchContext";
import { search } from "../api/backend";

const ParameterPanel = () => {
  const { searchTermFromSearchComponent, setSearchResults } =
    useContext(SearchContext);
  const [isLoading, setIsLoading] = useState(false);
  const [pageSize, setPageSize] = useState(1);
  const [summaryResultCount, setSummaryResultCount] = useState(1);
  const [maxSnippetCount, setMaxSnippetCount] = useState(1);
  const [maxExtractiveAnswerCount, setMaxExtractiveAnswerCount] = useState(1);
  const [maxExtractiveSegmentCount, setMaxExtractiveSegmentCount] = useState(1);

  const handleSearch = async () => {
    if (!searchTermFromSearchComponent) {
      alert("Please enter a search query.");
      return;
    }

    setIsLoading(true);

    const searchParams = {
      query: searchTermFromSearchComponent,
      page_size: pageSize,
      summary_result_count: summaryResultCount,
      max_snippet_count: maxSnippetCount,
      max_extractive_answer_count: maxExtractiveAnswerCount,
      max_extractive_segment_count: maxExtractiveSegmentCount,
    };

    console.log("Search Params: ", searchParams); // Log the search parameters

    const results = await search(searchParams); // Call the search function with the payload
    setSearchResults(results);
    setIsLoading(false);
  };

  return (
    <div className="flex w-1/4 bg-slate-50 rounded-lg flex-col p-4">
      <p className="text-md">Adjust Parameters</p>

      <ParameterInput
        label="Page Size"
        id="pageSize"
        defaultValue="1"
        min="1"
        placeholder="Enter page size"
        onChange={(e) => setPageSize(Number(e.target.value))}
      />
      <ParameterInput
        label="Summary Result Count"
        id="summaryResultCount"
        defaultValue="1"
        min="1"
        placeholder="Enter summary result count"
        onChange={(e) => setSummaryResultCount(Number(e.target.value))}
      />
      <ParameterInput
        label="Max Snippet Count"
        id="maxSnippetCount"
        defaultValue="1"
        min="1"
        placeholder="Enter max snippet count"
        onChange={(e) => setMaxSnippetCount(Number(e.target.value))}
      />
      <ParameterInput
        label="Max Extractive Answer Count"
        id="maxExtractiveAnswerCount"
        defaultValue="1"
        min="1"
        placeholder="Enter max extractive answer count"
        onChange={(e) => setMaxExtractiveAnswerCount(Number(e.target.value))}
      />
      <ParameterInput
        label="Max Extractive Segment Count"
        id="maxExtractiveSegmentCount"
        defaultValue="1"
        min="1"
        placeholder="Enter max extractive segment count"
        onChange={(e) => setMaxExtractiveSegmentCount(Number(e.target.value))}
      />

      {isLoading ? (
        <LoadingModal isOpen={isLoading} />
      ) : (
        <button
          className="bg-gray-800 hover:bg-blue-700 text-white font-bold py-2 px-4 mr-4 rounded-md"
          onClick={handleSearch}>
          Search
        </button>
      )}
    </div>
  );
};

export default ParameterPanel;
