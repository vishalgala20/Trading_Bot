from client import BinanceFuturesClient
from cli import get_args
from logger import setup_logger

logger = setup_logger()

def main():

    args = get_args()

    logger.info("Starting trading bot")

    print("\nOrder Request Summary")
    print("---------------------")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    print(f"Price: {args.price}")

    logger.info(f"Placing {args.side} {args.type} order for {args.symbol}")

    client = BinanceFuturesClient()

    order = client.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder Response")
    print("----------------")

    if "error" in order:

        logger.error("Order failed")
        logger.error(order["error"])

        print("Order Failed")
        print(order["error"])

    else:

        logger.info("Order placed successfully")

        print("Order Placed Successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))


if __name__ == "__main__":
    main()