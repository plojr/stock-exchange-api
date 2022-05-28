import database

INVALID_TICKER_DATE = "Not a valid ticker or date"

def get_closing_price(ticker, date):
    global INVALID_TICKER_DATE
    conn, cursor = database.get_cursor()
    cursor.execute("SELECT price "\
                   "FROM stock_exchange.adjusted_prices ap "\
                   "INNER JOIN stock_exchange.stock s ON s.id = ap.stock_id "\
                   "WHERE s.ticker = %s AND ap.date = %s", (ticker, date))
    result = cursor.fetchone()
    if result is None:
        return INVALID_TICKER_DATE
    return result[0]

def get_volume(ticker, date):
    global INVALID_TICKER_DATE
    conn, cursor = database.get_cursor()
    cursor.execute("SELECT volume "\
                   "FROM stock_exchange.adjusted_prices ap "\
                   "INNER JOIN stock_exchange.stock s ON s.id = ap.stock_id "\
                   "WHERE s.ticker = %s AND ap.date = %s", (ticker, date))
    result = cursor.fetchone()
    if result is None:
        return INVALID_TICKER_DATE
    return result[0]

def get_variation(ticker, initial_date, finish_date):
    global INVALID_TICKER_DATE
    price1 = get_closing_price(ticker, initial_date)
    if price1 == INVALID_TICKER_DATE:
        return "Invalid initial date or ticker"
    price2 = get_closing_price(ticker, finish_date)
    if price2 == INVALID_TICKER_DATE:
        return "Invalid finish date"
    return price2/price1 - 1
