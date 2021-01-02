from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import json
import time
import urllib.request
import finnhub
import pandas as pd

def call_API(ticker, timeout):
    finnhub_client = finnhub.Client(api_key="bvkm7nn48v6vtohist0g")
    response = finnhub_client.quote(ticker)
    return response

start = time.perf_counter()
# stocklist = ["MMM", "ABT", "ABBV", "ABMD", "ACN", "ATVI", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALXN", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "ANTM", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG", "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BLL", "BAC", "BK", "BAX", "BDX", "BRK.B", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BF.B", "CHRW", "COG", "CDNS", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CERN", "CF", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "CXO", "COP", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DISCA", "DISCK", "DISH", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD", "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES", "RE", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV", "FLT", "FLIR", "FLS", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HAL", "HBI", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HFC", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUM", "HBAN", "HII", "IEX", "IDXX", "INFO", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ", "JCI", "JPM", "JNPR", "KSU", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LB", "LHX", "LH", "LRCX", "LW", "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM"]
stocklist = ["MMM", "ABT", "ABBV", "ABMD", "ACN", "ATVI", "ADBE", "AMD", "AAP"]
results = {}
df = pd.DataFrame(columns=["ticker", "price"])
with ThreadPoolExecutor(max_workers=8) as executor:
    future_to_url = {executor.submit(call_API, stock, 60): stock for stock in stocklist}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            print(data)
        except Exception as e:
            print(f"{url} generated an exception: {e}")
print(results)
finish = time.perf_counter()
print(finish - start)
