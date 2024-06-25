# Python SMTP Proxy

A demo to proxy SMTP requests.

## Todo
- [ ] on CTRL+C, stop server.py process
- [ ] add proper loggers
- [ ] support authentication (username & password)
- [ ] support SSL (465) and TLS (587)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/ludndev/python-smtp-proxy.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Edit the config
   ```python
    SMTP_PROXY_HOST = "127.0.0.1"
    SMTP_PROXY_PORT = 1025
   ```

4. Run the server:
   ```
   python server.py
   ```

5. Run the demo client:
   ```
   python client.py
   ```

## Contributing

Contributions to this project are welcome! If you have any ideas for new features, bug fixes, or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
