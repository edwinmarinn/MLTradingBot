import datetime as dt

from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca

from ml_trader import MLTrader
from settings import settings


def main():
    start_date = dt.datetime(2020, 1, 1)
    end_date = dt.datetime(2023, 12, 31)
    broker = Alpaca(settings.alpaca_credentials)
    strategy = MLTrader(
        name="mlstrat", broker=broker, parameters={"symbol": "SPY", "cash_at_risk": 0.5}
    )
    strategy.backtest(
        YahooDataBacktesting,
        start_date,
        end_date,
        parameters={"symbol": "SPY", "cash_at_risk": 0.5},
    )
    # trader = Trader()
    # trader.add_strategy(strategy)
    # trader.run_all()


if __name__ == "__main__":
    main()
