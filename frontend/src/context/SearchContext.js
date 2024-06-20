// src/context/SearchContext.js
import React, { createContext, useState } from "react";

/**
 * Creates a context for managing search results.
 *
 * @type {React.Context<{ searchResults: any[]; setSearchResults: React.Dispatch<React.SetStateAction<any[]>>; searchTermFromSearchComponent: string; setSearchTermFromSearchComponent: React.Dispatch<React.SetStateAction<string>>; }>}
 */
const SearchContext = createContext();

/**
 * A component that provides search results to its children.
 *
 * @param {object} props The props object containing the children to render.
 * @param {React.ReactNode} props.children The children to render.
 * @returns {JSX.Element} The JSX element representing the search provider.
 */
const SearchProvider = ({ children }) => {
  const [searchResults, setSearchResults] = useState([]);
  const [searchTermFromSearchComponent, setSearchTermFromSearchComponent] =
    useState("");

  return (
    <SearchContext.Provider
      value={{
        searchResults,
        setSearchResults,
        searchTermFromSearchComponent,
        setSearchTermFromSearchComponent,
      }}>
      {children}
    </SearchContext.Provider>
  );
};

export { SearchContext, SearchProvider };
