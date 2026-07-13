from app.platform_core.api_search.catalog import api_search_catalog

class APIEndpointSearchService:
    def find(self, q: str = ""):
        query = (q or "").strip().lower()
        items = api_search_catalog.endpoints()
        if query:
            items = [i for i in items if query in i["path"].lower() or query in i["tag"].lower() or query in i["summary"].lower()]
        return {"ready": True, "query": query, "count": len(items), "items": items}

api_endpoint_search_service = APIEndpointSearchService()
