import argparse
import time

import speedtest
import wandb


def main():
    parser = argparse.ArgumentParser(description="Monitor and log internet speeds using Wandb.")
    parser.add_argument("-i", "--interval", type=int, default=60,
                        help="Time interval between measurements in seconds (default: 60)")
    args = parser.parse_args()

    # Initialize Wandb project
    wandb.init(project="speedlogger", dir="/tmp/wandb")

    # Create Speedtest object
    st = speedtest.Speedtest()

    # Perform speed tests at regular intervals and log results using Wandb
    while True:
        try:
            # Select the best server
            st.get_best_server()

            # Measure download speed
            download_speed = st.download() / 1_000_000  # Convert to Mbps

            # Measure upload speed
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps

            # Get ping
            ping = st.results.ping

            # Get server ID
            server_id = st.results.server["id"]

            # Save logs to Wandb
            wandb.log({
                "download_speed": download_speed,
                "upload_speed": upload_speed,
                "ping": ping,
                "server_id": server_id
            })

            print(
                f"Download: {download_speed} Mbps, Upload: {upload_speed} Mbps, Ping: {ping} ms, Server ID: {server_id}")

        except Exception as e:
            print(f"Error during speed test: {e}")

        # Wait until next measurement
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
