# SpeedLogger

SpeedLogger is a simple tool to monitor and log your internet connection's upload and download speeds, server ID, and ping at regular intervals using speedtest-cli and Weights & Biases (wandb).

## Installation

1. Install the `speedlogger` package using pip:

```shell
pip install speedlogger
```

2. Create a [Weights & Biases](https://wandb.ai/) account if you don't have one already.

4. Log in to your Weights & Biases account:

Follow the instructions to get your API key and finish the login process.
```shell
wandb login
```



## Usage

1. Run the `speedlogger` command with the desired time interval (in seconds) between measurements:

```shell
speedlogger --interval 60
```

The default interval is 60 seconds. You can change it using the `--interval` option.

2. The logged data will be sent to your Weights & Biases account under the `speedlogger` project. You can view the logs and visualize the results on the [Weights & Biases dashboard](https://wandb.ai/).

Please note that the internet speed measurements may consume a significant amount of data, especially when running the tool for extended periods. Make sure to consider any data usage limitations your internet service provider may impose.