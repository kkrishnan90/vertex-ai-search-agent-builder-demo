// src/components/SearchComponent.js
import React, { useState, useContext } from "react";
import { SearchContext } from "../context/SearchContext";

const SearchComponent = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const { setSearchTermFromSearchComponent } = useContext(SearchContext);
  const [isLoading] = useState(false);

  const onKeyPressHandler = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      setSearchTermFromSearchComponent(e.target.value);
    }
  };

  return (
    <div className="flex items-center w-full">
      <input
        type="text"
        id="searchInput"
        className="flex-grow px-4 py-2 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500 mr-4"
        placeholder="Search..."
        value={searchTerm}
        onKeyDown={onKeyPressHandler}
        disabled={isLoading}
        onChange={(event) => {
          setSearchTermFromSearchComponent(event.target.value);
          setSearchTerm(event.target.value);
        }}
      />
    </div>
  );
};

export default SearchComponent;
