from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from wrapper import proto_to_dict
import os

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
AGENT_APPLICATION_ID = os.getenv("AGENT_APPLICATION_ID")


@proto_to_dict
def search_discovery_engine(
    search_query: str,
    location: str = "global",
    summary_result_count: int = 5,
    page_size: int = 100,
    max_snippet_count: int = 5,
    include_citations: bool = True,
    use_semantic_chunks: bool = True,
    max_extractive_answer_count: int = 5,
    max_extractive_segment_count: int = 5,
) -> List[discoveryengine.SearchResponse]:
    """
    Searches the Discovery Engine for documents matching the provided query.

    Args:
        search_query (str): The search query to use.
        location (str, optional): The location of the Discovery Engine instance. Defaults to "global".
        summary_result_count (int, optional): The number of summary results to return. Defaults to 5.
        page_size (int, optional): The maximum number of results to return per page. Defaults to 1000.
        max_snippet_count (int, optional): The maximum number of snippets to return per result. Defaults to 5.
        include_citations (bool, optional): Whether to include citations in the search results. Defaults to True.
        use_semantic_chunks (bool, optional): Whether to use semantic chunks for search. Defaults to True.
        max_extractive_answer_count (int, optional): The maximum number of extractive answers to return per result. Defaults to 5.
        max_extractive_segment_count (int, optional): The maximum number of extractive segments to return per result. Defaults to 5.

    Returns:
        List[discoveryengine.SearchResponse]: A list of SearchResponse objects containing the search results.
    """
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(
            api_endpoint=f"{LOCATION}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search app serving config
    serving_config = f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/engines/{AGENT_APPLICATION_ID}/servingConfigs/default_config"

    # Optional: Configuration options for search
    # Refer to the `ContentSearchSpec` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        # For information about snippets, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/snippets
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True,
            max_snippet_count=max_snippet_count
        ),
        extractive_content_spec=discoveryengine.SearchRequest.ContentSearchSpec.ExtractiveContentSpec
        (
            max_extractive_answer_count=max_extractive_answer_count,
            max_extractive_segment_count=max_extractive_segment_count,
            return_extractive_segment_score=True,
        ),
        # For information about search summaries, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=summary_result_count,
            include_citations=include_citations,
            ignore_adversarial_query=True,
            use_semantic_chunks=use_semantic_chunks,
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        content_search_spec=content_search_spec,
        page_size=page_size,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    response = client.search(request)
    return response
