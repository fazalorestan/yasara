from app.desktop_ui_v1.order_book_view import OrderBookViewBuilderV1

def test_order_book_view_total():
    view = OrderBookViewBuilderV1().build([[100,2]], [[101,1]])
    assert view.bids[0].total == 200
