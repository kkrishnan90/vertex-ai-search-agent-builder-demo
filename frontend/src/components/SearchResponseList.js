import parse from "html-react-parser";

/**
 * Renders a single response item from the search results.
 *
 * @param {object} props The props object containing the response data.
 * @param {object} props.response The search response object.
 * @returns {JSX.Element} The JSX element representing the response item.
 */
const ResponseItem = (props) => {
  console.log("API pass as props", props.response);
  return (
    <div className="bg-gray rounded-md p-4 w-full mb-8">
      <div className="flex-col overflow-y-auto items-center justify-center">
        {props.response.results &&
          props.response.results.map((item) => {
            return getItem(item, props.response);
          })}
      </div>
    </div>
  );
};

/**
 * Renders a single item from the search results.
 *
 * @param {object} item The search result item.
 * @param {object} response The search response object.
 * @returns {JSX.Element} The JSX element representing the item.
 */
function getItem(item, response) {
  return (
    <div className="block bg-white rounded-md p-4 w-full mb-8">
      {getFileName(item.document.structData.title)}
      {getReferences(
        response.summary.summaryWithMetadata.references[0].chunkContents
      )}
      {getSnippets(item.document.derivedStructData.snippets)}
      {getExtractiveAnswer(item.document.derivedStructData.extractive_answers)}
      {getExtractiveSegments(
        item.document.derivedStructData.extractive_segments
      )}
    </div>
  );
}

/**
 * Renders the file name from the document title.
 *
 * @param {string} docTitle The document title.
 * @returns {JSX.Element} The JSX element representing the file name.
 */
function getFileName(docTitle) {
  return (
    <h3 className="text-md font-medium mb-2 text-sky-900">
      from:{" "}
      {docTitle.toString().includes("docs/")
        ? docTitle.toString().split("/")[1]
        : docTitle.toString()}
    </h3>
  );
}

/**
 * Renders the references from the search response.
 *
 * @param {array} referenceItems The array of reference items.
 * @returns {JSX.Element} The JSX element representing the references.
 */
function getReferences(referenceItems) {
  return (
    <div className="block mt-2 mb-2">
      <h1 className="text-md font-bold">References</h1>
      <div className="block ">
        {referenceItems &&
          referenceItems.map((item) => {
            return (
              <div className="block mb-2">
                <h1 className="text-xs font-medium text-violet-900">
                  page {item.pageIdentifier}
                </h1>
                <h1 className="text-sm">{item.content}</h1>
              </div>
            );
          })}
      </div>
    </div>
  );
}

/**
 * Renders the snippets from the search response.
 *
 * @param {array} snippetItems The array of snippet items.
 * @returns {JSX.Element} The JSX element representing the snippets.
 */
function getSnippets(snippetItems) {
  return (
    <div className="block mt-2 mb-2">
      <h1 className="text-md font-bold">Snippets</h1>
      {snippetItems &&
        snippetItems.map((item) => {
          return (
            <div className="block mb-2">
              <h1 className="text-sm prose">{parse(item.snippet)}</h1>
            </div>
          );
        })}
    </div>
  );
}

/**
 * Renders the extractive answers from the search response.
 *
 * @param {array} extractiveAnswerItems The array of extractive answer items.
 * @returns {JSX.Element} The JSX element representing the extractive answers.
 */
function getExtractiveAnswer(extractiveAnswerItems) {
  return (
    <div className="block mt-2 mb-2">
      <h1 className="text-md font-bold">Extractive Answers</h1>
      <div className="block mb-2">
        {extractiveAnswerItems &&
          extractiveAnswerItems.map((item) => {
            return (
              <div className="block">
                <h1 className="text-xs font-medium text-orange-700">
                  page {item.pageNumber}
                </h1>
                <h1 className="text-sm">{item.content}</h1>
              </div>
            );
          })}
      </div>
    </div>
  );
}

/**
 * Renders the extractive segments from the search response.
 *
 * @param {array} extractiveSegmentItems The array of extractive segment items.
 * @returns {JSX.Element} The JSX element representing the extractive segments.
 */
function getExtractiveSegments(extractiveSegmentItems) {
  return (
    <div className="block mt-2 mb-2">
      <h1 className="text-md font-bold">Extractive Segments</h1>
      <div className="block mb-2">
        {extractiveSegmentItems &&
          extractiveSegmentItems.map((item) => {
            return (
              <div className="block mb-2">
                <div className="flex justify-between">
                  <h1 className="text-xs font-medium text-orange-700">
                    page {item.pageNumber}
                  </h1>
                  <h1 className="text-xs font-medium text-green-800">
                    relevance score: {item.relevanceScore.toFixed(2)}
                  </h1>
                </div>
                <h1 className="text-sm">{item.content}</h1>
              </div>
            );
          })}
      </div>
    </div>
  );
}

export default ResponseItem;
