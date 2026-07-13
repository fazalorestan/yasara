from pydantic import BaseModel, Field

class FavoriteSymbolBookV1(BaseModel):
    owner_id: str = "default"
    symbols: list[str] = Field(default_factory=list)

class FavoriteSymbolServiceV1:
    def add(self, book: FavoriteSymbolBookV1, symbol: str) -> FavoriteSymbolBookV1:
        normalized = symbol.upper()
        if normalized not in book.symbols:
            book.symbols.append(normalized)
        return book

    def remove(self, book: FavoriteSymbolBookV1, symbol: str) -> FavoriteSymbolBookV1:
        normalized = symbol.upper()
        book.symbols = [s for s in book.symbols if s != normalized]
        return book
